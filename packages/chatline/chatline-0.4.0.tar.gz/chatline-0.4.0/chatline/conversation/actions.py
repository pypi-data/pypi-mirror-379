# conversation/actions.py

from typing import List, Tuple, Dict, Any, Optional
import asyncio
import sys
import termios
import tty
import os
import json

from .save_manager import ConversationSaveManager


class ConversationActions:
    """Manages conversation flow and actions."""

    def __init__(
        self,
        display,
        stream,
        history,
        messages,
        preface,
        logger,
        conclusion_string=None,
        loading_message=None,
        save_directory="./saved_conversations/",
    ):
        self.display = display
        self.terminal = display.terminal
        self.style = display.style
        self.animations = display.animations
        self.stream = stream
        self.generator = stream.get_generator()
        self.history = history
        self.messages = messages
        self.preface = preface
        self.logger = logger
        self.conclusion_string = conclusion_string
        self.loading_message = loading_message
        self.save_manager = ConversationSaveManager(save_directory)

        # UI-specific state
        self.is_silent = False
        self.prompt = ""
        self.last_user_input = ""
        self.preconversation_styled = ""
        self.conclusion_triggered = False
        self.disable_first_operations = False  # Flag to disable Ctrl+R/E/U for first response after loading

        # Local turn tracking (independent from conversation state)
        self.current_turn = 0
        self.history_index = -1

        # Detect remote vs. embedded mode (for generator usage)
        self.is_remote_mode = hasattr(stream, "endpoint")
        if self.is_remote_mode:
            self.logger.debug("Using remote mode for message generation")
        else:
            self.logger.debug("Using embedded mode for message generation")

    def _get_system_prompt(self) -> str:
        """Return the first system prompt found in our messages array, else empty."""
        for msg in self.messages.messages:
            if msg.role == "system":
                return msg.content
        return ""

    def _get_last_user_input(self) -> str:
        """Return the last user input from messages, else empty."""
        for msg in reversed(self.messages.messages):
            if msg.role == "user":
                return msg.content
        return ""

    def _get_last_assistant_response(self) -> str:
        """Return the last assistant response from messages, else empty."""
        for msg in reversed(self.messages.messages):
            if msg.role == "assistant":
                return msg.content
        return ""

    def _handle_state_update(self, new_state: Dict[str, Any]) -> None:
        """Handle conversation state updates from a remote provider."""
        if self.logger:
            self.logger.debug("Received state update from backend")

        # CRITICAL FIX: Ensure messages from state are properly incorporated into local tracking
        if "messages" in new_state and new_state["messages"]:
            state_messages = new_state["messages"]
            current_messages = self.messages.messages

            # If we have fewer messages locally than in the state, update from state
            if len(state_messages) > len(current_messages):
                # Clear existing messages to avoid duplication
                self.messages.messages.clear()

                # Add messages from state with proper turn numbering
                turn = 0
                for msg in state_messages:
                    role = msg["role"]
                    content = msg["content"]

                    # System message is turn 0, user/assistant pairs share turn numbers
                    if role == "system":
                        self.messages.add_message(role, content, 0)
                    else:
                        # For user/assistant messages, increment turn for user messages
                        if role == "user":
                            turn += 1
                        self.messages.add_message(role, content, turn)

                # Update current turn counter
                self.current_turn = turn

                if self.logger:
                    self.logger.debug(
                        f"Updated internal message tracking from state: {len(state_messages)} messages"
                    )

        # Original code: Update the state in the history
        self.history.update_state(**new_state)

    def _wrap_terminal_style(self, text: str, width: int) -> str:
        """Hard-wrap text at a fixed width to match terminal output."""
        if len(text) <= width:
            return text

        wrapped_chunks = []
        remaining_text = text
        while remaining_text:
            chunk = remaining_text[:width]
            wrapped_chunks.append(chunk)
            remaining_text = remaining_text[width:]
        return "\n".join(wrapped_chunks)

    async def _process_message(self, msg: str, silent: bool = False) -> Tuple[str, str]:
        """
        Process a user message, generate a response, store both in history.
        If silent=True, we do NOT show the user text in the terminal output.
        """
        try:
            self.current_turn += 1

            # Add the user message
            self.messages.add_message("user", msg, self.current_turn)
            self.last_user_input = msg

            # Build the input to the LLM
            sys_prompt = self._get_system_prompt()
            state_msgs = await self.messages.get_messages(sys_prompt)
            self.history.update_state(messages=state_msgs)
            self.history_index = self.history.get_latest_state_index()

            # Validate history index consistency
            if not self.validate_history_index():
                self.fix_history_index()

            # Output user text if not silent
            self.style.set_output_color("GREEN")
            prompt_text = "" if silent else f"> {msg}"
            loader = self.animations.create_dot_loader(
                prompt=prompt_text, no_animation=silent
            )

            # Prepare generator call
            current_state = self.history.create_state_snapshot()
            msgs_for_generation = await self.messages.get_messages(sys_prompt)

            if self.is_remote_mode:
                # Pass state to remote generator
                self.logger.debug("Calling remote generator with state and callback")
                raw, styled = await loader.run_with_loading(
                    self.generator(
                        messages=msgs_for_generation,
                        state=current_state,
                        state_callback=self._handle_state_update,
                    )
                )
            else:
                # Embedded mode
                self.logger.debug("Calling embedded generator with messages only")
                raw, styled = await loader.run_with_loading(
                    self.generator(messages=msgs_for_generation)
                )

            # Store assistant reply
            if raw:
                self.messages.add_message("assistant", raw, self.current_turn)

                new_state_msgs = await self.messages.get_messages(sys_prompt)
                self.history.update_state(messages=new_state_msgs)
                self.history_index = self.history.get_latest_state_index()

                # Validate history index consistency
                if not self.validate_history_index():
                    self.fix_history_index()

                # Check for conclusion string
                if self.conclusion_string:
                    if (
                        self.conclusion_string in raw
                        or self.conclusion_string in styled
                    ):
                        self.conclusion_triggered = True
                        self.terminal.hide_cursor()  # Ensure cursor is hidden
                        self.logger.debug(
                            f"Conclusion triggered: {self.conclusion_string}"
                        )

                # Build final UI text
                if not silent:
                    end_char = "..."
                    if msg.endswith(("?", "!")):
                        end_char = msg[-1] * 3
                    elif msg.endswith("."):
                        end_char = "..."
                    prompt_line = f"> {msg.rstrip('?.!')}{end_char}"
                    wrapped_prompt = self._wrap_terminal_style(
                        prompt_line, self.terminal.width
                    )
                    full_styled = f"{wrapped_prompt}\n\n{styled}"
                    return raw, full_styled
                else:
                    return raw, styled

            return "", ""

        except Exception as e:
            self.logger.error(f"Message processing error: {e}", exc_info=True)
            return "", ""

    def find_target_user_message(self) -> Optional[str]:
        """
        Find the target user message for rewind operation.
        Returns the second-to-last user message content, or None if not enough history.
        """
        user_messages = [m.content for m in self.messages.messages if m.role == "user"]
        if len(user_messages) < 2:
            return None
        return user_messages[-2]  # Second-to-last user message

    def find_state_before_user_message(
        self, target_user_content: str
    ) -> Optional[Tuple[int, Dict[str, Any]]]:
        """
        Find the history state that ends just before the target user message was added.

        Args:
            target_user_content: The content of the user message we want to rewind to

        Returns:
            Tuple of (state_index, state_data) or None if not found
        """
        if not self.history.state_history:
            return None

        # Search through history states to find the one that ends just before
        # the target user message was added
        for i in range(len(self.history.state_history) - 1, -1, -1):
            state = self.history.state_history[i]
            messages = state.get("messages", [])

            if not messages:
                continue

            # Get all user messages in this state
            user_messages = [
                msg["content"] for msg in messages if msg["role"] == "user"
            ]

            # If this state contains the target user message, we need to find
            # the previous state that ends just before it
            if target_user_content in user_messages:
                # Look for the last state before this target message was added
                target_user_index = user_messages.index(target_user_content)

                # We want a state that has all user messages up to (but not including) the target
                desired_user_count = target_user_index

                # Search backwards for a state with exactly the desired user count
                for j in range(i, -1, -1):
                    check_state = self.history.state_history[j]
                    check_messages = check_state.get("messages", [])
                    check_user_messages = [
                        msg["content"]
                        for msg in check_messages
                        if msg["role"] == "user"
                    ]

                    if len(check_user_messages) == desired_user_count:
                        return j, check_state

        return None

    def find_previous_user_message(self, current_user_content: str) -> Optional[str]:
        """
        Find the user message that came before the given user message.

        Args:
            current_user_content: Content of the current user message

        Returns:
            Content of the previous user message, or None if not found
        """
        user_messages = [m.content for m in self.messages.messages if m.role == "user"]

        try:
            current_index = user_messages.index(current_user_content)
            if current_index > 0:
                return user_messages[current_index - 1]
        except ValueError:
            pass

        return None

    def validate_history_index(self) -> bool:
        """
        Validate that history_index is consistent with actual history state.

        Returns:
            True if history_index is valid, False otherwise
        """
        if self.history_index < -1:
            self.logger.warning(
                f"Invalid history_index: {self.history_index} (below -1)"
            )
            return False

        history_length = len(self.history.state_history)
        if self.history_index >= history_length:
            self.logger.warning(
                f"Invalid history_index: {self.history_index} (beyond history length {history_length})"
            )
            return False

        return True

    def fix_history_index(self) -> None:
        """
        Fix history_index if it's out of bounds by setting it to the latest valid state.
        """
        if not self.validate_history_index():
            old_index = self.history_index
            self.history_index = self.history.get_latest_state_index()
            self.logger.info(
                f"Fixed history_index: {old_index} -> {self.history_index}"
            )

    async def introduce_conversation(self, intro_msg: str) -> Tuple[str, str, str]:
        """
        Show a preface panel (if any) or loading message, then process the first user message silently.
        Returns (raw_assistant_reply, combined_styled_text, empty_string_for_prompt).
        """
        self.terminal.hide_cursor()

        styled_panel = await self.preface.format_content(self.style)
        styled_panel = self.style.append_single_blank_line(styled_panel)

        # Track if we used loading animation
        used_loading_animation = False

        # Check if we should show loading message
        if not styled_panel.strip() and self.loading_message:
            used_loading_animation = True
            # Set flag to disable operations for the first response after loading
            self.disable_first_operations = True

            # Create reverse streamer with GRAY base color
            rev_streamer = self.animations.create_reverse_streamer("GRAY")

            # Stream the loading message word by word with GRAY color
            loading_prompt = self.loading_message
            await rev_streamer.fake_forward_stream_text(
                loading_prompt, delay=0.06, current_prompt="", base_color="GRAY"
            )

            # Now animate dots on the already-displayed loading message
            dot_count = 0
            animation_task = None
            animation_complete = asyncio.Event()
            first_chunk_received = False

            # Get gray color for dots
            gray_color = self.style.get_color("GRAY")
            reset_color = self.style.get_format("RESET")

            async def animate_dots():
                nonlocal dot_count
                resolved = False

                try:
                    while True:
                        # Just append/remove dots at cursor position with gray color
                        if dot_count == 0:
                            self.terminal.write(f"{gray_color}.{reset_color}")
                            dot_count = 1
                        elif dot_count == 1:
                            self.terminal.write(f"{gray_color}.{reset_color}")
                            dot_count = 2
                        elif dot_count == 2:
                            self.terminal.write(f"{gray_color}.{reset_color}")
                            dot_count = 3
                        else:  # dot_count == 3
                            # Check if we should stop on 3 dots
                            if resolved:
                                break
                            # Otherwise, clear dots and restart cycle
                            self.terminal.write("\b\b\b   \b\b\b")
                            dot_count = 0

                        # Check if animation should resolve after this iteration
                        if animation_complete.is_set() and not resolved:
                            resolved = True
                            # If we're not at 3 dots yet, continue the cycle

                        await asyncio.sleep(0.4)
                except asyncio.CancelledError:
                    # Clean up - ensure we always end with 3 gray dots
                    if dot_count < 3:
                        # Add remaining dots to get to 3
                        remaining_dots = "." * (3 - dot_count)
                        self.terminal.write(
                            f"{gray_color}{remaining_dots}{reset_color}"
                        )
                    raise

            # Process the message and prepare everything BEFORE starting animation
            self.current_turn += 1
            self.messages.add_message("user", intro_msg, self.current_turn)

            sys_prompt = self._get_system_prompt()
            state_msgs = await self.messages.get_messages(sys_prompt)
            self.history.update_state(messages=state_msgs)
            self.history_index = self.history.get_latest_state_index()

            if not self.validate_history_index():
                self.fix_history_index()

            # Prepare generator call
            current_state = self.history.create_state_snapshot()
            msgs_for_generation = await self.messages.get_messages(sys_prompt)

            # Now start dot animation with everything ready
            animation_task = asyncio.create_task(animate_dots())

            # Give animation task actual CPU time to start
            await asyncio.sleep(0.01)

            # Call generator and process response
            raw = ""
            assistant_styled = ""

            try:
                if self.is_remote_mode:
                    self.logger.debug(
                        "Calling remote generator with state and callback"
                    )
                    async for chunk in self.generator(
                        messages=msgs_for_generation,
                        state=current_state,
                        state_callback=self._handle_state_update,
                    ):
                        # First chunk - stop animation and wait for it to complete
                        if (
                            not first_chunk_received
                            and chunk.strip().startswith("data: ")
                            and chunk != "data: [DONE]"
                        ):
                            first_chunk_received = True
                            animation_complete.set()
                            # Wait for animation to finish on 3 dots
                            await animation_task
                            # Reset color before spacing
                            self.terminal.write(self.style.get_format("RESET"))
                            # Add spacing
                            self.terminal.write("\n\n")
                            # Set the output color for response chunks
                            self.style.set_output_color("GREEN")

                        # Process chunk only after animation is done
                        if (
                            first_chunk_received
                            and chunk.strip().startswith("data: ")
                            and chunk != "data: [DONE]"
                        ):
                            try:
                                data = json.loads(chunk[6:])
                                if "choices" in data and len(data["choices"]) > 0:
                                    content = (
                                        data["choices"][0]
                                        .get("delta", {})
                                        .get("content", "")
                                    )
                                    if content:
                                        r, s = await self.style.write_styled(content)
                                        raw += r
                                        assistant_styled += s
                            except json.JSONDecodeError:
                                pass
                else:
                    self.logger.debug("Calling embedded generator with messages only")
                    async for chunk in self.generator(messages=msgs_for_generation):
                        # First chunk - stop animation and wait for it to complete
                        if (
                            not first_chunk_received
                            and chunk.strip().startswith("data: ")
                            and chunk != "data: [DONE]"
                        ):
                            first_chunk_received = True
                            animation_complete.set()
                            # Wait for animation to finish on 3 dots
                            await animation_task
                            # Reset color before spacing
                            self.terminal.write(self.style.get_format("RESET"))
                            # Add spacing
                            self.terminal.write("\n\n")
                            # Set the output color for response chunks
                            self.style.set_output_color("GREEN")

                        # Process chunk only after animation is done
                        if (
                            first_chunk_received
                            and chunk.strip().startswith("data: ")
                            and chunk != "data: [DONE]"
                        ):
                            try:
                                data = json.loads(chunk[6:])
                                if "choices" in data and len(data["choices"]) > 0:
                                    content = (
                                        data["choices"][0]
                                        .get("delta", {})
                                        .get("content", "")
                                    )
                                    if content:
                                        r, s = await self.style.write_styled(content)
                                        raw += r
                                        assistant_styled += s
                            except json.JSONDecodeError:
                                pass
            finally:
                # Ensure animation is stopped
                animation_complete.set()
                if animation_task and not animation_task.done():
                    await animation_task

                # Flush any remaining styled content
                r, s = await self.style.flush_styled()
                raw += r
                assistant_styled += s

            # Store assistant reply
            if raw:
                self.messages.add_message("assistant", raw, self.current_turn)
                new_state_msgs = await self.messages.get_messages(sys_prompt)
                self.history.update_state(messages=new_state_msgs)
                self.history_index = self.history.get_latest_state_index()

                if not self.validate_history_index():
                    self.fix_history_index()

            # Build final styled output for proper storage
            # Format: gray loading message with dots inline, then spacing
            gray_color = self.style.get_color("GRAY")
            reset_color = self.style.get_format("RESET")
            styled_panel = f"{gray_color}{loading_prompt}...{reset_color}\n\n"

            # CRITICAL: Store in BOTH places for consistency
            self.preconversation_styled = styled_panel
            # Also add to preface so retry/rewind can find it
            self.preface.styled_content = styled_panel

            full_styled = styled_panel + assistant_styled

        else:
            # Original preface logic or no preface/loading
            if styled_panel.strip():
                await self.terminal.update_display(styled_panel, preserve_cursor=False)

            # Process message silently as before
            raw, assistant_styled = await self._process_message(intro_msg, silent=True)
            full_styled = styled_panel + assistant_styled

        # Check if full response exceeds screen height and set flag for future clearing
        lines = full_styled.split("\n")
        max_lines = self.terminal.height - 1  # Reserve one line for cursor/prompt
        if len(lines) > max_lines:
            self.terminal._had_long_content = True

        # Only clear and rewrite if we didn't use loading animation
        if not used_loading_animation:
            # Force scrollback clear to remove duplicate preface from initial display
            self.terminal.clear_screen_and_scrollback()
            self.terminal.write(full_styled)

        self.is_silent = True
        self.prompt = ""
        # Don't override preconversation_styled if we set it for loading message
        if not used_loading_animation:
            self.preconversation_styled = styled_panel
        self.terminal.hide_cursor()

        return raw, full_styled, ""

    async def process_user_message(
        self, user_input: str, intro_styled: str
    ) -> Tuple[str, str, str]:
        """
        Process a normal user message (visible in the terminal).
        """
        scroller = self.animations.create_scroller()
        await scroller.scroll_up(intro_styled, f"> {user_input}", 0.02)

        raw, styled = await self._process_message(user_input, silent=False)

        # Check if the full response content exceeds screen height and set flag for future clearing
        full_content = intro_styled + styled
        lines = full_content.split("\n")
        max_lines = self.terminal.height - 1  # Reserve one line for cursor/prompt
        if len(lines) > max_lines:
            self.terminal._had_long_content = True

        self.is_silent = False
        self.prompt = self.terminal.format_prompt(user_input)
        self.preface.clear()
        self.preconversation_styled = ""
        return raw, styled, self.prompt

    async def backtrack_conversation(
        self, intro_styled: str, is_retry: bool = False
    ) -> Tuple[str, str, str]:
        """
        Return to the previous user message, remove that user/assistant pair,
        then re-process or let the user edit it.
        """
        rev_streamer = self.animations.create_reverse_streamer()

        # Use whichever preconversation content is available
        preconversation_content = (
            self.preface.styled_content or self.preconversation_styled
        )

        await rev_streamer.reverse_stream(
            intro_styled,
            "",
            preconversation_text=preconversation_content,
        )

        last_msg = next(
            (m.content for m in reversed(self.messages.messages) if m.role == "user"),
            None,
        )
        if not last_msg:
            return "", intro_styled, ""

        # Remove the user+assistant pair
        user_idx = None
        for i in reversed(range(len(self.messages.messages))):
            if self.messages.messages[i].role == "user":
                user_idx = i
                break
        if user_idx is not None:
            # If next message is assistant, remove both
            if (
                user_idx + 1 < len(self.messages.messages)
                and self.messages.messages[user_idx + 1].role == "assistant"
            ):
                del self.messages.messages[user_idx : user_idx + 2]
                self.current_turn -= 1
                if self.history_index > 0:
                    self.history_index -= 1
                    self.history.restore_state_by_index(self.history_index)
            else:
                del self.messages.messages[user_idx : user_idx + 1]
                self.current_turn -= 1
                if self.history_index > 0:
                    self.history_index -= 1
                    self.history.restore_state_by_index(self.history_index)

        if self.is_silent:
            raw, styled = await self._process_message(last_msg, silent=True)
            return (
                raw,
                f"{preconversation_content}{styled}",
                "",
            )

        self.terminal.clear_screen()
        if is_retry:
            raw, styled = await self._process_message(last_msg, silent=False)
        else:
            new_input = await self.terminal.get_user_input(
                default_text=last_msg, add_newline=False
            )
            if not new_input:
                return "", intro_styled, ""
            self.terminal.clear_screen()
            raw, styled = await self._process_message(new_input, silent=False)
            last_msg = new_input

        self.prompt = self.terminal.format_prompt(last_msg)
        return raw, styled, self.prompt

    async def rewind_conversation(self, intro_styled: str) -> Tuple[str, str, str]:
        """
        Rewind the conversation by one exchange using content-based state resolution.
        This implementation decouples animation from state management and supports
        unlimited consecutive rewind operations.

        Process:
        1. Pre-flight: Extract animation data and validate rewind possibility
        2. Animation: Execute 3-phase animation using pre-extracted data
        3. State Restoration: Jump to content-identified target state
        4. Message Processing: Generate new response for target message
        """
        try:
            # PHASE 1: PRE-FLIGHT - Extract all data before any state changes
            target_user_msg = self.find_target_user_message()
            if not target_user_msg:
                self.logger.debug(
                    "Rewind failed: insufficient conversation history (need at least 2 user messages)"
                )
                return "", intro_styled, ""

            # Find the user message we're currently showing (for animation)
            current_user_msg = None
            for msg in reversed(self.messages.messages):
                if msg.role == "user":
                    current_user_msg = msg.content
                    break

            if not current_user_msg:
                self.logger.debug("Rewind failed: no current user message found")
                return "", intro_styled, ""

            # Find the target state before any animations
            target_state_result = self.find_state_before_user_message(target_user_msg)
            if not target_state_result:
                self.logger.debug(
                    f"Rewind failed: could not find state before user message: {target_user_msg[:50]}..."
                )
                return "", intro_styled, ""

            target_state_index, _ = target_state_result

            # Validate that target state is sane
            if target_state_index < 0 or target_state_index >= len(
                self.history.state_history
            ):
                self.logger.error(
                    f"Rewind failed: invalid target state index {target_state_index}"
                )
                return "", intro_styled, ""

            self.logger.debug(
                f"Rewind: current_user='{current_user_msg[:30]}...', target_user='{target_user_msg[:30]}...', target_state_index={target_state_index}"
            )

            # PHASE 2: ANIMATION - Execute 3-phase animation with pre-extracted data
            rev_streamer = self.animations.create_reverse_streamer()

            # Phase 2a: Standard reverse stream (removes assistant response + dots from user message)
            await rev_streamer.reverse_stream(
                intro_styled, "", preconversation_text=self.preface.styled_content
            )

            # Phase 2b: Fake reverse stream - remove current user message text word by word
            current_user_msg_without_dots = f"> {current_user_msg.rstrip('?.!')}"
            await rev_streamer.fake_reverse_stream_text(current_user_msg_without_dots)

            # Phase 2c: Fake forward stream - stream in the target message word by word
            await rev_streamer.fake_forward_stream_text(target_user_msg)

            # PHASE 3: STATE RESTORATION - Jump to content-identified target state
            restored_state = self.history.restore_state_by_index(target_state_index)
            if not restored_state:
                self.logger.error(
                    f"Rewind failed: could not restore state at index {target_state_index}"
                )
                return "", intro_styled, ""

            # Rebuild internal messages from restored history state
            self.messages.rebuild_from_state(restored_state.messages)

            # Update turn counter and history index to match restored state
            user_messages = [m for m in self.messages.messages if m.role == "user"]
            self.current_turn = len(user_messages)
            self.history_index = target_state_index

            self.logger.debug(
                f"Rewind: restored to state {target_state_index}, turn={self.current_turn}, messages={len(self.messages.messages)}"
            )

            # PHASE 4: MESSAGE PROCESSING - Generate new response for target message
            raw, styled = await self._process_message(target_user_msg, silent=False)

            self.prompt = self.terminal.format_prompt(target_user_msg)
            self.logger.debug("Rewind completed successfully")
            return raw, styled, self.prompt

        except Exception as e:
            self.logger.error(
                f"Rewind operation failed with exception: {e}", exc_info=True
            )
            # Return original state on error
            return "", intro_styled, ""

    def _read_line_raw_conclusion_mode(self) -> str:
        """
        Special raw input mode for conclusion state.
        No prompt, no cursor, no text input - only keyboard shortcuts.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            # Ensure cursor is hidden
            self.terminal.hide_cursor()

            # Switch to raw mode
            tty.setraw(fd, termios.TCSANOW)

            while True:
                c = os.read(fd, 1)

                # Only handle the allowed shortcuts
                if c == b"\x05":  # Ctrl+E
                    self.terminal.write("\r\n")
                    return "edit"
                elif c == b"\x12":  # Ctrl+R
                    self.terminal.write("\r\n")
                    return "retry"
                elif c == b"\x15":  # Ctrl+U
                    self.terminal.write("\r\n")
                    return "rewind"
                elif c == b"\x13":  # Ctrl+S
                    self.terminal.write("\r\n")
                    return "save"
                elif c == b"\x03":  # Ctrl+C
                    # In conclusion mode, Ctrl+C does nothing - just continue listening
                    pass
                elif c == b"\x04":  # Ctrl+D
                    self.terminal.write("\r\n")
                    raise KeyboardInterrupt()
                # Ignore all other input including Ctrl+P and regular characters

        finally:
            # Restore terminal settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            self.terminal.hide_cursor()

    async def _get_conclusion_mode_input(self) -> str:
        """Get input while in conclusion mode (no prompt, no cursor, only shortcuts)."""
        # Use the raw input method directly with hidden prompt
        result = await asyncio.get_event_loop().run_in_executor(
            None, self._read_line_raw_conclusion_mode
        )
        return result

    async def _async_conversation_loop(self, system_msg: str, intro_msg: str):
        """
        Main conversation loop:
         - Add system message (turn 0),
         - Process the first user message silently,
         - Then prompt for further input or let user edit.
        """
        try:
            # FIXED: Check if system message already exists before adding
            if system_msg:
                # Check if we already have a system message
                has_system = any(m.role == "system" for m in self.messages.messages)
                if not has_system:
                    self.messages.add_message("system", system_msg, 0)
                    sys_msgs = await self.messages.get_messages()
                    self.history.update_state(messages=sys_msgs)
                    self.history_index = self.history.get_latest_state_index()

            # Process the "intro" user message in silent mode
            _, intro_styled, _ = await self.introduce_conversation(intro_msg)

            # Now loop for interactive user input
            while True:
                if self.conclusion_triggered:
                    # Ensure cursor is hidden before entering conclusion mode
                    self.terminal.hide_cursor()
                    # Special handling for conclusion mode
                    user_input = await self._get_conclusion_mode_input()
                    if user_input in ["edit", "retry"]:
                        # Process backtracking
                        _, intro_styled, _ = await self.backtrack_conversation(
                            intro_styled, is_retry=(user_input == "retry")
                        )
                        self.conclusion_triggered = False  # Reset after edit/retry
                    elif user_input == "rewind":
                        # Process rewind
                        _, intro_styled, _ = await self.rewind_conversation(
                            intro_styled
                        )
                        self.conclusion_triggered = False  # Reset after rewind
                    elif user_input == "save":
                        # Process save
                        _, intro_styled, _ = await self._handle_save_command(
                            intro_styled
                        )
                else:
                    # Normal input handling - pass operations disable flag for first response
                    user_input = await self.terminal.get_user_input(
                        disable_operations=self.disable_first_operations
                    )
                    if not user_input:
                        continue

                    cmd = user_input.lower().strip()
                    if cmd in ["edit", "retry"]:
                        _, intro_styled, _ = await self.backtrack_conversation(
                            intro_styled, is_retry=(cmd == "retry")
                        )
                        # Reset flag after any retry/edit operation
                        self.disable_first_operations = False
                    elif cmd == "rewind":
                        _, intro_styled, _ = await self.rewind_conversation(
                            intro_styled
                        )
                        # Reset flag after rewind operation
                        self.disable_first_operations = False
                    elif cmd == "save":
                        _, intro_styled, _ = await self._handle_save_command(
                            intro_styled
                        )
                    else:
                        _, intro_styled, _ = await self.process_user_message(
                            user_input, intro_styled
                        )
                        # Reset flag after first user message is processed
                        self.disable_first_operations = False

        except Exception as e:
            self.logger.error(f"Critical error: {e}", exc_info=True)
            raise
        finally:
            await self.terminal.update_display()

    def start_conversation(self, messages: List[Dict[str, str]]) -> None:
        """
        Public entry from Interface.start(), with validated messages:
        - Possibly a system message at index 0
        - Multiple user/assistant pairs
        - Must end on user (unless empty)
        """
        try:
            # Reset local counters for a fresh start
            self.current_turn = 0
            self.history_index = -1

            # Handle the case of empty messages
            if not messages:
                # Just run the conversation loop with empty system and intro messages
                asyncio.run(self._async_conversation_loop("", ""))
                return

            # 1) Identify system_msg if present at messages[0]
            idx = 0
            system_msg = ""
            if messages[0]["role"] == "system":
                system_msg = messages[0]["content"]
                # CRITICAL FIX: Add system message immediately to self.messages
                self.messages.add_message("system", system_msg, 0)
                idx = 1

            # The final user message is always the last item
            final_user_msg = messages[-1]["content"]

            # 2) Insert all hidden pairs from messages[idx:-1]
            hidden_messages = messages[idx:-1]  # everything except the last user
            turn_count = 0

            i = 0
            while i < len(hidden_messages):
                if hidden_messages[i]["role"] == "user":
                    turn_count += 1
                    self.messages.add_message(
                        "user", hidden_messages[i]["content"], turn_count
                    )
                    i += 1
                    # If next is assistant, same turn_count
                    if (
                        i < len(hidden_messages)
                        and hidden_messages[i]["role"] == "assistant"
                    ):
                        self.messages.add_message(
                            "assistant", hidden_messages[i]["content"], turn_count
                        )
                        i += 1
                else:
                    # If for some reason the next message is "assistant" w/o a user,
                    # we can handle it or skip. But by prior validation, that shouldn't happen.
                    i += 1

            # Update our conversation state
            async def _update_history():
                sys_prompt = self._get_system_prompt()
                combined = await self.messages.get_messages(sys_prompt)
                self.history.update_state(messages=combined)
                self.history_index = self.history.get_latest_state_index()

            asyncio.run(_update_history())

            # 3) Run the normal async conversation loop with the final user message
            # CRITICAL FIX: Always pass empty string for system_msg to avoid duplication
            asyncio.run(self._async_conversation_loop("", final_user_msg))

        except KeyboardInterrupt:
            self.logger.info("User interrupted")
            self.terminal.reset()
        except Exception as e:
            self.logger.error(f"Critical error in conversation: {e}", exc_info=True)
            self.terminal.reset()

    async def _handle_save_command(self, intro_styled: str) -> Tuple[str, str, str]:
        """Handle the save command with smooth animation sequence."""
        try:
            # Store original conversation state for restoration
            original_user_message = self._get_last_user_input()

            if not original_user_message:
                # No conversation to save
                await self.terminal.update_display("No conversation to save.\n")
                return "", intro_styled, ""

            # Create reverse streamer for animations
            rev_streamer = self.animations.create_reverse_streamer()

            # Phase 1: Reverse stream the current conversation using the actual styled content
            await rev_streamer.reverse_stream(intro_styled, delay=0.05)

            # Phase 2: Clear screen and show save prompt
            self.terminal.clear_screen()
            filename = await self.terminal.get_user_input(
                default_text="",  # No prepopulated filename
                prompt_prefix="> Save As: ",  # Protected prompt prefix
                add_newline=False,  # Don't add extra spacing
                hide_cursor=True,  # Hide cursor after input
            )

            # Check if user cancelled (Ctrl+C returns empty string)
            if not filename.strip():
                # User cancelled - restore original conversation with streaming
                await rev_streamer.fake_forward_stream_styled_content(
                    intro_styled, delay=0.05
                )
                return "", intro_styled, ""

            # Phase 3: Perform the save operation (behind the scenes)
            clean_filename = self._clean_filename(filename.strip())
            conversation_data = self.history.create_state_snapshot()
            saved_path, save_error = self.save_manager.save_conversation(
                clean_filename, conversation_data
            )

            # Log the save result
            if saved_path:
                self.logger.info(f"Conversation saved to: {saved_path}")
            else:
                error_msg = (
                    f"Save failed: {save_error}"
                    if save_error
                    else "Save failed for unknown reason"
                )
                self.logger.error(error_msg)

            # Phase 4: Reverse stream the save prompt word by word
            full_save_prompt = f"> Save As: {filename.strip()}"
            await rev_streamer.fake_reverse_stream_text(full_save_prompt, delay=0.06)

            # Phase 5: Remove the final prompt symbol to get completely clean screen
            await rev_streamer.update_display("", "", force_full_clear=True)

            # Phase 6: Stream the original conversation back progressively
            await rev_streamer.fake_forward_stream_styled_content(
                intro_styled, delay=0.05
            )

            return "", intro_styled, ""

        except Exception as e:
            self.logger.error(f"Error handling save command: {e}", exc_info=True)
            # On error, restore the conversation with streaming
            rev_streamer = self.animations.create_reverse_streamer()
            await rev_streamer.fake_forward_stream_styled_content(
                intro_styled, delay=0.05
            )
            return "", intro_styled, ""

    async def _prompt_for_filename(self) -> Optional[str]:
        """
        Prompt the user for a filename using the terminal input system.

        Returns:
            Filename if provided, None if cancelled
        """
        try:
            # Generate default filename
            default_filename = self.save_manager.generate_default_filename()

            # Show the save prompt
            prompt_text = f"Save as: {default_filename}"
            await self.terminal.update_display(prompt_text)

            # Get user input using the existing terminal input system
            # We'll reuse the _read_line_raw method but with a custom prompt
            user_input = await self._get_filename_input(default_filename)

            if user_input is None:
                # User cancelled with Ctrl+C
                return None

            # Use the input if provided, otherwise use default
            filename = user_input.strip() if user_input.strip() else default_filename

            # Clean up the filename (remove any potentially problematic characters)
            filename = self._clean_filename(filename)

            return filename

        except Exception as e:
            self.logger.error(f"Error prompting for filename: {e}", exc_info=True)
            return None

    async def _get_filename_input(self, default_filename: str) -> Optional[str]:
        """
        Get filename input from the user with default pre-populated.

        Args:
            default_filename: The default filename to show

        Returns:
            User input or None if cancelled
        """
        try:
            # Use the existing terminal input system
            result = await asyncio.get_event_loop().run_in_executor(
                None, self._read_filename_raw, default_filename
            )
            return result
        except Exception as e:
            self.logger.error(f"Error getting filename input: {e}", exc_info=True)
            return None

    def _clean_filename(self, filename: str) -> str:
        """Clean the filename by removing or replacing problematic characters."""
        # Remove or replace characters that are problematic in filenames
        import re

        # Replace spaces with underscores
        filename = filename.replace(" ", "_")

        # Remove characters that are invalid in filenames
        filename = re.sub(r'[<>:"/\\|?*]', "", filename)

        # Ensure filename is not empty
        if not filename.strip():
            filename = self.save_manager.generate_default_filename()

        return filename

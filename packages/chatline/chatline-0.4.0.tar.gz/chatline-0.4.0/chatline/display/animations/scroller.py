# display/animations/scroller.py

import asyncio
from typing import List, Optional

class Scroller:
    """Animate text scrolling with wrapping and formatting."""
    def __init__(self, style, terminal):
        """Init scroller with style engine and terminal."""
        self.style = style
        self.terminal = terminal

    def _handle_text(self, text: str, width: Optional[int] = None) -> List[str]:
        """Wrap text into lines, handling box-drawing chars."""
        width = width or self.terminal.width
        
        # If box-drawing chars present, split by newline.
        if any(ch in text for ch in ('╭', '╮', '╯', '╰')):
            return text.split('\n')
            
        # Create a more accurate method to handle styled text wrapping
        # that's compatible with how the StyleEngine processes text
        result = []
        for para in text.split('\n'):
            if not para.strip():
                result.append('')
                continue
                
            # Process paragraph as a whole instead of word by word
            # This will better handle ANSI sequences that span words
            current_line = ''
            for word in para.split():
                test_line = f"{current_line}{' ' if current_line else ''}{word}"
                # Use the StyleEngine's method directly for consistent calculation
                if self.style._engine.get_visible_length(test_line) <= width:
                    current_line = test_line
                else:
                    if current_line:
                        result.append(current_line)
                    current_line = word
                    
            if current_line:
                result.append(current_line)
                
        return result

    async def _update_scroll_display(self, lines: List[str], prompt: str) -> None:
        """Clear screen and display lines with a prompt."""
        self.terminal.clear_screen()
        # Write each line.
        for line in lines:
            self.terminal.write(line, newline=True)
        # Write prompt with reset formatting.
        self.terminal.write(self.style.get_format('RESET'))
        self.terminal.write(prompt)

    async def scroll_up(self, styled_lines: str, prompt: str, delay: float = 0.5) -> None:
        """Scroll pre-styled text upward with a prompt and delay."""
        # Strip leading newlines to prevent extra blank line at top
        styled_lines = styled_lines.lstrip('\n')
        # Capture terminal width at the start of scrolling
        # to ensure consistent width throughout the operation
        current_width = self.terminal.width
        lines = self._handle_text(styled_lines, width=current_width)
        
        # Limit lines to what can fit on screen to prevent duplication
        max_lines = self.terminal.height - 1  # Reserve one line for prompt
        if len(lines) > max_lines:
            # Show only the last portion that fits on screen
            lines = lines[-max_lines:]
        
        for i in range(len(lines) + 1):
            self.terminal.clear_screen_smart()
            # Write remaining lines that fit on screen
            remaining_lines = lines[i:]
            if len(remaining_lines) > max_lines:
                remaining_lines = remaining_lines[-max_lines:]
            for ln in remaining_lines:
                self.terminal.write(ln, newline=True)
            # Write prompt with reset formatting.
            self.terminal.write(self.style.get_format('RESET') + prompt)
            await asyncio.sleep(delay)
# conversation/messages.py

from dataclasses import dataclass

@dataclass
class Message:
    """A conversation message."""
    role: str
    content: str
    turn_number: int = 0

class ConversationMessages:
    """Handles conversation messages."""
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, role: str, content: str, turn_number: int) -> None:
        """Add a message to the history."""
        self.messages.append(Message(role, content, turn_number))

    async def get_messages(self, system_prompt: str = None) -> list[dict]:
        """Return messages as dicts; prepend system prompt if provided and not already present."""
        base_messages = [{"role": m.role, "content": m.content} for m in self.messages]
        
        # Check if we already have a system message at the start
        has_system = base_messages and base_messages[0]["role"] == "system"
        
        # If system_prompt is provided and we don't have a system message yet, add it
        if system_prompt and not has_system:
            return [{"role": "system", "content": system_prompt}] + base_messages
        return base_messages

    def remove_last_n_messages(self, n: int) -> None:
        """Remove the last n messages."""
        self.messages = self.messages[:-n] if n <= len(self.messages) else []

    def rebuild_from_state(self, state_messages: list[dict]) -> None:
        """Rebuild internal messages from history state messages."""
        self.messages.clear()
        
        # Rebuild messages with turn numbers
        current_turn = 0
        for msg_dict in state_messages:
            role = msg_dict["role"]
            content = msg_dict["content"]
            
            # System message is turn 0, user messages increment turn
            if role == "system":
                turn_number = 0
            elif role == "user":
                current_turn += 1
                turn_number = current_turn
            else:  # assistant
                turn_number = current_turn
            
            self.messages.append(Message(role, content, turn_number))
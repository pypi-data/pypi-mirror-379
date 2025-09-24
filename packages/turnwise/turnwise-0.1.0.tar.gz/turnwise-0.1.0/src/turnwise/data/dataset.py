"""Dataset management for Turnwise evaluation library."""

from collections.abc import Iterator
from typing import Any

from .types import Conversation, Role, Turn


class ConversationDataset:
    """A collection of conversations for evaluation."""

    def __init__(self, data=None):
        """Initialize the dataset.

        Args:
            data: Optional data to create dataset from. Can be:
                - List of Conversation objects
                - List of dictionaries (conversation data)
                - List of tuples (role, content) pairs
                - None for empty dataset
        """
        if data is None:
            self.conversations = []
        elif isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], Conversation):
                # List of Conversation objects
                self.conversations = data
            elif isinstance(data[0], dict):
                # List of dictionaries
                self.conversations = [
                    self._from_dicts(conv["turns"], conv.get("metadata"))
                    for conv in data
                ]
            elif isinstance(data[0], (tuple, list)) and len(data[0]) == 2:
                # List of (role, content) tuples
                self.conversations = [self._from_strings(data)]
            else:
                raise ValueError("Unsupported data format")
        else:
            self.conversations = []

    def add(self, data) -> None:
        """Add conversation(s) to the dataset.

        Args:
            data: Can be:
                - Single Conversation object
                - List of Conversation objects
                - List of dictionaries (conversation data)
                - List of tuples (role, content) pairs
        """
        if isinstance(data, Conversation):
            # Single conversation
            self.conversations.append(data)
        elif isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], Conversation):
                # List of Conversation objects
                self.conversations.extend(data)
            elif isinstance(data[0], dict):
                # List of dictionaries
                conversations = [
                    self._from_dicts(conv["turns"], conv.get("metadata"))
                    for conv in data
                ]
                self.conversations.extend(conversations)
            elif isinstance(data[0], (tuple, list)) and len(data[0]) == 2:
                # List of (role, content) tuples
                conversation = self._from_strings(data)
                self.conversations.append(conversation)
            else:
                raise ValueError("Unsupported data format")
        else:
            raise ValueError("Unsupported data format")

    def __len__(self) -> int:
        """Return the number of conversations in the dataset."""
        return len(self.conversations)

    def __iter__(self) -> Iterator[Conversation]:
        """Iterate over conversations in the dataset."""
        return iter(self.conversations)

    def __getitem__(self, index: int) -> Conversation:
        """Get a conversation by index."""
        return self.conversations[index]

    def filter_length(
        self, min_turns: int = 1, max_turns: int | None = None
    ) -> "ConversationDataset":
        """Filter conversations by number of turns.

        Args:
            min_turns: Minimum number of turns required
            max_turns: Maximum number of turns allowed (None for no limit)

        Returns:
            New ConversationDataset with filtered conversations
        """
        filtered = []
        for conv in self.conversations:
            num_turns = len(conv.turns)
            if num_turns >= min_turns and (max_turns is None or num_turns <= max_turns):
                filtered.append(conv)

        return ConversationDataset(filtered)

    def filter_ratio(
        self, min_user_ratio: float = 0.0, max_user_ratio: float = 1.0
    ) -> "ConversationDataset":
        """Filter conversations by user turn ratio.

        Args:
            min_user_ratio: Minimum ratio of user turns to total turns
            max_user_ratio: Maximum ratio of user turns to total turns

        Returns:
            New ConversationDataset with filtered conversations
        """
        filtered = []
        for conv in self.conversations:
            total_turns = len(conv.turns)
            user_turns = len(conv.user_turns)
            user_ratio = user_turns / total_turns if total_turns > 0 else 0.0

            if min_user_ratio <= user_ratio <= max_user_ratio:
                filtered.append(conv)

        return ConversationDataset(filtered)

    def stats(self) -> dict[str, Any]:
        """Get statistics about the dataset.

        Returns:
            Dictionary containing dataset statistics
        """
        if not self.conversations:
            return {"total_conversations": 0}

        total_conversations = len(self.conversations)
        total_turns = sum(len(conv.turns) for conv in self.conversations)

        turn_counts = [len(conv.turns) for conv in self.conversations]
        user_turn_counts = [len(conv.user_turns) for conv in self.conversations]
        assistant_turn_counts = [
            len(conv.assistant_turns) for conv in self.conversations
        ]

        return {
            "total_conversations": total_conversations,
            "total_turns": total_turns,
            "average_turns_per_conversation": total_turns / total_conversations,
            "min_turns": min(turn_counts),
            "max_turns": max(turn_counts),
            "average_user_turns": sum(user_turn_counts) / total_conversations,
            "average_assistant_turns": sum(assistant_turn_counts) / total_conversations,
            "conversations_with_metadata": sum(
                1 for conv in self.conversations if conv.metadata
            ),
            "conversations_with_expected_output": sum(
                1 for conv in self.conversations if conv.expected_output
            ),
        }

    def _from_strings(
        self, turns: list[tuple[str, str]], metadata: dict[str, Any] | None = None
    ) -> Conversation:
        """Create a Conversation from a list of (role, content) tuples."""
        conversation_turns = []

        for role_str, content in turns:
            try:
                role = Role(role_str.lower())
            except ValueError:
                raise ValueError(
                    f"Invalid role '{role_str}'. Must be 'user', 'assistant', or 'system'"
                )

            turn = Turn(role=role, content=content)
            conversation_turns.append(turn)

        return Conversation(turns=conversation_turns, metadata=metadata)

    def _from_dicts(
        self, turns: list[dict[str, str]], metadata: dict[str, Any] | None = None
    ) -> Conversation:
        """Create a Conversation from a list of dictionaries."""
        turn_tuples = []

        for turn_dict in turns:
            if "role" not in turn_dict or "content" not in turn_dict:
                raise ValueError(
                    "Each turn dictionary must have 'role' and 'content' keys"
                )

            turn_tuples.append((turn_dict["role"], turn_dict["content"]))

        return self._from_strings(turn_tuples, metadata)

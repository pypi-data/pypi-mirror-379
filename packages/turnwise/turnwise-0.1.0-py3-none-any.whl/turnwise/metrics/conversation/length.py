"""Conversation length metric."""

from ...data.types import Conversation, EvaluationResult
from ..base import Metric


class ConversationLengthMetric(Metric):
    """Evaluates if conversation has appropriate length."""

    def __init__(
        self, min_turns: int = 1, max_turns: int = 100, threshold: float = 0.5
    ):
        """Initialize the conversation length metric.

        Args:
            min_turns: Minimum number of turns required
            max_turns: Maximum number of turns allowed
            threshold: Minimum score to pass
        """
        super().__init__("conversation_length", threshold)
        self.min_turns = min_turns
        self.max_turns = max_turns

    def evaluate(self, conversation: Conversation) -> EvaluationResult:
        """Evaluate conversation length."""
        num_turns = len(conversation.turns)

        if num_turns < self.min_turns:
            score = 0.0
            details = {
                "actual_turns": num_turns,
                "min_required": self.min_turns,
                "max_allowed": self.max_turns,
                "reason": "too_short",
            }
        elif num_turns > self.max_turns:
            score = 0.0
            details = {
                "actual_turns": num_turns,
                "min_required": self.min_turns,
                "max_allowed": self.max_turns,
                "reason": "too_long",
            }
        else:
            score = 1.0
            details = {
                "actual_turns": num_turns,
                "min_required": self.min_turns,
                "max_allowed": self.max_turns,
                "reason": "appropriate_length",
            }

        return self._create_result(score, details)

"""Core data types for Turnwise evaluation library."""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class Role(Enum):
    """Represents the role of a speaker in a conversation turn."""

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass
class Turn:
    """A single turn in a conversation."""

    role: Role
    content: str
    metadata: dict[str, Any] | None = None

    def __post_init__(self):
        """Validate turn data after initialization."""
        if not self.content.strip():
            raise ValueError("Turn content cannot be empty")


@dataclass
class Conversation:
    """A multi-turn conversation for evaluation."""

    turns: list[Turn]
    metadata: dict[str, Any] | None = None
    expected_output: str | None = None

    def __post_init__(self):
        """Validate conversation data after initialization."""
        if not self.turns:
            raise ValueError("Conversation must have at least one turn")

        # Ensure conversation starts with user or system
        if self.turns[0].role not in [Role.USER, Role.SYSTEM]:
            raise ValueError("Conversation must start with user or system turn")

    @property
    def user_turns(self) -> list[Turn]:
        """Get all user turns in the conversation."""
        return [turn for turn in self.turns if turn.role == Role.USER]

    @property
    def assistant_turns(self) -> list[Turn]:
        """Get all assistant turns in the conversation."""
        return [turn for turn in self.turns if turn.role == Role.ASSISTANT]

    @property
    def last_assistant_turn(self) -> Turn | None:
        """Get the last assistant turn in the conversation."""
        assistant_turns = self.assistant_turns
        return assistant_turns[-1] if assistant_turns else None

    def to_string(self) -> str:
        """Convert conversation to a readable string format."""
        lines = []
        for turn in self.turns:
            lines.append(f"{turn.role.value}: {turn.content}")
        return "\n".join(lines)


@dataclass
class EvaluationResult:
    """Result of evaluating a conversation against a metric."""

    metric_name: str
    score: float
    passed: bool
    details: dict[str, Any] | None = None
    error: str | None = None


@dataclass
class EvaluationReport:
    """Complete evaluation report for a conversation."""

    conversation: Conversation
    results: list[EvaluationResult]
    overall_score: float
    passed: bool
    metadata: dict[str, Any] | None = None

    @property
    def failed_metrics(self) -> list[EvaluationResult]:
        """Get all failed metric results."""
        return [result for result in self.results if not result.passed]

    @property
    def passed_metrics(self) -> list[EvaluationResult]:
        """Get all passed metric results."""
        return [result for result in self.results if result.passed]

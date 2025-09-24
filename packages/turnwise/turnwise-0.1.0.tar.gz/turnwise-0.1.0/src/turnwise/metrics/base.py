"""Base metric classes for Turnwise."""

from abc import ABC, abstractmethod
from typing import Any

from ..data.types import Conversation, EvaluationResult


class Metric(ABC):
    """Base class for all evaluation metrics."""

    def __init__(self, name: str, threshold: float = 0.5):
        """Initialize the metric.

        Args:
            name: Human-readable name of the metric
            threshold: Minimum score to pass the metric (0.0 to 1.0)
        """
        self.name = name
        self.threshold = threshold
        if not 0.0 <= threshold <= 1.0:
            raise ValueError("Threshold must be between 0.0 and 1.0")

    @abstractmethod
    def evaluate(self, conversation: Conversation) -> EvaluationResult:
        """Evaluate a conversation against this metric.

        Args:
            conversation: The conversation to evaluate

        Returns:
            EvaluationResult with score, pass/fail status, and details
        """
        pass

    def _create_result(
        self,
        score: float,
        details: dict[str, Any] | None = None,
        error: str | None = None,
    ) -> EvaluationResult:
        """Helper method to create an EvaluationResult."""
        return EvaluationResult(
            metric_name=self.name,
            score=score,
            passed=score >= self.threshold,
            details=details,
            error=error,
        )

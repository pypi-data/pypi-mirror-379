"""Turnwise: A modern Python library for evaluating multi-turn chatbot conversations."""

# Core types
# CLI
from .cli import cli

# Configuration
from .config import EvaluationConfig, config

# Core evaluation engine
from .core import Evaluator

# Dataset management
from .data.dataset import ConversationDataset
from .data.types import Conversation, EvaluationReport, EvaluationResult, Role, Turn

# Evaluation functions
from .evaluate import create_summary_report

# Metrics
from .metrics.base import Metric
from .metrics.conversation import ConversationCoherenceMetric, ConversationLengthMetric
from .metrics.llm import (
    ConversationQualityMetric,
    ResponseHelpfulnessMetric,
    ResponseSafetyMetric,
)
from .metrics.relevance import ResponseRelevanceMetric

__version__ = "0.1.0"

__all__ = [
    # Core types
    "Turn",
    "Conversation",
    "Role",
    "EvaluationResult",
    "EvaluationReport",
    # Metrics
    "Metric",
    "ConversationLengthMetric",
    "ResponseRelevanceMetric",
    "ConversationCoherenceMetric",
    "ConversationQualityMetric",
    "ResponseHelpfulnessMetric",
    "ResponseSafetyMetric",
    # Evaluation functions
    "create_summary_report",
    # Dataset management
    "ConversationDataset",
    # Core engine
    "Evaluator",
    # Configuration
    "config",
    "EvaluationConfig",
    # CLI
    "cli",
]

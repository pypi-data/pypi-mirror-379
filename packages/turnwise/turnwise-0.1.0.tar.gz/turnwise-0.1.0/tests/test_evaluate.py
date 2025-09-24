"""Tests for evaluation functions."""

import pytest

from turnwise import (
    Conversation,
    ConversationLengthMetric,
    Evaluator,
    Metric,
    Role,
    Turn,
    create_summary_report,
)


class TestEvaluate:
    """Test evaluate function."""

    def test_evaluate_single_conversation(self):
        """Test evaluating a single conversation."""
        turns = [
            Turn(role=Role.USER, content="Hello"),
            Turn(role=Role.ASSISTANT, content="Hi there!"),
        ]
        conv = Conversation(turns=turns)
        metrics = [ConversationLengthMetric()]

        evaluator = Evaluator(metrics=metrics)
        report = evaluator.run(conv)

        assert report.conversation == conv
        assert len(report.results) == 1
        assert report.overall_score >= 0.0
        assert report.overall_score <= 1.0
        assert isinstance(report.passed, bool)

    def test_evaluate_with_metadata(self):
        """Test evaluating with metadata."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)
        metrics = [ConversationLengthMetric()]
        metadata = {"session_id": "123"}

        evaluator = Evaluator(metrics=metrics)
        report = evaluator.run(conv, metadata)

        assert report.metadata == metadata

    def test_evaluate_no_metrics_raises_error(self):
        """Test that empty metrics list raises error."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)

        evaluator = Evaluator(metrics=[])
        with pytest.raises(ValueError, match="No metrics configured"):
            evaluator.run(conv)

    def test_evaluate_metric_error_handling(self):
        """Test handling of metric evaluation errors."""
        turns = [Turn(role=Role.USER, content="Hello")]
        conv = Conversation(turns=turns)

        # Create a metric that will raise an error
        class ErrorMetric(Metric):
            def __init__(self):
                super().__init__("error_metric", 0.5)

            def evaluate(self, conversation):
                raise Exception("Test error")

        evaluator = Evaluator(metrics=[ErrorMetric()])
        report = evaluator.run(conv)

        assert len(report.results) == 1
        assert report.results[0].error == "Test error"
        assert report.results[0].passed is False
        assert report.results[0].score == 0.0


class TestEvaluateBatch:
    """Test evaluate_batch function."""

    def test_evaluate_multiple_conversations(self):
        """Test evaluating multiple conversations."""
        conv1 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi!"),
            ]
        )
        conv2 = Conversation(
            turns=[
                Turn(role=Role.USER, content="How are you?"),
                Turn(role=Role.ASSISTANT, content="I'm good!"),
            ]
        )

        conversations = [conv1, conv2]
        metrics = [ConversationLengthMetric()]

        evaluator = Evaluator(metrics=metrics)
        reports = evaluator.batch(conversations)

        assert len(reports) == 2
        assert all(isinstance(report, type(reports[0])) for report in reports)
        assert reports[0].metadata["conversation_index"] == 0
        assert reports[1].metadata["conversation_index"] == 1

    def test_evaluate_batch_empty_conversations_raises_error(self):
        """Test that empty conversations list raises error."""
        evaluator = Evaluator(metrics=[ConversationLengthMetric()])
        with pytest.raises(
            ValueError, match="At least one conversation must be provided"
        ):
            evaluator.batch([])

    def test_evaluate_batch_no_metrics_raises_error(self):
        """Test that empty metrics list raises error."""
        conv = Conversation(turns=[Turn(role=Role.USER, content="Hello")])

        evaluator = Evaluator(metrics=[])
        with pytest.raises(ValueError, match="No metrics configured"):
            evaluator.batch([conv])


class TestCreateSummaryReport:
    """Test create_summary_report function."""

    def test_create_summary_report(self):
        """Test creating a summary report."""
        # Create test conversations and reports
        conv1 = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi!"),
            ]
        )
        conv2 = Conversation(
            turns=[
                Turn(role=Role.USER, content="How are you?"),
                Turn(role=Role.ASSISTANT, content="I'm good!"),
            ]
        )

        metrics = [ConversationLengthMetric()]
        evaluator = Evaluator(metrics=metrics)
        reports = evaluator.batch([conv1, conv2])

        summary = create_summary_report(reports)

        assert summary["total_conversations"] == 2
        assert summary["passed_conversations"] >= 0
        assert summary["overall_pass_rate"] >= 0.0
        assert summary["overall_pass_rate"] <= 1.0
        assert "metric_statistics" in summary
        assert len(summary["metric_statistics"]) == 1

    def test_create_summary_report_empty_list(self):
        """Test creating summary report with empty list."""
        summary = create_summary_report([])
        assert "error" in summary
        assert summary["error"] == "No reports provided"

    def test_summary_report_metric_statistics(self):
        """Test that metric statistics are calculated correctly."""
        conv = Conversation(
            turns=[
                Turn(role=Role.USER, content="Hello"),
                Turn(role=Role.ASSISTANT, content="Hi!"),
            ]
        )

        metrics = [ConversationLengthMetric()]
        evaluator = Evaluator(metrics=metrics)
        reports = evaluator.batch([conv])
        summary = create_summary_report(reports)

        metric_stats = summary["metric_statistics"]
        assert "conversation_length" in metric_stats

        length_stats = metric_stats["conversation_length"]
        assert length_stats["total_evaluations"] == 1
        assert length_stats["passed_evaluations"] >= 0
        assert length_stats["pass_rate"] >= 0.0
        assert length_stats["pass_rate"] <= 1.0
        assert length_stats["average_score"] >= 0.0
        assert length_stats["average_score"] <= 1.0
        assert length_stats["error_count"] == 0

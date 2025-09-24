"""Core evaluation engine."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

from dotenv import load_dotenv

from ..data.types import Conversation, EvaluationReport, EvaluationResult
from ..metrics.base import Metric

# Load environment variables from .env file
load_dotenv()


class Evaluator:
    """Core evaluation engine for Turnwise."""

    def __init__(
        self,
        metrics: list[Metric | type[Metric]] | None = None,
        max_workers: int = 4,
        openai_api_key: str | None = None,
        anthropic_api_key: str | None = None
    ):
        """Initialize the evaluator.

        Args:
            metrics: List of metrics to use for evaluation (instances or classes)
            max_workers: Maximum number of worker threads for parallel evaluation
            openai_api_key: OpenAI API key for LLM-based metrics
            anthropic_api_key: Anthropic API key for LLM-based metrics
        """
        self.metrics = self._resolve_metrics(metrics or [])
        self.max_workers = max_workers
        self.openai_api_key = openai_api_key
        self.anthropic_api_key = anthropic_api_key

    def run(
        self,
        conversation: Conversation,
        metadata: dict[str, Any] | None = None,
        parallel: bool = True,
    ) -> EvaluationReport:
        """Evaluate a conversation against configured metrics.

        Args:
            conversation: The conversation to evaluate
            metadata: Optional metadata for the report
            parallel: Whether to run metrics in parallel

        Returns:
            EvaluationReport with results
        """
        if not self.metrics:
            raise ValueError("No metrics configured. Provide metrics in constructor.")

        # Run evaluation
        if parallel and len(self.metrics) > 1:
            results = self._evaluate_parallel(conversation, self.metrics)
        else:
            results = self._evaluate_sequential(conversation, self.metrics)

        # Calculate overall score
        valid_scores = [r.score for r in results if r.error is None]
        overall_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0.0

        # Determine if all metrics passed
        passed = all(result.passed for result in results)

        return EvaluationReport(
            conversation=conversation,
            results=results,
            overall_score=overall_score,
            passed=passed,
            metadata=metadata,
        )

    def batch(
        self,
        conversations: list[Conversation],
        metadata: dict[str, Any] | None = None,
        parallel: bool = True,
    ) -> list[EvaluationReport]:
        """Evaluate multiple conversations against configured metrics.

        Args:
            conversations: List of conversations to evaluate
            metadata: Optional metadata for reports
            parallel: Whether to run evaluations in parallel

        Returns:
            List of EvaluationReport objects
        """
        if not conversations:
            raise ValueError("At least one conversation must be provided")

        if not self.metrics:
            raise ValueError("No metrics configured. Provide metrics in constructor.")

        if parallel and len(conversations) > 1:
            return self._batch_parallel(conversations, metadata)
        else:
            return self._batch_sequential(conversations, metadata)

    def _resolve_metrics(self, metrics: list[Metric | type[Metric]]) -> list[Metric]:
        """Resolve metric classes to instances."""
        resolved = []

        for metric in metrics:
            if isinstance(metric, type) and issubclass(metric, Metric):
                # Create instance from class with API keys if needed
                metric_instance = self._create_metric_instance(metric)
                resolved.append(metric_instance)
            elif isinstance(metric, Metric):
                # Already an instance
                resolved.append(metric)
            else:
                raise ValueError(
                    f"Invalid metric type: {type(metric)}. Expected Metric class or instance."
                )

        return resolved

    def _create_metric_instance(self, metric_class: type[Metric]) -> Metric:
        """Create a metric instance with appropriate API keys."""
        # Check if this is an LLM-based metric that needs API keys
        metric_name = metric_class.__name__.lower()

        if 'openai' in metric_name or any(name in metric_name for name in ['helpfulness', 'quality', 'safety']):
            # This is likely an OpenAI-based metric
            if self.openai_api_key:
                return metric_class(api_key=self.openai_api_key)
            else:
                return metric_class()  # Will use environment variable
        elif 'anthropic' in metric_name:
            # This is an Anthropic-based metric
            if self.anthropic_api_key:
                return metric_class(api_key=self.anthropic_api_key)
            else:
                return metric_class()  # Will use environment variable
        else:
            # Regular metric, no API key needed
            return metric_class()

    def _evaluate_sequential(
        self, conversation: Conversation, metrics: list[Metric]
    ) -> list[EvaluationResult]:
        """Evaluate metrics sequentially."""
        results = []

        for metric in metrics:
            try:
                result = metric.evaluate(conversation)
                results.append(result)
            except Exception as e:
                error_result = EvaluationResult(
                    metric_name=metric.name, score=0.0, passed=False, error=str(e)
                )
                results.append(error_result)

        return results

    def _evaluate_parallel(
        self, conversation: Conversation, metrics: list[Metric]
    ) -> list[EvaluationResult]:
        """Evaluate metrics in parallel."""
        results = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all metric evaluations
            future_to_metric = {
                executor.submit(metric.evaluate, conversation): metric
                for metric in metrics
            }

            # Collect results as they complete
            for future in as_completed(future_to_metric):
                metric = future_to_metric[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    error_result = EvaluationResult(
                        metric_name=metric.name, score=0.0, passed=False, error=str(e)
                    )
                    results.append(error_result)

        # Sort results to maintain order
        metric_names = [m.name for m in metrics]
        results.sort(key=lambda r: metric_names.index(r.metric_name))

        return results

    def _batch_sequential(
        self,
        conversations: list[Conversation],
        metadata: dict[str, Any] | None,
    ) -> list[EvaluationReport]:
        """Evaluate conversations sequentially."""
        reports = []

        for i, conversation in enumerate(conversations):
            conv_metadata = metadata.copy() if metadata else {}
            conv_metadata["conversation_index"] = i

            report = self.run(conversation, conv_metadata, parallel=False)
            reports.append(report)

        return reports

    def _batch_parallel(
        self,
        conversations: list[Conversation],
        metadata: dict[str, Any] | None,
    ) -> list[EvaluationReport]:
        """Evaluate conversations in parallel."""
        reports = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all conversation evaluations
            future_to_index = {}
            for i, conv in enumerate(conversations):
                conv_metadata = metadata.copy() if metadata else {}
                conv_metadata["conversation_index"] = i
                future = executor.submit(self.run, conv, conv_metadata, False)
                future_to_index[future] = i

            # Collect results as they complete
            results_dict = {}
            for future in as_completed(future_to_index):
                index = future_to_index[future]
                try:
                    report = future.result()
                    results_dict[index] = report
                except Exception as e:
                    # Create error report
                    error_report = EvaluationReport(
                        conversation=conversations[index],
                        results=[],
                        overall_score=0.0,
                        passed=False,
                        metadata={"error": str(e), "conversation_index": index},
                    )
                    results_dict[index] = error_report

            # Sort results by index
            reports = [results_dict[i] for i in sorted(results_dict.keys())]

        return reports

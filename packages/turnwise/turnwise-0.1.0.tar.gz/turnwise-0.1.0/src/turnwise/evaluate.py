"""Main evaluation functions for Turnwise."""

from typing import Any

from .data.types import EvaluationReport


def create_summary_report(reports: list[EvaluationReport]) -> dict[str, Any]:
    """Create a summary report from multiple evaluation reports.

    Args:
        reports: List of evaluation reports to summarize

    Returns:
        Dictionary containing summary statistics
    """
    if not reports:
        return {"error": "No reports provided"}

    total_conversations = len(reports)
    passed_conversations = sum(1 for r in reports if r.passed)

    # Collect all metric results
    all_metric_results = {}
    for report in reports:
        for result in report.results:
            metric_name = result.metric_name
            if metric_name not in all_metric_results:
                all_metric_results[metric_name] = []
            all_metric_results[metric_name].append(result)

    # Calculate per-metric statistics
    metric_stats = {}
    for metric_name, results in all_metric_results.items():
        valid_scores = [r.score for r in results if r.error is None]
        passed_count = sum(1 for r in results if r.passed)

        metric_stats[metric_name] = {
            "total_evaluations": len(results),
            "passed_evaluations": passed_count,
            "pass_rate": passed_count / len(results) if results else 0.0,
            "average_score": sum(valid_scores) / len(valid_scores)
            if valid_scores
            else 0.0,
            "min_score": min(valid_scores) if valid_scores else 0.0,
            "max_score": max(valid_scores) if valid_scores else 0.0,
            "error_count": sum(1 for r in results if r.error is not None),
        }

    # Calculate overall statistics
    all_scores = [r.overall_score for r in reports]

    summary = {
        "total_conversations": total_conversations,
        "passed_conversations": passed_conversations,
        "overall_pass_rate": passed_conversations / total_conversations,
        "average_overall_score": sum(all_scores) / len(all_scores),
        "min_overall_score": min(all_scores),
        "max_overall_score": max(all_scores),
        "metric_statistics": metric_stats,
    }

    return summary

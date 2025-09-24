"""CLI commands for Turnwise."""

import json
import sys

import click

from ..core.evaluator import Evaluator
from ..data.dataset import ConversationDataset
from ..metrics import (
    ConversationCoherenceMetric,
    ConversationLengthMetric,
    ConversationQualityMetric,
    ResponseHelpfulnessMetric,
    ResponseRelevanceMetric,
    ResponseSafetyMetric,
)
from ..utils.logging import get_logger

logger = get_logger(__name__)


@click.command()
@click.argument("conversation_file", type=click.Path(exists=True))
@click.option("--metrics", "-m", multiple=True, help="Metrics to use for evaluation")
@click.option("--output", "-o", type=click.Path(), help="Output file for results")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["json", "text"]),
    default="text",
    help="Output format",
)
@click.option("--parallel/--no-parallel", default=True, help="Run metrics in parallel")
@click.option("--workers", "-w", default=4, help="Number of worker threads")
@click.pass_context
def evaluate(ctx, conversation_file, metrics, output, output_format, parallel, workers):
    """Evaluate a conversation from a JSON file."""
    try:
        # Load conversation from file
        with open(conversation_file) as f:
            data = json.load(f)

        # Create conversation object
        if isinstance(data, list):
            conversations = ConversationDataset(data).conversations
        else:
            conversations = ConversationDataset([data]).conversations

        # Set up evaluator
        evaluator = Evaluator(max_workers=workers)

        # Set up metrics
        metric_list = _get_metrics(metrics)

        # Evaluate
        if len(conversations) == 1:
            report = evaluator.run(
                conversations[0], metric_list, parallel=parallel
            )
            results = [report]
        else:
            results = evaluator.batch(
                conversations, metric_list, parallel=parallel
            )

        # Output results
        if output_format == "json":
            output_data = _format_results_json(results)
        else:
            output_data = _format_results_text(results)

        if output:
            with open(output, "w") as f:
                f.write(output_data)
            click.echo(f"Results saved to {output}")
        else:
            click.echo(output_data)

    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        if ctx.obj.get("verbose"):
            raise
        sys.exit(1)


@click.command()
@click.argument("conversation_file", type=click.Path(exists=True))
@click.option("--metrics", "-m", multiple=True, help="Metrics to use for evaluation")
@click.option("--output", "-o", type=click.Path(), help="Output file for summary")
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["json", "text"]),
    default="text",
    help="Output format",
)
@click.option(
    "--parallel/--no-parallel", default=True, help="Run evaluations in parallel"
)
@click.option("--workers", "-w", default=4, help="Number of worker threads")
@click.pass_context
def batch_evaluate(
    ctx, conversation_file, metrics, output, output_format, parallel, workers
):
    """Evaluate multiple conversations and create a summary report."""
    try:
        # Load conversations from file
        with open(conversation_file) as f:
            data = json.load(f)

        if not isinstance(data, list):
            click.echo(
                "Error: File must contain a list of conversations for batch evaluation",
                err=True,
            )
            sys.exit(1)

        conversations = ConversationDataset(data).conversations

        # Set up evaluator
        evaluator = Evaluator(max_workers=workers)

        # Set up metrics
        metric_list = _get_metrics(metrics)

        # Evaluate
        results = evaluator.batch(
            conversations, metric_list, parallel=parallel
        )

        # Create summary
        from ..evaluate import create_summary_report

        summary = create_summary_report(results)

        # Output results
        if output_format == "json":
            output_data = json.dumps(summary, indent=2)
        else:
            output_data = _format_summary_text(summary)

        if output:
            with open(output, "w") as f:
                f.write(output_data)
            click.echo(f"Summary saved to {output}")
        else:
            click.echo(output_data)

    except Exception as e:
        logger.error(f"Batch evaluation failed: {e}")
        if ctx.obj.get("verbose"):
            raise
        sys.exit(1)


@click.command()
def list_metrics():
    """List available metrics."""
    metric_map = {
        "length": ConversationLengthMetric,
        "relevance": ResponseRelevanceMetric,
        "coherence": ConversationCoherenceMetric,
        "quality": ConversationQualityMetric,
        "helpfulness": ResponseHelpfulnessMetric,
        "safety": ResponseSafetyMetric,
    }

    click.echo("Available Metrics:")
    click.echo("=" * 50)

    for name, metric_class in metric_map.items():
        click.echo(f"• {name}")
        if hasattr(metric_class, "__doc__") and metric_class.__doc__:
            doc = metric_class.__doc__.strip().split("\n")[0]
            click.echo(f"  {doc}")

    click.echo("\nFull Names (also supported):")
    click.echo("-" * 30)
    click.echo("• conversation_length")
    click.echo("• response_relevance")
    click.echo("• conversation_coherence")
    click.echo("• conversation_quality")
    click.echo("• response_helpfulness")
    click.echo("• response_safety")


@click.command()
@click.option("--show", is_flag=True, help="Show current configuration")
@click.option(
    "--set",
    "set_config",
    nargs=2,
    multiple=True,
    help="Set configuration value (key value)",
)
def config_cmd(show, set_config):
    """Manage Turnwise configuration."""
    from ..config import config

    if show:
        click.echo("Current Configuration:")
        click.echo("=" * 30)
        for key, value in config.to_dict().items():
            click.echo(f"{key}: {value}")

    if set_config:
        for key, value in set_config:
            if hasattr(config, key):
                # Convert value to appropriate type
                current_value = getattr(config, key)
                if isinstance(current_value, bool):
                    setattr(config, key, value.lower() in ("true", "1", "yes", "on"))
                elif isinstance(current_value, int):
                    setattr(config, key, int(value))
                else:
                    setattr(config, key, value)
                click.echo(f"Set {key} = {value}")
            else:
                click.echo(f"Unknown configuration key: {key}", err=True)


def _get_metrics(metric_names: list[str]) -> list:
    """Get metric objects from metric names."""
    metric_map = {
        "length": ConversationLengthMetric,
        "relevance": ResponseRelevanceMetric,
        "coherence": ConversationCoherenceMetric,
        "quality": ConversationQualityMetric,
        "helpfulness": ResponseHelpfulnessMetric,
        "safety": ResponseSafetyMetric,
        # Aliases
        "conversation_length": ConversationLengthMetric,
        "response_relevance": ResponseRelevanceMetric,
        "conversation_coherence": ConversationCoherenceMetric,
        "conversation_quality": ConversationQualityMetric,
        "response_helpfulness": ResponseHelpfulnessMetric,
        "response_safety": ResponseSafetyMetric,
    }

    if not metric_names:
        # Default metrics
        return [
            ConversationLengthMetric(),
            ResponseRelevanceMetric(),
            ConversationCoherenceMetric(),
        ]

    metrics = []
    for name in metric_names:
        if name not in metric_map:
            available = list(metric_map.keys())
            click.echo(
                f"Warning: Unknown metric '{name}'. Available: {available}", err=True
            )
            continue

        metric_class = metric_map[name]
        metrics.append(metric_class())

    if not metrics:
        click.echo("Error: No valid metrics specified", err=True)
        sys.exit(1)

    return metrics


def _format_results_json(results) -> str:
    """Format results as JSON."""
    output_data = []
    for result in results:
        output_data.append(
            {
                "conversation": {
                    "turns": [
                        {"role": turn.role.value, "content": turn.content}
                        for turn in result.conversation.turns
                    ],
                    "metadata": result.conversation.metadata,
                },
                "overall_score": result.overall_score,
                "passed": result.passed,
                "results": [
                    {
                        "metric_name": r.metric_name,
                        "score": r.score,
                        "passed": r.passed,
                        "details": r.details,
                        "error": r.error,
                    }
                    for r in result.results
                ],
                "metadata": result.metadata,
            }
        )

    return json.dumps(output_data, indent=2)


def _format_results_text(results) -> str:
    """Format results as human-readable text."""
    output_lines = []

    for i, result in enumerate(results):
        output_lines.append(f"=== Conversation {i + 1} ===")
        output_lines.append(f"Overall Score: {result.overall_score:.3f}")
        output_lines.append(f"Status: {'PASSED' if result.passed else 'FAILED'}")
        output_lines.append("")

        output_lines.append("Metric Results:")
        for metric_result in result.results:
            status = "✓" if metric_result.passed else "✗"
            output_lines.append(
                f"  {status} {metric_result.metric_name}: {metric_result.score:.3f}"
            )
            if metric_result.error:
                output_lines.append(f"    Error: {metric_result.error}")
        output_lines.append("")

    return "\n".join(output_lines)


def _format_summary_text(summary) -> str:
    """Format summary as human-readable text."""
    output_lines = []

    output_lines.append("=== Evaluation Summary ===")
    output_lines.append(f"Total Conversations: {summary['total_conversations']}")
    output_lines.append(f"Passed Conversations: {summary['passed_conversations']}")
    output_lines.append(f"Overall Pass Rate: {summary['overall_pass_rate']:.1%}")
    output_lines.append(
        f"Average Overall Score: {summary['average_overall_score']:.3f}"
    )
    output_lines.append("")

    output_lines.append("Metric Statistics:")
    for metric_name, stats in summary["metric_statistics"].items():
        output_lines.append(f"  {metric_name}:")
        output_lines.append(f"    Pass Rate: {stats['pass_rate']:.1%}")
        output_lines.append(f"    Average Score: {stats['average_score']:.3f}")
        output_lines.append(
            f"    Score Range: {stats['min_score']:.3f} - {stats['max_score']:.3f}"
        )
        if stats["error_count"] > 0:
            output_lines.append(f"    Errors: {stats['error_count']}")
        output_lines.append("")

    return "\n".join(output_lines)

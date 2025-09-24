"""Main CLI entry point for Turnwise."""

import click

from .commands import batch_evaluate, config_cmd, evaluate, list_metrics


@click.group()
@click.version_option()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--config", "-c", help="Path to configuration file")
@click.pass_context
def cli(ctx, verbose, config):
    """Turnwise: A modern Python library for evaluating multi-turn chatbot conversations."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose
    ctx.obj["config"] = config

    if verbose:
        from turnwise.utils.logging import setup_logging

        setup_logging(level="DEBUG")


# Add subcommands
cli.add_command(evaluate)
cli.add_command(batch_evaluate)
cli.add_command(list_metrics)
cli.add_command(config_cmd)

if __name__ == "__main__":
    cli()

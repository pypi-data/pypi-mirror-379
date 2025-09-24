"""Simple configuration for Turnwise."""

from dataclasses import dataclass


@dataclass
class EvaluationConfig:
    """Simple configuration for evaluation runs."""

    max_workers: int = 4
    verbose: bool = False

    def to_dict(self) -> dict:
        """Convert config to dictionary."""
        return {
            "max_workers": self.max_workers,
            "verbose": self.verbose,
        }


# Global config instance
config = EvaluationConfig()

"""CLI usage example for Turnwise."""

import subprocess
from pathlib import Path


def run_cli_example():
    """Demonstrate Turnwise CLI usage with sample conversation."""

    print("=== Turnwise CLI Usage Example ===\n")

    # Get the path to the sample conversation
    sample_file = Path(__file__).parent / "sample_conversation.json"

    if not sample_file.exists():
        print("❌ Sample conversation file not found!")
        return

    print(f"📁 Using sample conversation: {sample_file}")
    print()

    # Example 1: Basic evaluation
    print("1️⃣ Basic evaluation with length metric:")
    print("   Command: turnwise evaluate sample_conversation.json -m length")
    print("   Output:")
    try:
        result = subprocess.run(
            ["uv", "run", "turnwise", "evaluate", str(sample_file), "-m", "length"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        if result.returncode == 0:
            print("   " + result.stdout.replace("\n", "\n   "))
        else:
            print(f"   Error: {result.stderr}")
    except Exception as e:
        print(f"   Error running command: {e}")

    print()

    # Example 2: Multiple metrics
    print("2️⃣ Multiple metrics evaluation:")
    print(
        "   Command: turnwise evaluate sample_conversation.json -m length -m relevance -m coherence"
    )
    print("   Output:")
    try:
        result = subprocess.run(
            [
                "uv",
                "run",
                "turnwise",
                "evaluate",
                str(sample_file),
                "-m",
                "length",
                "-m",
                "relevance",
                "-m",
                "coherence",
            ],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        if result.returncode == 0:
            print("   " + result.stdout.replace("\n", "\n   "))
        else:
            print(f"   Error: {result.stderr}")
    except Exception as e:
        print(f"   Error running command: {e}")

    print()

    # Example 3: JSON output
    print("3️⃣ JSON output format:")
    print(
        "   Command: turnwise evaluate sample_conversation.json -m length --format json"
    )
    print("   Output:")
    try:
        result = subprocess.run(
            [
                "uv",
                "run",
                "turnwise",
                "evaluate",
                str(sample_file),
                "-m",
                "length",
                "--format",
                "json",
            ],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        if result.returncode == 0:
            print("   " + result.stdout.replace("\n", "\n   "))
        else:
            print(f"   Error: {result.stderr}")
    except Exception as e:
        print(f"   Error running command: {e}")

    print()

    # Example 4: List available metrics
    print("4️⃣ List available metrics:")
    print("   Command: turnwise list-metrics")
    print("   Output:")
    try:
        result = subprocess.run(
            ["uv", "run", "turnwise", "list-metrics"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        if result.returncode == 0:
            print("   " + result.stdout.replace("\n", "\n   "))
        else:
            print(f"   Error: {result.stderr}")
    except Exception as e:
        print(f"   Error running command: {e}")

    print()
    print("🎯 Try these commands yourself:")
    print(f"   cd {Path(__file__).parent.parent}")
    print("   uv run turnwise evaluate examples/sample_conversation.json -m length")
    print(
        "   uv run turnwise evaluate examples/sample_conversation.json -m length -m relevance"
    )
    print("   uv run turnwise list-metrics")


if __name__ == "__main__":
    run_cli_example()

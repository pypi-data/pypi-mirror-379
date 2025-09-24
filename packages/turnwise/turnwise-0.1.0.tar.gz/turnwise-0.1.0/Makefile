# Turnwise Development Makefile

.PHONY: help install test lint format clean run-example run-llm-example

# Default target
help:
	@echo "Turnwise Development Commands"
	@echo "============================="
	@echo ""
	@echo "  install        Install dependencies"
	@echo "  test           Run tests"
	@echo "  lint           Run linter"
	@echo "  format         Format code"
	@echo "  clean          Clean build artifacts"
	@echo "  run-example    Run basic example"
	@echo "  run-llm-example Run LLM evaluation example"
	@echo ""

# Setup
install:
	uv sync

# Testing
test:
	uv run pytest -v

# Code Quality
lint:
	uv run ruff check src/ tests/ examples/

format:
	uv run ruff format src/ tests/ examples/

# Development
clean:
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

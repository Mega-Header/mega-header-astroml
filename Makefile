.PHONY: help quickstart test lint format clean install

help:
	@echo "AstroML Development Commands"
	@echo "============================"
	@echo ""
	@echo "make quickstart          Run quick start: ingestion → graph → train pipeline"
	@echo "make quickstart-verbose  Run quick start with verbose output"
	@echo "make test                Run test suite"
	@echo "make lint                Run linters (flake8, mypy)"
	@echo "make format              Format code (black, isort)"
	@echo "make install             Install development dependencies"
	@echo "make clean               Clean build artifacts and cache"
	@echo ""

quickstart:
	python -m mega-header-astroml.quick_start

quickstart-verbose:
	python -m mega-header-astroml.quick_start --num-ledgers 200 --num-accounts 100 --epochs 20

test:
	pytest tests/ -v

lint:
	flake8 mega-header-astroml/ tests/
	mypy mega-header-astroml/ --ignore-missing-imports

format:
	black mega-header-astroml/ tests/
	isort mega-header-astroml/ tests/

install:
	pip install -e ".[dev]"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache build/ dist/ *.egg-info
	rm -rf benchmark_results/quickstart .mega-header-astroml_state_quickstart

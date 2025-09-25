# Makefile for PFAGD development

.PHONY: help install dev-install test test-coverage lint format type-check security docs clean build publish

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install package in production mode"
	@echo "  dev-install  Install package in development mode"
	@echo "  test         Run tests"
	@echo "  test-coverage Run tests with coverage"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  type-check   Run type checking with mypy"
	@echo "  security     Run security checks"
	@echo "  docs         Build documentation"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build distribution packages"
	@echo "  publish      Publish to PyPI (requires authentication)"
	@echo "  publish-test Publish to TestPyPI (requires authentication)"

# Installation
install:
	pip install .

dev-install:
	pip install -e .[dev]
	pre-commit install

# Testing
test:
	pytest

test-coverage:
	pytest --cov=pfagd --cov-report=html --cov-report=term-missing

# Code quality
lint:
	flake8 pfagd tests
	bandit -r pfagd

format:
	black pfagd tests
	isort pfagd tests

type-check:
	mypy pfagd

security:
	safety check
	bandit -r pfagd

# Documentation
docs:
	cd docs && sphinx-build -b html . _build/html

# Build and publish
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete

build: clean
	python -m build

publish: build
	twine upload dist/*

publish-test: build
	twine upload --repository testpypi dist/*

# All quality checks
check-all: lint type-check security test

# Development setup
setup-dev: dev-install
	@echo "Development environment set up successfully!"
	@echo "Run 'make help' to see available commands."
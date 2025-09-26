.ONESHELL:

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[1;33m
RED = \033[0;31m

SUCCESS = \033[0;32m [SUCCESS]:
WARNING = \033[1;33m [WARNING]:
ERROR = \033[0;31m [ERROR]:
INFO = \033[1;37m [INFO]:
HINT = \033[3;37m

NC = \033[0m # No Color

# Default target
.DEFAULT_GOAL := help

# Project configuration
PROJECT_NAME := "RisoTech Python Kit"

# ==============================================================================
# SETUP & INSTALLATION
# ==============================================================================

# Complete development environment setup
.PHONY: setup
setup:
	@echo "${INFO} Setting up $(PROJECT_NAME) development environment...${NC}"
	@pip install --upgrade pip
	@pip install --upgrade pip-tools
	@pip-compile requirements/requirements.in --output-file=requirements/requirements.txt
	@pip-sync requirements/requirements.txt
	@pre-commit install
	@echo "${SUCCESS} $(PROJECT_NAME) development environment ready!${NC}"

# ==============================================================================
# TESTING
# ==============================================================================

# Run tests with coverage
.PHONY: test
test:
	@echo "${INFO} Running tests with coverage...${NC}"
	@pytest --cov=pykit --cov-report=term-missing --cov-report=html
	@echo "${SUCCESS} Tests completed with coverage report!${NC}"

# Run tests without coverage
.PHONY: test-fast
test-fast:
	@echo "${INFO} Running tests (fast mode)...${NC}"
	@pytest -v
	@echo "${SUCCESS} Fast tests completed!${NC}"

# ==============================================================================
# PACKAGE MANAGEMENT
# ==============================================================================

# Build package distributions
.PHONY: build
build:
	@echo "${INFO} Building package distributions...${NC}"
	@python -m build
	@echo "${SUCCESS} Package built successfully!${NC}"

# Upload to test PyPI
.PHONY: upload-test
upload-test: build
	@echo "${INFO} Uploading to test PyPI...${NC}"
	@python -m twine upload --repository testpypi dist/*
	@echo "${SUCCESS} Package uploaded to test PyPI!${NC}"

# Upload to PyPI
.PHONY: upload
upload: build
	@echo "${WARNING} Uploading to production PyPI...${NC}"
	@python -m twine upload dist/*
	@echo "${SUCCESS} Package uploaded to PyPI!${NC}"

# ==============================================================================
# CLEANUP
# ==============================================================================

# Remove temporary files and caches
.PHONY: clean
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name "*.pyd" -delete 2>/dev/null || true
	@find . -type f -name ".coverage" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "*.egg" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	@rm -rf build/ 2>/dev/null || true
	@rm -rf dist/ 2>/dev/null || true
	@rm -rf .tox/ 2>/dev/null || true
	@rm -rf htmlcov/ 2>/dev/null || true
	@echo "${INFO} Cleaned up compiled files for $(PROJECT_NAME)${NC}"

# ==============================================================================
# HELP
# ==============================================================================

# Display help
.PHONY: help
help:
	@echo "============================================================================"
	@echo "                         ${GREEN}$(PROJECT_NAME) Makefile${NC}"
	@echo "============================================================================"
	@echo ""
	@echo "${YELLOW}Development Setup:${NC}"
	@echo "  ${GREEN}make ${YELLOW}setup${NC}               - Setup development environment"
	@echo ""
	@echo "${YELLOW}Testing:${NC}"
	@echo "  ${GREEN}make ${YELLOW}test${NC}                 - Run tests with coverage"
	@echo "  ${GREEN}make ${YELLOW}test-fast${NC}            - Run tests without coverage"
	@echo ""
	@echo "${YELLOW}Package Management:${NC}"
	@echo "  ${GREEN}make ${YELLOW}build${NC}                - Build package distributions"
	@echo "  ${GREEN}make ${YELLOW}upload-test${NC}          - Upload to test PyPI"
	@echo "  ${GREEN}make ${YELLOW}upload${NC}               - Upload to production PyPI"
	@echo ""
	@echo "${YELLOW}Utilities:${NC}"
	@echo "  ${GREEN}make ${YELLOW}clean${NC}                - Clean up compiled files"
	@echo "  ${GREEN}make ${YELLOW}help${NC}                 - Display this help message"

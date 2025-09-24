# Face Enhancement API Makefile
# Cross-platform commands

.PHONY: help install install-dev install-linux start test clean build package

help: ## Show this help message
	@echo "Face Enhancement Service - Available Commands:"
	@echo "=========================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install basic dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install pytest pytest-asyncio black flake8

install-linux: ## Install Linux-optimized dependencies
	pip install -r requirements.txt
	pip install uvloop httptools

start: ## Start the API server
	python launch.py

start-dev: ## Start API in development mode
	uvicorn src.face_enhancer_api:app --reload --host 0.0.0.0 --port 8000

test: ## Run tests
	pytest tests/ -v

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	python setup.py sdist bdist_wheel

package: ## Create distribution package
	python -m build

install-package: ## Install the package locally
	pip install -e .

docker-build: ## Build Docker image
	docker build -t face-enhancement-service .

docker-run: ## Run Docker container
	docker run -p 8000:8000 face-enhancement-service

docker-compose-up: ## Start with Docker Compose
	docker-compose up -d

docker-compose-down: ## Stop Docker Compose
	docker-compose down

format: ## Format code with black
	black src/ tests/

lint: ## Lint code with flake8
	flake8 src/ tests/

check: format lint test ## Run all checks

# Platform-specific shortcuts
windows: ## Windows-specific installation
	pip install -r requirements_windows.txt

linux: ## Linux-specific installation  
	pip install -r requirements.txt
	pip install uvloop httptools

mac: ## Mac-specific installation
	pip install -r requirements.txt
	pip install uvloop httptools

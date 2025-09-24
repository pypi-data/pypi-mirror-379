.PHONY: help install install-dev test test-cov lint format clean build upload docs

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install the package
	pip install -e .

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt
	pip install -e .

test: ## Run tests
	python manage.py test dj_health_checker

test-cov: ## Run tests with coverage
	coverage run --source='.' manage.py test dj_health_checker
	coverage report
	coverage html

lint: ## Run linting
	flake8 dj_health_checker/
	isort --check-only dj_health_checker/

format: ## Format code
	black dj_health_checker/
	isort dj_health_checker/

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -path "./venv" -prune -o -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -path "./venv" -prune -o -type f -name "*.pyc" -delete 2>/dev/null || true

build: clean ## Build package
	python -m build

upload: build ## Upload to PyPI
	twine upload dist/*

docs: ## Build documentation
	cd docs && make html

migrate: ## Run database migrations
	python manage.py migrate

makemigrations: ## Create database migrations
	python manage.py makemigrations dj_health_checker

shell: ## Start Django shell
	python manage.py shell

runserver: ## Start development server
	python manage.py runserver

health-check: ## Run health checks
	python manage.py run_health_checks --save-results --verbose

cleanup: ## Cleanup old health data
	python manage.py cleanup_health_data --days 7

superuser: ## Create superuser
	python manage.py createsuperuser

# Health check specific targets
create-health-check: ## Create a health check via management command
	@echo "Creating health check..."
	@read -p "Enter health check name: " name; \
	read -p "Enter URL to check: " url; \
	read -p "Enter timeout (default 5): " timeout; \
	timeout=$${timeout:-5}; \
	python manage.py shell -c "from dj_health_checker.models import HealthCheck; HealthCheck.objects.create(name='$$name', url='$$url', timeout=$$timeout)"

list-health-checks: ## List all health checks
	python manage.py shell -c "from dj_health_checker.models import HealthCheck; [print(f'{hc.id}: {hc.name} - {hc.url} (active: {hc.is_active})') for hc in HealthCheck.objects.all()]"

# Development helpers
check: lint test ## Run linting and tests
	@echo "All checks passed!"

dev-setup: install-dev migrate superuser ## Complete development setup
	@echo "Development environment ready!"
	@echo "Run 'make runserver' to start the development server"

# Docker helpers (if needed)
docker-build: ## Build Docker image
	docker build -t dj-health-checker .

docker-run: ## Run Docker container
	docker run -p 8000:8000 dj-health-checker

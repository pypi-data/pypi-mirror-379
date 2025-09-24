# Django Health Checker

A comprehensive Django health checker app for monitoring application health, system resources, and external services. Perfect for production environments, Kubernetes deployments, and Docker containers.

## Features

- **Multiple Health Check Endpoints**: Basic, detailed, liveness, and readiness probes
- **System Monitoring**: Database, cache, memory, disk, and CPU monitoring
- **External Service Checks**: Monitor external APIs and services
- **Historical Data**: Store and retrieve health check history
- **Admin Interface**: Full Django admin integration for managing health checks
- **Management Commands**: CLI tools for running health checks and cleanup
- **Webhook Support**: Receive health check data from external monitoring services
- **Kubernetes Ready**: Built-in liveness and readiness probe endpoints
- **Comprehensive Testing**: Full test suite with 90%+ coverage

## Installation

### From PyPI (Recommended)

```bash
pip install dj-health-checker
```

### From Source

```bash
git clone https://github.com/azcare/dj-health-checker.git
cd dj-health-checker
pip install -e .
```

## Quick Start

1. **Add to INSTALLED_APPS**:

```python
# settings.py
INSTALLED_APPS = [
    # ... other apps
    'dj_health_checker',
]
```

2. **Include URLs**:

```python
# urls.py
from django.urls import path, include

urlpatterns = [
    # ... other patterns
    path('health/', include('dj_health_checker.urls')),
]
```

3. **Run Migrations**:

```bash
python manage.py migrate
```

4. **Test the Endpoints**:

```bash
# Basic health check
curl http://localhost:8000/health/

# Detailed health check
curl http://localhost:8000/health/detailed/

# Kubernetes liveness probe
curl http://localhost:8000/health/live/

# Kubernetes readiness probe
curl http://localhost:8000/health/ready/
```

## API Endpoints

### Basic Health Check
- **URL**: `/health/`
- **Method**: GET
- **Description**: Basic application health status
- **Response**: JSON with overall status and basic checks

### Detailed Health Check
- **URL**: `/health/detailed/`
- **Method**: GET
- **Description**: Comprehensive health information including system resources
- **Response**: JSON with detailed system information

### Liveness Probe
- **URL**: `/health/live/`
- **Method**: GET
- **Description**: Simple liveness check for Kubernetes/Docker
- **Response**: JSON with alive status

### Readiness Probe
- **URL**: `/health/ready/`
- **Method**: GET
- **Description**: Readiness check for Kubernetes/Docker
- **Response**: JSON with ready status

### Health History
- **URL**: `/health/history/`
- **Method**: GET
- **Description**: Retrieve health check history
- **Parameters**: `limit` (default: 100)

### Webhook Endpoint
- **URL**: `/health/webhook/`
- **Method**: POST
- **Description**: Receive health check data from external services
- **Body**: JSON with status, response_time, and details

## Configuration

### Settings

Add these optional settings to your `settings.py`:

```python
# Health check version
HEALTH_CHECK_VERSION = '1.0.0'

# Environment name
ENVIRONMENT = 'production'

# External services to monitor
HEALTH_CHECK_EXTERNAL_SERVICES = [
    {
        'name': 'api_service',
        'url': 'https://api.example.com/health'
    },
    {
        'name': 'database_service',
        'url': 'https://db.example.com/health'
    }
]
```

### Graceful Degradation

The health checker is designed to work gracefully even when database or cache are not configured:

- **No Database**: Returns `not_configured` status instead of failing
- **No Cache**: Returns `not_configured` status instead of failing
- **Overall Health**: Remains `healthy` when services are not configured
- **Readiness Probe**: Works even without database configuration

#### Status Types:
- `healthy`: Service is configured and working properly
- `unhealthy`: Service is configured but failing (triggers HTTP 503)
- `not_configured`: Service is not configured (not an error, HTTP 200)
- `warning`: Service is working but with warnings

### Database Models

The app provides several models for storing health check data:

- **HealthCheck**: Configuration for health checks
- **HealthCheckResult**: Results of health check runs
- **HealthCheckAlert**: Alert configurations
- **HealthCheckMetric**: Metrics for monitoring and analytics

## Management Commands

### Run Health Checks

```bash
# Run all active health checks
python manage.py run_health_checks --save-results

# Run a specific health check
python manage.py run_health_checks --check-id 1 --verbose

# Run without saving results
python manage.py run_health_checks
```

### Cleanup Old Data

```bash
# Cleanup data older than 30 days (default)
python manage.py cleanup_health_data

# Cleanup data older than 7 days
python manage.py cleanup_health_data --days 7

# Dry run to see what would be deleted
python manage.py cleanup_health_data --dry-run
```

## Kubernetes Integration

### Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-app
spec:
  template:
    spec:
      containers:
      - name: django
        image: your-django-app
        ports:
        - containerPort: 8000
        livenessProbe:
          httpGet:
            path: /health/live/
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health/ready/
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Docker Example

```dockerfile
FROM python:3.11-slim

# ... your app setup

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1
```

## Admin Interface

Access the Django admin to manage health checks:

1. Create a superuser: `python manage.py createsuperuser`
2. Visit `/admin/`
3. Configure health checks, view results, and manage alerts

## Testing

Run the test suite:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python manage.py test dj_health_checker

# Run with coverage
coverage run --source='.' manage.py test dj_health_checker
coverage report
coverage html
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/azcare/dj-health-checker.git
cd dj-health-checker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Code Quality

```bash
# Format code
black dj_health_checker/
isort dj_health_checker/

# Lint code
flake8 dj_health_checker/

# Type checking (if using mypy)
mypy dj_health_checker/
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `python manage.py test`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [GitHub Wiki](https://github.com/azcare/dj-health-checker/wiki)
- **Issues**: [GitHub Issues](https://github.com/azcare/dj-health-checker/issues)
- **Discussions**: [GitHub Discussions](https://github.com/azcare/dj-health-checker/discussions)

## Changelog

### Version 1.0.0
- Initial release
- Basic and detailed health check endpoints
- Kubernetes liveness and readiness probes
- System resource monitoring
- External service monitoring
- Admin interface
- Management commands
- Comprehensive test suite
- Webhook support
- Historical data storage

## Roadmap

- [ ] Prometheus metrics integration
- [ ] Grafana dashboard templates
- [ ] Slack/Teams notifications
- [ ] Email alerts
- [ ] Custom health check plugins
- [ ] Health check scheduling
- [ ] Performance analytics
- [ ] Multi-tenant support

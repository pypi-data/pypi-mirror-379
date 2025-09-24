#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Test endpoints
curl http://localhost:8000/health/
curl http://localhost:8000/health/detailed/
curl http://localhost:8000/health/live/
curl http://localhost:8000/health/ready/

# Run health checks
python manage.py run_health_checks --save-results --verbose
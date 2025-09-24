import json
import time
import psutil
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.db import connection
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .models import HealthCheck, HealthCheckResult
from .utils import get_database_status, get_cache_status, get_disk_usage, get_memory_usage


@require_http_methods(["GET"])
def health_check(request):
    """
    Basic health check endpoint that returns the status of the application.
    Returns 200 if healthy, 503 if unhealthy.
    """
    try:
        # Basic application health
        health_status = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': getattr(settings, 'HEALTH_CHECK_VERSION', '1.0.0'),
            'checks': {}
        }
        
        # Database check
        try:
            db_status = get_database_status()
            health_status['checks']['database'] = db_status
            # Only mark as unhealthy if database is configured but failing
            if db_status['status'] == 'unhealthy':
                health_status['status'] = 'unhealthy'
        except Exception as e:
            health_status['checks']['database'] = {
                'status': 'unhealthy',
                'error': str(e)
            }
            health_status['status'] = 'unhealthy'
        
        # Cache check
        try:
            cache_status = get_cache_status()
            health_status['checks']['cache'] = cache_status
            # Only mark as unhealthy if cache is configured but failing
            if cache_status['status'] == 'unhealthy':
                health_status['status'] = 'unhealthy'
        except Exception as e:
            health_status['checks']['cache'] = {
                'status': 'unhealthy',
                'error': str(e)
            }
            health_status['status'] = 'unhealthy'
        
        # System resources check
        try:
            health_status['checks']['system'] = {
                'memory': get_memory_usage(),
                'disk': get_disk_usage()
            }
        except Exception as e:
            health_status['checks']['system'] = {
                'status': 'unhealthy',
                'error': str(e)
            }
            health_status['status'] = 'unhealthy'
        
        # Determine HTTP status code
        status_code = 200 if health_status['status'] == 'healthy' else 503
        
        return JsonResponse(health_status, status=status_code)
        
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }, status=503)


@require_http_methods(["GET"])
def health_check_detailed(request):
    """
    Detailed health check endpoint with comprehensive system information.
    """
    try:
        detailed_status = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': getattr(settings, 'HEALTH_CHECK_VERSION', '1.0.0'),
            'environment': getattr(settings, 'ENVIRONMENT', 'development'),
            'debug': settings.DEBUG,
            'checks': {}
        }
        
        # Database detailed check
        try:
            db_status = get_database_status()
            detailed_status['checks']['database'] = db_status
            if db_status['status'] == 'unhealthy':
                detailed_status['status'] = 'unhealthy'
        except Exception as e:
            detailed_status['checks']['database'] = {
                'status': 'unhealthy',
                'error': str(e)
            }
            detailed_status['status'] = 'unhealthy'
        
        # Cache detailed check
        try:
            cache_status = get_cache_status()
            detailed_status['checks']['cache'] = cache_status
            if cache_status['status'] == 'unhealthy':
                detailed_status['status'] = 'unhealthy'
        except Exception as e:
            detailed_status['checks']['cache'] = {
                'status': 'unhealthy',
                'error': str(e)
            }
            detailed_status['status'] = 'unhealthy'
        
        # System resources detailed check
        try:
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            detailed_status['checks']['system'] = {
                'memory': {
                    'total': memory.total,
                    'available': memory.available,
                    'percent': memory.percent,
                    'status': 'healthy' if memory.percent < 90 else 'warning'
                },
                'disk': {
                    'total': disk.total,
                    'free': disk.free,
                    'percent': (disk.used / disk.total) * 100,
                    'status': 'healthy' if (disk.used / disk.total) * 100 < 90 else 'warning'
                }
            }
        except Exception as e:
            detailed_status['checks']['system'] = {
                'status': 'unhealthy',
                'error': str(e)
            }
            detailed_status['status'] = 'unhealthy'
        
        # External services check (if configured)
        external_services = getattr(settings, 'HEALTH_CHECK_EXTERNAL_SERVICES', [])
        if external_services:
            detailed_status['checks']['external'] = {}
            for service in external_services:
                try:
                    response = requests.get(service['url'], timeout=5)
                    detailed_status['checks']['external'][service['name']] = {
                        'status': 'healthy' if response.status_code == 200 else 'unhealthy',
                        'response_time': response.elapsed.total_seconds(),
                        'status_code': response.status_code
                    }
                except Exception as e:
                    detailed_status['checks']['external'][service['name']] = {
                        'status': 'unhealthy',
                        'error': str(e)
                    }
                    detailed_status['status'] = 'unhealthy'
        
        # Determine HTTP status code
        status_code = 200 if detailed_status['status'] == 'healthy' else 503
        
        return JsonResponse(detailed_status, status=status_code)
        
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }, status=503)


@require_http_methods(["GET"])
def health_check_live(request):
    """
    Liveness probe endpoint for Kubernetes/Docker.
    Simple check that the application is running.
    """
    return JsonResponse({
        'status': 'alive',
        'timestamp': datetime.now().isoformat()
    })


@require_http_methods(["GET"])
def health_check_ready(request):
    """
    Readiness probe endpoint for Kubernetes/Docker.
    Checks if the application is ready to serve traffic.
    """
    try:
        # Check if database is configured and accessible
        if hasattr(settings, 'DATABASES') and settings.DATABASES and 'default' in settings.DATABASES:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        
        return JsonResponse({
            'status': 'ready',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'not_ready',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }, status=503)


@require_http_methods(["GET"])
def health_check_history(request):
    """
    Returns the history of health check results.
    """
    try:
        limit = int(request.GET.get('limit', 100))
        health_checks = HealthCheckResult.objects.order_by('-timestamp')[:limit]
        
        results = []
        for check in health_checks:
            results.append({
                'id': check.id,
                'timestamp': check.timestamp.isoformat(),
                'status': check.status,
                'response_time': check.response_time,
                'details': check.details
            })
        
        return JsonResponse({
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def health_check_webhook(request):
    """
    Webhook endpoint for external health monitoring services.
    """
    try:
        data = json.loads(request.body)
        
        # Create a health check result record
        result = HealthCheckResult.objects.create(
            status=data.get('status', 'unknown'),
            response_time=data.get('response_time', 0),
            details=data.get('details', {})
        )
        
        return JsonResponse({
            'id': result.id,
            'status': 'recorded',
            'timestamp': result.timestamp.isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)

"""
Utility functions for health checks.
"""
import time
import psutil
from django.core.cache import cache
from django.db import connection
from django.conf import settings


def get_database_status():
    """
    Check database connectivity and performance.
    """
    # Check if database is configured
    if not hasattr(settings, 'DATABASES') or not settings.DATABASES:
        return {
            'status': 'not_configured',
            'message': 'No database configuration found'
        }
    
    if 'default' not in settings.DATABASES:
        return {
            'status': 'not_configured',
            'message': 'No default database configuration found'
        }
    
    start_time = time.time()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
        
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        return {
            'status': 'healthy',
            'response_time': f"{response_time:.2f}ms",
            'engine': settings.DATABASES['default']['ENGINE']
        }
    except Exception as e:
        return {
            'status': 'unhealthy',
            'error': str(e)
        }


def get_cache_status():
    """
    Check cache connectivity and performance.
    """
    # Check if cache is configured
    if not hasattr(settings, 'CACHES') or not settings.CACHES:
        return {
            'status': 'not_configured',
            'message': 'No cache configuration found'
        }
    
    if 'default' not in settings.CACHES:
        return {
            'status': 'not_configured',
            'message': 'No default cache configuration found'
        }
    
    start_time = time.time()
    try:
        # Test cache operations
        test_key = 'health_check_test'
        test_value = 'ok'
        
        cache.set(test_key, test_value, 10)
        retrieved_value = cache.get(test_key)
        cache.delete(test_key)
        
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        if retrieved_value == test_value:
            return {
                'status': 'healthy',
                'response_time': f"{response_time:.2f}ms",
                'backend': str(settings.CACHES['default']['BACKEND'])
            }
        else:
            return {
                'status': 'unhealthy',
                'error': 'Cache test failed - value mismatch'
            }
    except Exception as e:
        return {
            'status': 'unhealthy',
            'error': str(e)
        }


def get_disk_usage():
    """
    Get disk usage information.
    """
    try:
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total,
            'used': disk.used,
            'free': disk.free,
            'percent': (disk.used / disk.total) * 100
        }
    except Exception as e:
        return {
            'error': str(e)
        }


def get_memory_usage():
    """
    Get memory usage information.
    """
    try:
        memory = psutil.virtual_memory()
        return {
            'total': memory.total,
            'available': memory.available,
            'used': memory.used,
            'percent': memory.percent
        }
    except Exception as e:
        return {
            'error': str(e)
        }


def get_cpu_usage():
    """
    Get CPU usage information.
    """
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        return {
            'percent': cpu_percent,
            'count': cpu_count
        }
    except Exception as e:
        return {
            'error': str(e)
        }


def check_external_service(url, timeout=5):
    """
    Check external service availability.
    """
    import requests
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        response_time = (time.time() - start_time) * 1000
        
        return {
            'status': 'healthy' if response.status_code == 200 else 'unhealthy',
            'status_code': response.status_code,
            'response_time': f"{response_time:.2f}ms"
        }
    except Exception as e:
        return {
            'status': 'unhealthy',
            'error': str(e)
        }

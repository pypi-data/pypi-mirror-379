import json
import time
from unittest.mock import patch, MagicMock
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.core.cache import cache
from django.db import connection
from django.conf import settings
from .models import HealthCheck, HealthCheckResult, HealthCheckAlert, HealthCheckMetric
from .utils import get_database_status, get_cache_status, get_disk_usage, get_memory_usage


class HealthCheckViewsTestCase(TestCase):
    """Test cases for health check views."""
    
    def setUp(self):
        self.client = Client()
    
    def test_health_check_basic(self):
        """Test basic health check endpoint."""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('status', data)
        self.assertIn('timestamp', data)
        self.assertIn('checks', data)
        self.assertIn('database', data['checks'])
    
    def test_health_check_detailed(self):
        """Test detailed health check endpoint."""
        response = self.client.get('/health/detailed/')
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('status', data)
        self.assertIn('timestamp', data)
        self.assertIn('version', data)
        self.assertIn('environment', data)
        self.assertIn('debug', data)
        self.assertIn('checks', data)
    
    def test_health_check_live(self):
        """Test liveness probe endpoint."""
        response = self.client.get('/health/live/')
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'alive')
        self.assertIn('timestamp', data)
    
    def test_health_check_ready(self):
        """Test readiness probe endpoint."""
        response = self.client.get('/health/ready/')
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'ready')
        self.assertIn('timestamp', data)
    
    def test_health_check_history(self):
        """Test health check history endpoint."""
        # Create a test health check result
        HealthCheckResult.objects.create(
            status='healthy',
            response_time=100.0,
            details={'test': 'data'}
        )
        
        response = self.client.get('/health/history/')
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('results', data)
        self.assertIn('count', data)
        self.assertEqual(data['count'], 1)
    
    def test_health_check_webhook(self):
        """Test webhook endpoint."""
        webhook_data = {
            'status': 'healthy',
            'response_time': 150.0,
            'details': {'source': 'external_monitor'}
        }
        
        response = self.client.post(
            '/health/webhook/',
            data=json.dumps(webhook_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertEqual(data['status'], 'recorded')
        self.assertIn('id', data)
        
        # Verify the result was created
        result = HealthCheckResult.objects.get(id=data['id'])
        self.assertEqual(result.status, 'healthy')
        self.assertEqual(result.response_time, 150.0)


class HealthCheckModelsTestCase(TestCase):
    """Test cases for health check models."""
    
    def test_health_check_creation(self):
        """Test health check model creation."""
        health_check = HealthCheck.objects.create(
            name='Test Check',
            description='A test health check',
            url='https://example.com/health',
            timeout=10,
            expected_status_code=200
        )
        
        self.assertEqual(health_check.name, 'Test Check')
        self.assertEqual(health_check.url, 'https://example.com/health')
        self.assertTrue(health_check.is_active)
        self.assertEqual(str(health_check), 'Test Check')
    
    def test_health_check_result_creation(self):
        """Test health check result model creation."""
        health_check = HealthCheck.objects.create(
            name='Test Check',
            url='https://example.com/health'
        )
        
        result = HealthCheckResult.objects.create(
            health_check=health_check,
            status='healthy',
            response_time=100.0,
            status_code=200,
            details={'test': 'data'}
        )
        
        self.assertEqual(result.health_check, health_check)
        self.assertEqual(result.status, 'healthy')
        self.assertTrue(result.is_healthy)
        self.assertFalse(result.is_unhealthy)
        self.assertIn('Test Check', str(result))
    
    def test_health_check_alert_creation(self):
        """Test health check alert model creation."""
        alert = HealthCheckAlert.objects.create(
            name='Test Alert',
            alert_type='email',
            recipients=['admin@example.com'],
            conditions={'status': 'unhealthy', 'consecutive_failures': 3}
        )
        
        self.assertEqual(alert.name, 'Test Alert')
        self.assertEqual(alert.alert_type, 'email')
        self.assertTrue(alert.is_active)
        self.assertIn('Test Alert', str(alert))
    
    def test_health_check_metric_creation(self):
        """Test health check metric model creation."""
        metric = HealthCheckMetric.objects.create(
            metric_name='response_time',
            metric_value=150.0,
            metric_unit='ms',
            tags={'service': 'api'}
        )
        
        self.assertEqual(metric.metric_name, 'response_time')
        self.assertEqual(metric.metric_value, 150.0)
        self.assertEqual(metric.metric_unit, 'ms')
        self.assertIn('response_time', str(metric))


class HealthCheckUtilsTestCase(TestCase):
    """Test cases for health check utility functions."""
    
    def test_get_database_status(self):
        """Test database status check."""
        status = get_database_status()
        
        self.assertIn('status', status)
        self.assertIn('response_time', status)
        self.assertIn('engine', status)
        self.assertEqual(status['status'], 'healthy')
    
    def test_get_cache_status(self):
        """Test cache status check."""
        status = get_cache_status()
        
        self.assertIn('status', status)
        self.assertIn('response_time', status)
        self.assertIn('backend', status)
        self.assertEqual(status['status'], 'healthy')
    
    @patch('psutil.disk_usage')
    def test_get_disk_usage(self, mock_disk_usage):
        """Test disk usage check."""
        mock_disk = MagicMock()
        mock_disk.total = 1000000000
        mock_disk.used = 500000000
        mock_disk.free = 500000000
        mock_disk_usage.return_value = mock_disk
        
        usage = get_disk_usage()
        
        self.assertIn('total', usage)
        self.assertIn('used', usage)
        self.assertIn('free', usage)
        self.assertIn('percent', usage)
        self.assertEqual(usage['percent'], 50.0)
    
    @patch('psutil.virtual_memory')
    def test_get_memory_usage(self, mock_memory):
        """Test memory usage check."""
        mock_mem = MagicMock()
        mock_mem.total = 8000000000
        mock_mem.available = 4000000000
        mock_mem.used = 4000000000
        mock_mem.percent = 50.0
        mock_memory.return_value = mock_mem
        
        usage = get_memory_usage()
        
        self.assertIn('total', usage)
        self.assertIn('available', usage)
        self.assertIn('used', usage)
        self.assertIn('percent', usage)
        self.assertEqual(usage['percent'], 50.0)


class HealthCheckIntegrationTestCase(TestCase):
    """Integration test cases for health checks."""
    
    def setUp(self):
        self.client = Client()
        # Create a test health check
        self.health_check = HealthCheck.objects.create(
            name='Test API',
            url='https://httpbin.org/status/200',
            timeout=5,
            expected_status_code=200
        )
    
    def test_full_health_check_workflow(self):
        """Test complete health check workflow."""
        # Test basic health check
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        
        # Test detailed health check
        response = self.client.get('/health/detailed/')
        self.assertEqual(response.status_code, 200)
        
        # Test history endpoint
        response = self.client.get('/health/history/')
        self.assertEqual(response.status_code, 200)
    
    def test_health_check_with_external_services(self):
        """Test health check with external services configuration."""
        # This would require mocking external service calls in a real test
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.elapsed.total_seconds.return_value = 0.1
            mock_get.return_value = mock_response
            
            # Test with external services configured
            with self.settings(
                HEALTH_CHECK_EXTERNAL_SERVICES=[
                    {'name': 'test_service', 'url': 'https://httpbin.org/status/200'}
                ]
            ):
                response = self.client.get('/health/detailed/')
                self.assertEqual(response.status_code, 200)

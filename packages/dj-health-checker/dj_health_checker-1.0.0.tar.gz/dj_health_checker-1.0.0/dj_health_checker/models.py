from django.db import models
from django.utils import timezone
import json


class HealthCheck(models.Model):
    """
    Model to store health check configurations.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField(help_text="URL to check")
    timeout = models.IntegerField(default=5, help_text="Timeout in seconds")
    expected_status_code = models.IntegerField(default=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Health Check"
        verbose_name_plural = "Health Checks"
    
    def __str__(self):
        return self.name


class HealthCheckResult(models.Model):
    """
    Model to store health check results.
    """
    STATUS_CHOICES = [
        ('healthy', 'Healthy'),
        ('unhealthy', 'Unhealthy'),
        ('warning', 'Warning'),
        ('unknown', 'Unknown'),
    ]
    
    health_check = models.ForeignKey(
        HealthCheck, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text="Associated health check (if any)"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    response_time = models.FloatField(help_text="Response time in milliseconds")
    status_code = models.IntegerField(null=True, blank=True)
    details = models.JSONField(default=dict, blank=True)
    error_message = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Health Check Result"
        verbose_name_plural = "Health Check Results"
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['status']),
            models.Index(fields=['health_check', 'timestamp']),
        ]
    
    def __str__(self):
        return f"{self.health_check.name if self.health_check else 'System'} - {self.status} ({self.timestamp})"
    
    @property
    def is_healthy(self):
        return self.status == 'healthy'
    
    @property
    def is_unhealthy(self):
        return self.status == 'unhealthy'


class HealthCheckAlert(models.Model):
    """
    Model to store health check alerts and notifications.
    """
    ALERT_TYPES = [
        ('email', 'Email'),
        ('webhook', 'Webhook'),
        ('slack', 'Slack'),
        ('sms', 'SMS'),
    ]
    
    name = models.CharField(max_length=100)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    recipients = models.JSONField(default=list, help_text="List of recipients (emails, webhook URLs, etc.)")
    conditions = models.JSONField(
        default=dict,
        help_text="Alert conditions (e.g., {'status': 'unhealthy', 'consecutive_failures': 3})"
    )
    is_active = models.BooleanField(default=True)
    last_triggered = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Health Check Alert"
        verbose_name_plural = "Health Check Alerts"
    
    def __str__(self):
        return f"{self.name} ({self.alert_type})"


class HealthCheckMetric(models.Model):
    """
    Model to store health check metrics for monitoring and analytics.
    """
    metric_name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    metric_unit = models.CharField(max_length=20, default='ms')
    tags = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Health Check Metric"
        verbose_name_plural = "Health Check Metrics"
        indexes = [
            models.Index(fields=['metric_name', 'timestamp']),
            models.Index(fields=['timestamp']),
        ]
    
    def __str__(self):
        return f"{self.metric_name}: {self.metric_value}{self.metric_unit} ({self.timestamp})"

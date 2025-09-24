from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import HealthCheck, HealthCheckResult, HealthCheckAlert, HealthCheckMetric


@admin.register(HealthCheck)
class HealthCheckAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'timeout', 'expected_status_code', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'expected_status_code']
    search_fields = ['name', 'description', 'url']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'url')
        }),
        ('Configuration', {
            'fields': ('timeout', 'expected_status_code', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(HealthCheckResult)
class HealthCheckResultAdmin(admin.ModelAdmin):
    list_display = ['health_check', 'status', 'response_time', 'status_code', 'timestamp']
    list_filter = ['status', 'timestamp', 'health_check']
    search_fields = ['health_check__name', 'error_message']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('health_check')
    
    def status_colored(self, obj):
        colors = {
            'healthy': 'green',
            'unhealthy': 'red',
            'warning': 'orange',
            'unknown': 'gray'
        }
        color = colors.get(obj.status, 'black')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_colored.short_description = 'Status'
    
    list_display = ['health_check', 'status_colored', 'response_time', 'status_code', 'timestamp']


@admin.register(HealthCheckAlert)
class HealthCheckAlertAdmin(admin.ModelAdmin):
    list_display = ['name', 'alert_type', 'is_active', 'last_triggered', 'created_at']
    list_filter = ['alert_type', 'is_active', 'created_at']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at', 'last_triggered']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'alert_type', 'is_active')
        }),
        ('Configuration', {
            'fields': ('recipients', 'conditions')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'last_triggered'),
            'classes': ('collapse',)
        }),
    )


@admin.register(HealthCheckMetric)
class HealthCheckMetricAdmin(admin.ModelAdmin):
    list_display = ['metric_name', 'metric_value', 'metric_unit', 'timestamp']
    list_filter = ['metric_name', 'metric_unit', 'timestamp']
    search_fields = ['metric_name']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-timestamp')


# Customize admin site headers
admin.site.site_header = "Django Health Checker Administration"
admin.site.site_title = "Health Checker Admin"
admin.site.index_title = "Health Checker Management"

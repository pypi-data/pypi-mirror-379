"""
URL configuration for dj_health_checker app.
"""
from django.urls import path
from . import views

app_name = 'dj_health_checker'

urlpatterns = [
    # Basic health check endpoints
    path('health/', views.health_check, name='health_check'),
    path('health/detailed/', views.health_check_detailed, name='health_check_detailed'),
    
    # Kubernetes/Docker probe endpoints
    path('health/live/', views.health_check_live, name='health_check_live'),
    path('health/ready/', views.health_check_ready, name='health_check_ready'),
    
    # History and monitoring endpoints
    path('health/history/', views.health_check_history, name='health_check_history'),
    path('health/webhook/', views.health_check_webhook, name='health_check_webhook'),
]

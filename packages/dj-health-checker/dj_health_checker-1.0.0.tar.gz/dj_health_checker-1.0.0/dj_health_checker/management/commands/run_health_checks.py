"""
Management command to run health checks.
"""
import time
import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from dj_health_checker.models import HealthCheck, HealthCheckResult, HealthCheckMetric
from dj_health_checker.utils import check_external_service


class Command(BaseCommand):
    help = 'Run configured health checks and store results'

    def add_arguments(self, parser):
        parser.add_argument(
            '--check-id',
            type=int,
            help='Run a specific health check by ID',
        )
        parser.add_argument(
            '--save-results',
            action='store_true',
            help='Save results to database',
        )
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        save_results = options['save_results']
        check_id = options.get('check_id')

        if check_id:
            try:
                health_checks = [HealthCheck.objects.get(id=check_id)]
            except HealthCheck.DoesNotExist:
                raise CommandError(f'Health check with ID {check_id} does not exist')
        else:
            health_checks = HealthCheck.objects.filter(is_active=True)

        if not health_checks:
            self.stdout.write(
                self.style.WARNING('No active health checks found')
            )
            return

        self.stdout.write(f'Running {len(health_checks)} health check(s)...')

        for health_check in health_checks:
            if verbose:
                self.stdout.write(f'Checking: {health_check.name} ({health_check.url})')

            start_time = time.time()
            
            try:
                response = requests.get(
                    health_check.url,
                    timeout=health_check.timeout
                )
                response_time = (time.time() - start_time) * 1000
                
                if response.status_code == health_check.expected_status_code:
                    status = 'healthy'
                    if verbose:
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ {health_check.name}: {status} ({response_time:.2f}ms)')
                        )
                else:
                    status = 'unhealthy'
                    if verbose:
                        self.stdout.write(
                            self.style.ERROR(f'✗ {health_check.name}: {status} (HTTP {response.status_code})')
                        )
                
                details = {
                    'status_code': response.status_code,
                    'expected_status_code': health_check.expected_status_code,
                    'response_time': response_time,
                    'url': health_check.url
                }
                
            except requests.exceptions.Timeout:
                response_time = health_check.timeout * 1000
                status = 'unhealthy'
                error_message = f'Timeout after {health_check.timeout} seconds'
                details = {
                    'error': error_message,
                    'timeout': health_check.timeout,
                    'url': health_check.url
                }
                
                if verbose:
                    self.stdout.write(
                        self.style.ERROR(f'✗ {health_check.name}: {status} (Timeout)')
                    )
                    
            except Exception as e:
                response_time = (time.time() - start_time) * 1000
                status = 'unhealthy'
                error_message = str(e)
                details = {
                    'error': error_message,
                    'url': health_check.url
                }
                
                if verbose:
                    self.stdout.write(
                        self.style.ERROR(f'✗ {health_check.name}: {status} ({error_message})')
                    )

            # Save results if requested
            if save_results:
                result = HealthCheckResult.objects.create(
                    health_check=health_check,
                    status=status,
                    response_time=response_time,
                    status_code=response.status_code if 'response' in locals() else None,
                    details=details,
                    error_message=error_message if 'error_message' in locals() else ''
                )
                
                # Save metrics
                HealthCheckMetric.objects.create(
                    metric_name=f'health_check_response_time',
                    metric_value=response_time,
                    metric_unit='ms',
                    tags={
                        'health_check_id': health_check.id,
                        'health_check_name': health_check.name,
                        'status': status
                    }
                )

        self.stdout.write(
            self.style.SUCCESS('Health checks completed')
        )

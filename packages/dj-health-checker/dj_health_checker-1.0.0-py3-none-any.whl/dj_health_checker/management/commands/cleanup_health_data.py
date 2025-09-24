"""
Management command to cleanup old health check data.
"""
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from dj_health_checker.models import HealthCheckResult, HealthCheckMetric


class Command(BaseCommand):
    help = 'Cleanup old health check results and metrics'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=30,
            help='Number of days to keep data (default: 30)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting',
        )
        parser.add_argument(
            '--results-only',
            action='store_true',
            help='Only cleanup health check results',
        )
        parser.add_argument(
            '--metrics-only',
            action='store_true',
            help='Only cleanup health check metrics',
        )

    def handle(self, *args, **options):
        days = options['days']
        dry_run = options['dry_run']
        results_only = options['results_only']
        metrics_only = options['metrics_only']
        
        cutoff_date = timezone.now() - timedelta(days=days)
        
        self.stdout.write(f'Cleaning up data older than {days} days (before {cutoff_date})')
        
        if not metrics_only:
            # Cleanup health check results
            old_results = HealthCheckResult.objects.filter(timestamp__lt=cutoff_date)
            results_count = old_results.count()
            
            if results_count > 0:
                if dry_run:
                    self.stdout.write(
                        self.style.WARNING(f'Would delete {results_count} health check results')
                    )
                else:
                    deleted_results = old_results.delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Deleted {deleted_results[0]} health check results')
                    )
            else:
                self.stdout.write('No old health check results to delete')
        
        if not results_only:
            # Cleanup health check metrics
            old_metrics = HealthCheckMetric.objects.filter(timestamp__lt=cutoff_date)
            metrics_count = old_metrics.count()
            
            if metrics_count > 0:
                if dry_run:
                    self.stdout.write(
                        self.style.WARNING(f'Would delete {metrics_count} health check metrics')
                    )
                else:
                    deleted_metrics = old_metrics.delete()
                    self.stdout.write(
                        self.style.SUCCESS(f'Deleted {deleted_metrics[0]} health check metrics')
                    )
            else:
                self.stdout.write('No old health check metrics to delete')
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING('Dry run completed - no data was actually deleted')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Cleanup completed')
            )

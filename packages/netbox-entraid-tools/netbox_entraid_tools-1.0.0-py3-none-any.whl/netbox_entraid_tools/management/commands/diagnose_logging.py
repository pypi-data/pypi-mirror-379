"""
Django management command for logging diagnostics.
Usage: python manage.py diagnose_logging
"""

from django.core.management.base import BaseCommand
import sys
import os

# Import our diagnostics class
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from test_logging import LoggingDiagnostics


class Command(BaseCommand):
    """Django management command for logging diagnostics."""

    help = "Diagnose and validate NetBox EntraID Tools logging configuration"

    def add_arguments(self, parser):
        parser.add_argument(
            "--generate-config",
            action="store_true",
            help="Generate sample logging configuration for configuration.py",
        )

    def handle(self, *args, **options):
        """Run the logging diagnostics."""
        self.stdout.write(
            self.style.SUCCESS("Starting NetBox EntraID Tools logging diagnostics...")
        )

        # Run diagnostics
        diagnostics = LoggingDiagnostics()
        diagnostics.run_full_diagnostics()

        # Summary
        if diagnostics.issues:
            self.stdout.write(
                self.style.WARNING(
                    f"\nFound {len(diagnostics.issues)} issues that need attention."
                )
            )
        else:
            self.stdout.write(self.style.SUCCESS("\nLogging configuration looks good!"))

        if diagnostics.recommendations:
            self.stdout.write(
                self.style.NOTICE(
                    f"Generated {len(diagnostics.recommendations)} recommendations for improvement."
                )
            )

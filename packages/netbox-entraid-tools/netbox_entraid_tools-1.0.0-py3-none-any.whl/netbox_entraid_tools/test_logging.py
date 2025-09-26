#!/usr/bin/env python3
"""
NetBox EntraID Tools - Logging Configuration Diagnostics and Helper

This script analyzes, tests, and provides recommendations for NetBox logging
configuration to ensure the plugin's logging works correctly, especially
in debug mode.

Can be run as a Django management command or standalone script.
"""

import os
import sys
import tempfile
import json
import getpass

# Unix-specific imports (may not be available on Windows)
try:
    import stat
    import pwd
    import grp
    import subprocess

    UNIX_FEATURES_AVAILABLE = True
except ImportError:
    UNIX_FEATURES_AVAILABLE = False
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class LoggingDiagnostics:
    """Comprehensive logging configuration diagnostics for NetBox EntraID Tools."""

    def __init__(self):
        self.issues = []
        self.recommendations = []
        self.plugin_name = "netbox_entraid_tools"
        self.logger_name = f"netbox.plugins.{self.plugin_name}"

    def run_full_diagnostics(self):
        """Run complete logging diagnostics and provide recommendations."""
        print("=" * 70)
        print("NetBox EntraID Tools - Logging Configuration Diagnostics")
        print("=" * 70)

        # Test 1: Check Django settings and logging config
        self.check_django_logging_config()

        # Test 2: Check plugin-specific configuration
        self.check_plugin_logging_config()

        # Test 3: Test actual logging functionality
        self.test_logging_functionality()

        # Test 4: Check debug mode implications
        self.check_debug_mode_logging()

        # Test 5: Validate file permissions and paths
        self.validate_log_paths()

        # Test 6: Test in various scenarios
        self.test_logging_scenarios()

        # Report findings and recommendations
        self.generate_report()

    def check_django_logging_config(self):
        """Analyze the current Django LOGGING configuration."""
        print("\n1. ANALYZING DJANGO LOGGING CONFIGURATION")
        print("-" * 50)

        try:
            from django.conf import settings

            if hasattr(settings, "LOGGING"):
                logging_config = settings.LOGGING
                print("✅ LOGGING configuration found in settings")

                # Check handlers
                handlers = logging_config.get("handlers", {})
                print(f"   Handlers configured: {list(handlers.keys())}")

                # Check our plugin logger
                loggers = logging_config.get("loggers", {})
                plugin_logger = loggers.get(
                    self.logger_name, loggers.get("netbox.plugins", {})
                )

                if plugin_logger:
                    print(f"✅ Plugin logger configuration found: {self.logger_name}")
                    print(f"   Level: {plugin_logger.get('level', 'Not set')}")
                    print(f"   Handlers: {plugin_logger.get('handlers', [])}")
                else:
                    print(f"⚠️  No specific logger for {self.logger_name}")
                    self.issues.append("No specific logger configuration for plugin")

                # Check file handlers
                file_handlers = {
                    name: config
                    for name, config in handlers.items()
                    if config.get("class")
                    in ["logging.FileHandler", "logging.handlers.RotatingFileHandler"]
                }

                if file_handlers:
                    print(f"✅ File handlers found: {list(file_handlers.keys())}")
                    for name, config in file_handlers.items():
                        filename = config.get("filename", "Not specified")
                        print(f"   {name}: {filename}")
                else:
                    print("⚠️  No file handlers configured")
                    self.issues.append(
                        "No file handlers - only console logging available"
                    )

            else:
                print("❌ No LOGGING configuration found in settings")
                self.issues.append("Missing LOGGING configuration in settings")

        except Exception as e:
            print(f"❌ Error checking Django settings: {e}")
            self.issues.append(f"Cannot access Django settings: {e}")

    def check_plugin_logging_config(self):
        """Check plugin-specific logging configuration."""
        print("\n2. CHECKING PLUGIN LOGGING CONFIGURATION")
        print("-" * 50)

        try:
            from django.conf import settings

            # Check PLUGINS_CONFIG
            if hasattr(settings, "PLUGINS_CONFIG"):
                plugin_config = settings.PLUGINS_CONFIG.get(self.plugin_name, {})
                log_path = plugin_config.get("log_file_path", "")
                debug_mode = plugin_config.get("debug_mode", False)

                print(f"✅ Plugin configuration found")
                print(f"   Debug mode: {debug_mode}")
                print(
                    f"   Custom log path: {log_path or 'Not set (using auto-detection)'}"
                )

                if debug_mode and not log_path:
                    self.recommendations.append(
                        "Consider setting explicit log_file_path when debug_mode is enabled"
                    )
            else:
                print("⚠️  PLUGINS_CONFIG not found")
                self.issues.append(
                    "PLUGINS_CONFIG missing - plugin configuration unavailable"
                )

            # Test our get_log_file_path function
            from common import get_log_file_path

            detected_path = get_log_file_path()

            if detected_path:
                print(f"✅ Plugin can determine log path: {detected_path}")
            else:
                print("❌ Plugin cannot determine usable log path")
                self.issues.append("No writable log path available for plugin")

        except Exception as e:
            print(f"❌ Error checking plugin configuration: {e}")
            self.issues.append(f"Plugin configuration error: {e}")

    def test_logging_functionality(self):
        """Test actual logging functionality."""
        print("\n3. TESTING LOGGING FUNCTIONALITY")
        print("-" * 50)

        try:
            from common import ensure_plugin_logger

            # Test logger creation
            logger = ensure_plugin_logger()
            print(f"✅ Plugin logger created successfully")
            print(f"   Logger name: {logger.name}")
            print(f"   Logger level: {logger.level}")
            print(f"   Number of handlers: {len(logger.handlers)}")

            # Test each handler type
            for i, handler in enumerate(logger.handlers):
                handler_type = type(handler).__name__
                print(f"   Handler {i+1}: {handler_type}")

                if hasattr(handler, "stream"):
                    print(f"     Stream: {handler.stream}")
                if hasattr(handler, "baseFilename"):
                    print(f"     File: {handler.baseFilename}")
                    # Test file writability
                    try:
                        with open(handler.baseFilename, "a") as f:
                            f.write("")
                        print(f"     ✅ File is writable")
                    except Exception as e:
                        print(f"     ❌ File write error: {e}")
                        self.issues.append(
                            f"Log file not writable: {handler.baseFilename}"
                        )

            # Test actual logging
            test_messages = [
                ("DEBUG", "Test debug message"),
                ("INFO", "Test info message"),
                ("WARNING", "Test warning message"),
                ("ERROR", "Test error message"),
            ]

            print("   Testing log message output...")
            for level, message in test_messages:
                try:
                    getattr(logger, level.lower())(f"DIAGNOSTIC: {message}")
                    print(f"     ✅ {level} message logged successfully")
                except Exception as e:
                    print(f"     ❌ {level} logging failed: {e}")
                    self.issues.append(f"{level} logging failed")

        except Exception as e:
            print(f"❌ Logger functionality test failed: {e}")
            self.issues.append(f"Logger creation/testing failed: {e}")

    def check_debug_mode_logging(self):
        """Check logging configuration for debug mode scenarios."""
        print("\n4. CHECKING DEBUG MODE LOGGING")
        print("-" * 50)

        try:
            from django.conf import settings

            # Check if debug mode is enabled
            plugin_config = getattr(settings, "PLUGINS_CONFIG", {}).get(
                self.plugin_name, {}
            )
            debug_mode = plugin_config.get("debug_mode", False)

            print(f"   Plugin debug mode: {debug_mode}")

            if debug_mode:
                print("   ✅ Debug mode is enabled")

                # Check if logging is adequate for debug mode
                from common import get_log_file_path

                log_path = get_log_file_path()

                if log_path:
                    print(f"   ✅ File logging available for debug output: {log_path}")
                else:
                    print("   ⚠️  No file logging - debug info only in console")
                    self.recommendations.append(
                        "Enable file logging for better debug mode experience"
                    )

                # Test debug-specific logging
                from common import ensure_plugin_logger

                logger = ensure_plugin_logger()

                if logger.level <= 10:  # DEBUG level
                    print("   ✅ Logger level supports debug messages")
                else:
                    print(
                        f"   ⚠️  Logger level ({logger.level}) may filter debug messages"
                    )
                    self.recommendations.append(
                        "Lower logger level to DEBUG (10) for debug mode"
                    )
            else:
                print("   ℹ️  Debug mode disabled - detailed logging not critical")

        except Exception as e:
            print(f"❌ Debug mode check failed: {e}")

    def validate_log_paths(self):
        """Validate log file paths, permissions, and ownership."""
        print("\n5. VALIDATING LOG PATHS, PERMISSIONS & OWNERSHIP")
        print("-" * 60)

        if not UNIX_FEATURES_AVAILABLE:
            print("   ⚠️  Unix permission checking not available (Windows system?)")
            print("   Falling back to basic write permission tests...")
            self._validate_basic_permissions()
            return

        # Get expected NetBox user/group
        expected_user = self.get_netbox_user()
        expected_group = self.get_netbox_group()

        print(f"   Expected NetBox user: {expected_user}")
        print(f"   Expected NetBox group: {expected_group}")

        # Test common log directories (including custom paths)
        test_dirs = [
            "/static/log/netbox",  # Custom log location
            "/var/log/netbox",  # Standard NetBox
            "/opt/netbox/logs",  # Alternative NetBox
            "/tmp",  # Temporary fallback
            ".",  # Current directory fallback
        ]

        print("\n   Testing common log directories:")
        for dir_path in test_dirs:
            self.check_directory_permissions(dir_path, expected_user, expected_group)

        # Test our plugin's detected path
        try:
            from common import get_log_file_path

            plugin_log_path = get_log_file_path()

            if plugin_log_path:
                print(f"\n   Plugin detected path: {plugin_log_path}")
                self.check_file_permissions(
                    plugin_log_path, expected_user, expected_group
                )

                # Test creating/writing the file
                self.test_file_operations(plugin_log_path)
            else:
                print("   ❌ No usable log path detected")
                self.issues.append("No writable log path available")

        except Exception as e:
            print(f"❌ Path validation failed: {e}")

    def _validate_basic_permissions(self):
        """Basic permission validation for systems without Unix features."""
        # Test common log directories (including custom paths)
        test_dirs = [
            "/static/log/netbox",  # Custom log location
            "/var/log/netbox",  # Standard NetBox
            "/opt/netbox/logs",  # Alternative NetBox
            "/tmp",  # Temporary fallback
            ".",  # Current directory fallback
        ]

        print("   Testing common log directories:")
        for dir_path in test_dirs:
            if os.path.exists(dir_path):
                writable = os.access(dir_path, os.W_OK)
                status = "✅ Writable" if writable else "❌ Not writable"
                print(f"     {dir_path}: {status}")
                if not writable:
                    self.issues.append(f"{dir_path} is not writable")
            else:
                print(f"     {dir_path}: ❌ Does not exist")
                if dir_path in ["/var/log/netbox", "/opt/netbox/logs"]:
                    self.recommendations.append(
                        f"Create directory: mkdir -p {dir_path}"
                    )

        # Test our plugin's detected path
        try:
            from common import get_log_file_path

            plugin_log_path = get_log_file_path()

            if plugin_log_path:
                print(f"\n   Plugin detected path: {plugin_log_path}")
                self.test_file_operations(plugin_log_path)
            else:
                print("   ❌ No usable log path detected")
                self.issues.append("No writable log path available")

        except Exception as e:
            print(f"❌ Path validation failed: {e}")

    def get_netbox_user(self):
        """Detect the expected NetBox user."""
        try:
            # Try to detect from process owner or common NetBox users
            common_users = ["netbox", "www-data", "nginx", "apache"]

            # Check if running as one of these users
            import getpass

            current_user = getpass.getuser()

            if current_user in common_users:
                return current_user

            # Try to find NetBox installation and infer user
            for user in common_users:
                try:
                    pwd.getpwnam(user)
                    return user  # Return first valid user found
                except KeyError:
                    continue

            return current_user  # Fallback to current user

        except Exception:
            return "netbox"  # Default assumption

    def get_netbox_group(self):
        """Detect the expected NetBox group."""
        try:
            expected_user = self.get_netbox_user()

            # Get primary group of the expected user
            user_info = pwd.getpwnam(expected_user)
            group_info = grp.getgrgid(user_info.pw_gid)
            return group_info.gr_name

        except Exception:
            return "netbox"  # Default assumption

    def check_directory_permissions(self, dir_path, expected_user, expected_group):
        """Check directory permissions and ownership."""
        if not os.path.exists(dir_path):
            print(f"     {dir_path}: ❌ Does not exist")
            if dir_path in ["/var/log/netbox", "/opt/netbox/logs"]:
                self.recommendations.append(
                    f"Create directory: sudo mkdir -p {dir_path}"
                )
            return

        try:
            # Get file stats
            stat_info = os.stat(dir_path)

            # Get ownership info
            try:
                owner = pwd.getpwuid(stat_info.st_uid).pw_name
                group = grp.getgrgid(stat_info.st_gid).gr_name
            except KeyError:
                owner = f"UID:{stat_info.st_uid}"
                group = f"GID:{stat_info.st_gid}"

            # Get permissions
            perms = stat.filemode(stat_info.st_mode)
            octal_perms = oct(stat_info.st_mode)[-3:]

            # Check writability
            writable = os.access(dir_path, os.W_OK)

            # Report status
            print(f"     {dir_path}:")
            print(
                f"       Owner: {owner}:{group} (expected: {expected_user}:{expected_group})"
            )
            print(f"       Permissions: {perms} ({octal_perms})")
            print(f"       Writable: {'✅ Yes' if writable else '❌ No'}")

            # Check for issues and recommendations
            issues_found = []

            if owner != expected_user:
                issues_found.append(f"Wrong owner (expected {expected_user})")
                self.recommendations.append(
                    f"Fix ownership: sudo chown {expected_user}:{expected_group} {dir_path}"
                )

            if group != expected_group:
                issues_found.append(f"Wrong group (expected {expected_group})")
                if (
                    f"sudo chown {expected_user}:{expected_group} {dir_path}"
                    not in self.recommendations
                ):
                    self.recommendations.append(
                        f"Fix ownership: sudo chown {expected_user}:{expected_group} {dir_path}"
                    )

            if not writable:
                issues_found.append("Not writable")
                self.recommendations.append(
                    f"Fix permissions: sudo chmod 755 {dir_path}"
                )

            # Check if permissions are too restrictive (should be at least 755 for directories)
            dir_perms = stat_info.st_mode & 0o777
            if dir_perms < 0o755:
                issues_found.append(f"Permissions too restrictive ({octal_perms})")
                self.recommendations.append(
                    f"Fix permissions: sudo chmod 755 {dir_path}"
                )

            if issues_found:
                self.issues.extend([f"{dir_path}: {issue}" for issue in issues_found])
                print(f"       Issues: {', '.join(issues_found)}")
            else:
                print(f"       Status: ✅ OK")

        except Exception as e:
            print(f"     {dir_path}: ❌ Error checking - {e}")
            self.issues.append(f"Cannot check {dir_path}: {e}")

    def check_file_permissions(self, file_path, expected_user, expected_group):
        """Check file permissions and ownership."""
        file_dir = os.path.dirname(file_path)

        print(f"     File directory: {file_dir}")

        # Check directory first
        if os.path.exists(file_dir):
            self.check_directory_permissions(file_dir, expected_user, expected_group)
        else:
            print(f"       ❌ Parent directory does not exist")
            self.issues.append(f"Parent directory missing: {file_dir}")
            self.recommendations.append(f"Create directory: sudo mkdir -p {file_dir}")
            return

        # Check file if it exists
        if os.path.exists(file_path):
            print(f"     File: {file_path}")

            try:
                stat_info = os.stat(file_path)

                # Get ownership
                try:
                    owner = pwd.getpwuid(stat_info.st_uid).pw_name
                    group = grp.getgrgid(stat_info.st_gid).gr_name
                except KeyError:
                    owner = f"UID:{stat_info.st_uid}"
                    group = f"GID:{stat_info.st_gid}"

                # Get permissions
                perms = stat.filemode(stat_info.st_mode)
                octal_perms = oct(stat_info.st_mode)[-3:]

                print(f"       Owner: {owner}:{group}")
                print(f"       Permissions: {perms} ({octal_perms})")

                # Check for issues
                file_issues = []

                if owner != expected_user or group != expected_group:
                    file_issues.append("Wrong ownership")
                    self.recommendations.append(
                        f"Fix file ownership: sudo chown {expected_user}:{expected_group} {file_path}"
                    )

                # Files should be at least 644 (readable by group, writable by owner)
                file_perms = stat_info.st_mode & 0o777
                if file_perms < 0o644:
                    file_issues.append(f"Permissions too restrictive ({octal_perms})")
                    self.recommendations.append(
                        f"Fix file permissions: sudo chmod 644 {file_path}"
                    )

                if file_issues:
                    self.issues.extend(
                        [f"{file_path}: {issue}" for issue in file_issues]
                    )
                    print(f"       Issues: {', '.join(file_issues)}")
                else:
                    print(f"       Status: ✅ OK")

            except Exception as e:
                print(f"       ❌ Error checking file - {e}")
                self.issues.append(f"Cannot check file {file_path}: {e}")
        else:
            print(f"     File: {file_path} (will be created)")

    def test_file_operations(self, plugin_log_path):
        """Test actual file operations."""
        print(f"     Testing file operations:")

        try:
            # Test write access
            test_content = "# NetBox EntraID Tools - Logging diagnostic test\n"
            with open(plugin_log_path, "a") as f:
                f.write(test_content)
            print("       ✅ Successfully wrote test content")

            # Test read access
            with open(plugin_log_path, "r") as f:
                content = f.read()
            print("       ✅ Successfully read file content")

            # Clean up test content if it's clearly a test
            if "test" in plugin_log_path.lower() or plugin_log_path.endswith(".test"):
                try:
                    os.remove(plugin_log_path)
                    print("       ✅ Test file cleaned up")
                except:
                    pass
            else:
                # For real log files, just note that we tested
                print("       ℹ️  Test content written to actual log file")

        except PermissionError as e:
            print(f"       ❌ Permission denied: {e}")
            self.issues.append(f"Cannot write to log file: {e}")

            # Try to determine the specific issue
            if "Permission denied" in str(e):
                self.recommendations.append(
                    f"Fix log file permissions or create with proper ownership:\n"
                    f"    sudo touch {plugin_log_path}\n"
                    f"    sudo chown {self.get_netbox_user()}:{self.get_netbox_group()} {plugin_log_path}\n"
                    f"    sudo chmod 644 {plugin_log_path}"
                )

        except Exception as e:
            print(f"       ❌ Write test failed: {e}")
            self.issues.append(f"Cannot write to detected log path: {e}")

    def generate_fix_script(self):
        """Generate a shell script to fix permission issues."""
        if not self.issues:
            return

        print("\n" + "=" * 70)
        print("PERMISSION FIX SCRIPT")
        print("=" * 70)

        print("\n#!/bin/bash")
        print("# Auto-generated script to fix NetBox EntraID Tools logging permissions")
        print("# Run with: sudo bash fix_logging_permissions.sh\n")

        expected_user = self.get_netbox_user()
        expected_group = self.get_netbox_group()

        print("# Create log directories")
        print("mkdir -p /static/log/netbox")
        print("mkdir -p /var/log/netbox")
        print("mkdir -p /opt/netbox/logs")
        print()

        print("# Set directory ownership and permissions")
        print(f"chown {expected_user}:{expected_group} /static/log/netbox")
        print(f"chown {expected_user}:{expected_group} /var/log/netbox")
        print(f"chown {expected_user}:{expected_group} /opt/netbox/logs")
        print("chmod 755 /static/log/netbox")
        print("chmod 755 /var/log/netbox")
        print("chmod 755 /opt/netbox/logs")
        print()

        # Add specific log file fixes
        from common import get_log_file_path

        try:
            plugin_log_path = get_log_file_path()
            if plugin_log_path and not plugin_log_path.startswith("/tmp"):
                print("# Create and set log file permissions")
                print(f"touch {plugin_log_path}")
                print(f"chown {expected_user}:{expected_group} {plugin_log_path}")
                print(f"chmod 644 {plugin_log_path}")
                print()
        except:
            pass

        print("# Restart NetBox (adjust command for your setup)")
        print("# systemctl restart netbox")
        print("# or")
        print("# supervisorctl restart netbox")
        print()
        print("echo 'Logging permissions fixed. Please restart NetBox.'")

        # Also save to file if possible
        try:
            script_path = "fix_logging_permissions.sh"
            with open(script_path, "w") as f:
                f.write("#!/bin/bash\n")
                f.write(
                    "# Auto-generated script to fix NetBox EntraID Tools logging permissions\n\n"
                )
                f.write("mkdir -p /static/log/netbox\n")
                f.write("mkdir -p /var/log/netbox\n")
                f.write("mkdir -p /opt/netbox/logs\n")
                f.write(f"chown {expected_user}:{expected_group} /static/log/netbox\n")
                f.write(f"chown {expected_user}:{expected_group} /var/log/netbox\n")
                f.write(f"chown {expected_user}:{expected_group} /opt/netbox/logs\n")
                f.write("chmod 755 /static/log/netbox\n")
                f.write("chmod 755 /var/log/netbox\n")
                f.write("chmod 755 /opt/netbox/logs\n")

                plugin_log_path = get_log_file_path()
                if plugin_log_path and not plugin_log_path.startswith("/tmp"):
                    f.write(f"touch {plugin_log_path}\n")
                    f.write(
                        f"chown {expected_user}:{expected_group} {plugin_log_path}\n"
                    )
                    f.write(f"chmod 644 {plugin_log_path}\n")

            os.chmod(script_path, 0o755)
            print(f"\n✅ Fix script saved as: {script_path}")

        except Exception as e:
            print(f"\n⚠️  Could not save script file: {e}")

    def test_logging_scenarios(self):
        """Test logging in various scenarios."""
        print("\n6. TESTING VARIOUS LOGGING SCENARIOS")
        print("-" * 50)

        scenarios = [
            ("Job execution logging", self.test_job_logging),
            ("Error condition logging", self.test_error_logging),
            ("Debug information logging", self.test_debug_logging),
        ]

        for scenario_name, test_func in scenarios:
            print(f"\n   Testing: {scenario_name}")
            try:
                test_func()
                print(f"     ✅ {scenario_name} - OK")
            except Exception as e:
                print(f"     ❌ {scenario_name} - Failed: {e}")
                self.issues.append(f"{scenario_name} failed: {e}")

    def test_job_logging(self):
        """Test logging as it would be used in jobs."""
        from common import ensure_plugin_logger

        logger = ensure_plugin_logger()

        # Simulate job logging
        logger.info("Job started: DeprecateContactsJob")
        logger.debug("Processing 5 contacts for validation")
        logger.warning("Contact John Doe not found in EntraID")
        logger.info("Job completed successfully")

    def test_error_logging(self):
        """Test error logging scenarios."""
        from common import ensure_plugin_logger

        logger = ensure_plugin_logger()

        # Simulate error scenarios
        logger.error("Failed to connect to Azure Graph API")
        logger.exception("Simulated exception for testing")

    def test_debug_logging(self):
        """Test debug logging scenarios."""
        from common import ensure_plugin_logger

        logger = ensure_plugin_logger()

        # Simulate debug scenarios
        logger.debug("Azure Graph API response: {user_count: 42}")
        logger.debug("Contact validation details: email=test@example.com, status=valid")

    def generate_report(self):
        """Generate final diagnostic report with recommendations."""
        print("\n" + "=" * 70)
        print("DIAGNOSTIC REPORT")
        print("=" * 70)

        if not self.issues:
            print("🎉 EXCELLENT: No critical logging issues detected!")
        else:
            print(f"⚠️  ISSUES FOUND ({len(self.issues)}):")
            for i, issue in enumerate(self.issues, 1):
                print(f"   {i}. {issue}")

        if self.recommendations:
            print(f"\n💡 RECOMMENDATIONS ({len(self.recommendations)}):")
            for i, rec in enumerate(self.recommendations, 1):
                print(f"   {i}. {rec}")

        # Generate sample configuration
        if self.issues or self.recommendations:
            print("\n" + "=" * 70)
            print("SUGGESTED LOGGING CONFIGURATION")
            print("=" * 70)
            self.generate_sample_config()

            # Generate permission fix script if there are permission issues
            permission_issues = [
                issue
                for issue in self.issues
                if any(
                    keyword in issue.lower()
                    for keyword in [
                        "permission",
                        "ownership",
                        "writable",
                        "chown",
                        "chmod",
                    ]
                )
            ]
            if permission_issues:
                self.generate_fix_script()

    def generate_sample_config(self):
        """Generate sample logging configuration for NetBox configuration.py."""

        print("\n# Add this to your NetBox configuration.py file:")
        print("\n# ===== LOGGING CONFIGURATION =====")

        sample_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "verbose": {
                    "format": "{asctime} {name} {levelname} {message}",
                    "style": "{",
                },
                "simple": {
                    "format": "{levelname} {message}",
                    "style": "{",
                },
            },
            "handlers": {
                "console": {"class": "logging.StreamHandler", "formatter": "simple"},
                "netbox_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "/var/log/netbox/netbox.log",
                    "maxBytes": 1024 * 1024 * 10,  # 10MB
                    "backupCount": 5,
                    "formatter": "verbose",
                },
                "plugin_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "/var/log/netbox/netbox_entraid_tools.log",
                    "maxBytes": 1024 * 1024 * 5,  # 5MB
                    "backupCount": 3,
                    "formatter": "verbose",
                },
            },
            "loggers": {
                "netbox.plugins.netbox_entraid_tools": {
                    "handlers": ["console", "plugin_file"],
                    "level": "DEBUG",
                    "propagate": False,
                },
                "netbox": {
                    "handlers": ["console", "netbox_file"],
                    "level": "INFO",
                },
            },
        }

        print(f"\nLOGGING = {json.dumps(sample_config, indent=4)}")

        print("\n# ===== PLUGIN CONFIGURATION =====")
        plugin_config = {
            "netbox_entraid_tools": {
                "log_file_path": "/var/log/netbox/netbox_entraid_tools.log",
                "debug_mode": True,  # Enable for troubleshooting
                # ... other plugin settings
            }
        }

        print(f"\nPLUGINS_CONFIG = {json.dumps(plugin_config, indent=4)}")

        print("\n# Don't forget to:")
        print("# 1. Create log directory: sudo mkdir -p /var/log/netbox")
        print("# 2. Set permissions: sudo chown netbox:netbox /var/log/netbox")
        print("# 3. Restart NetBox")


def main():
    """Main function - can be called directly or as management command."""
    diagnostics = LoggingDiagnostics()
    diagnostics.run_full_diagnostics()


if __name__ == "__main__":
    main()

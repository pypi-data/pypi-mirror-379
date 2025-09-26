# Utility function to get debug mode from settings
import logging
import os


def get_debug_mode():
    """
    Get the debug_mode setting from plugin configuration.
    Returns a boolean value.
    """
    from django.conf import settings

    if hasattr(settings, "PLUGINS_CONFIG"):
        plugin_config = settings.PLUGINS_CONFIG.get("netbox_entraid_tools", {})
        return plugin_config.get(
            "debug_mode", False
        )  # Default to False for normal operation
    return False  # Default to False for normal operation


def ensure_plugin_logger():
    """
    Ensure we have a dedicated logger for the plugin that logs to both the console and a file.
    Uses configurable log file path from Settings model.
    """
    logger = logging.getLogger("netbox.plugins.netbox_entraid_tools")

    # Check if handlers are already configured to avoid duplicates
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Console handler
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console_format = logging.Formatter("%(name)s [%(levelname)s] %(message)s")
        console.setFormatter(console_format)
        logger.addHandler(console)

        # Try to set up file handler if we have permissions
        try:
            # Get log file path from settings
            log_file_path = get_log_file_path()

            if log_file_path:
                file_handler = logging.FileHandler(log_file_path)
                file_handler.setLevel(logging.DEBUG)
                file_format = logging.Formatter(
                    "%(asctime)s %(name)s [%(levelname)s] %(message)s"
                )
                file_handler.setFormatter(file_format)
                logger.addHandler(file_handler)
                logger.info(f"File logging enabled: {log_file_path}")
            else:
                logger.warning(
                    "File logging disabled - no valid log file path configured"
                )

        except Exception as e:
            logger.error(f"Failed to set up file logging: {str(e)}")

    return logger


def get_log_file_path():
    """
    Get the log file path from plugin configuration or use sensible defaults.
    Returns None if no valid path can be determined.

    Priority order:
    1. PLUGINS_CONFIG["netbox_entraid_tools"]["log_file_path"]
    2. Automatic detection of writable directories
    """
    try:
        # Check plugin configuration (available during startup)
        from django.conf import settings

        if hasattr(settings, "PLUGINS_CONFIG"):
            plugin_config = settings.PLUGINS_CONFIG.get("netbox_entraid_tools", {})
            config_path = plugin_config.get("log_file_path", "").strip()
            if config_path:
                # Validate the directory exists and is writable
                log_dir = os.path.dirname(config_path)
                if log_dir and os.path.exists(log_dir) and os.access(log_dir, os.W_OK):
                    return config_path
                elif not log_dir:  # filename only, use current directory
                    return config_path

        # Fall back to system defaults
        possible_dirs = [
            "/static/log/netbox",  # Custom log directory (separate disk)
            "/var/log/netbox",  # Standard NetBox log directory
            "/opt/netbox/logs",  # Alternative NetBox log directory
            "/tmp",  # Temporary directory (usually writable)
            ".",  # Current working directory (last resort)
        ]

        for log_dir in possible_dirs:
            if os.path.exists(log_dir) and os.access(log_dir, os.W_OK):
                return os.path.join(log_dir, "netbox_entraid_tools.log")

        # If all else fails, return None to disable file logging
        return None

    except Exception:
        # If there's any error, return None to disable file logging
        return None


# NetBox-native contact payload builder from EntraID user dict
def contact_payload_from_user(user):
    """
    Build a dict of contact fields from an EntraID user object for NetBox ORM updates.
    """
    address_parts = [
        user.get("streetAddress", ""),
        user.get("city", ""),
        user.get("state", ""),
        user.get("postalCode", ""),
        user.get("country", ""),
    ]
    address = "\n".join([part for part in address_parts if part])

    object_id = user.get("id", "")
    link = (
        f"https://entra.microsoft.com/#view/Microsoft_AAD_UsersAndTenants/UserProfileMenuBlade/~/overview/userId/{object_id}/hidePreviewBanner~/true"
        if object_id
        else ""
    )
    email = (user.get("mail") or user.get("userPrincipalName", "")).lower()

    payload = {
        "name": user.get("displayName", ""),
        "title": user.get("jobTitle", ""),
        "phone": user.get("mobilePhone", ""),
        "email": email,
        "address": address,
        "link": link,
        "description": user.get("department", ""),
        "entra_oid": object_id,
    }
    # Remove empty fields
    payload = {k: v for k, v in payload.items() if v not in (None, "", [])}
    return payload

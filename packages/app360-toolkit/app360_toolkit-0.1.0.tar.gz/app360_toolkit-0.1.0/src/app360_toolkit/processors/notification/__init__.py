"""Notification processors - Auto-discovered from local settings."""

from ...core.registry import registry

# Auto-load this specific module
registry.load_all()

# Get components for this module
_notification_classes = registry.get_processor_module('notification')

# Make available in this module
locals().update(_notification_classes)

# Dynamic __all__
__all__ = list(_notification_classes.keys())

__doc__ = f"""
Notification Processors

Available: {', '.join(__all__)}

Auto-discovered from local settings.py
"""
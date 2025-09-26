"""
Factory configuration.

This file defines all factory classes available in the toolkit.
"""

# =============================================================================
# FACTORIES CONFIGURATION
# =============================================================================

FACTORIES = {
    'DocumentFactory': {
        'class': 'DocumentFactory',
        'module': 'factories.document_factory',
        'description': 'Factory for creating document processors',
        'enabled': True,
    },
    'NotificationFactory': {
        'class': 'NotificationFactory', 
        'module': 'factories.notification_factory',
        'description': 'Factory for creating notification processors',
        'enabled': False,
    },
    'ValidationFactory': {
        'class': 'ValidationFactory',
        'module': 'factories.validation_factory', 
        'description': 'Factory for creating validation utilities',
        'enabled': False,  # Futuro
    },
}

# =============================================================================
# LOCAL SETTINGS
# =============================================================================

LOCAL_CONFIG = {
    'auto_register': True,
    'lazy_instantiation': True,
    'cache_instances': False,
}
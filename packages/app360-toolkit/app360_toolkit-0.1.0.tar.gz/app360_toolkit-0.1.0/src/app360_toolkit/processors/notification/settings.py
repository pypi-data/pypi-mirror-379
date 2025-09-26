"""
Notification processor configuration.

This file defines all notification processors available in this module.
"""

# =============================================================================
# MODULE CONFIGURATION
# =============================================================================

# Habilitar/desabilitar este módulo inteiro
ENABLED = False

# =============================================================================
# COMPONENTS CONFIGURATION
# =============================================================================

COMPONENTS = {
    'Email': {
        'class': 'EmailProcessor',
        'file': 'email',
        'description': 'Email notification processor',
        'enabled': False,
    },
    'SMS': {
        'class': 'SMSProcessor',
        'file': 'sms', 
        'description': 'SMS notification processor',
        'enabled': False,  # Ainda não implementado
    },
    'Push': {
        'class': 'PushProcessor',
        'file': 'push',
        'description': 'Push notification processor',
        'enabled': False,  # Futuro
    },
    'Webhook': {
        'class': 'WebhookProcessor', 
        'file': 'webhook',
        'description': 'Webhook notification processor',
        'enabled': False,  # Futuro
    },
}

# =============================================================================
# VIRTUAL MODULE CONFIGURATION
# =============================================================================

VIRTUAL_MODULE = {
    'exports': [name for name, config in COMPONENTS.items() 
               if config.get('enabled', True)],
    'description': 'Notification sending and management',
}

# =============================================================================
# LOCAL SETTINGS
# =============================================================================

LOCAL_CONFIG = {
    'default_timeout': 30,
    'retry_attempts': 3,
    'async_mode': True,
}
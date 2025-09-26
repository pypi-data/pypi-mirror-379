"""
Document processor configuration.

This file defines all document processors available in this module.
"""

# =============================================================================
# MODULE CONFIGURATION
# =============================================================================

# Habilitar/desabilitar este módulo inteiro
ENABLED = True

# =============================================================================
# COMPONENTS CONFIGURATION
# =============================================================================

COMPONENTS = {
    'CPF': {
        'class': 'CPF',
        'file': 'cpf',
        'description': 'Brazilian CPF document processor',
        'enabled': True,
    },
    'CNPJ': {
        'class': 'CNPJ', 
        'file': 'cnpj',
        'description': 'Brazilian CNPJ document processor',
        'enabled': False,
    },
    'RG': {
        'class': 'RG',
        'file': 'rg',
        'description': 'Brazilian RG document processor', 
        'enabled': False,  # Ainda não implementado
    },
    'PIS': {
        'class': 'PIS',
        'file': 'pis',
        'description': 'Brazilian PIS document processor',
        'enabled': False,  # Futuro
    },
}

# =============================================================================
# VIRTUAL MODULE CONFIGURATION
# =============================================================================

VIRTUAL_MODULE = {
    'exports': [name for name, config in COMPONENTS.items() 
               if config.get('enabled', True)],
    'description': 'Brazilian document validation and formatting',
}

# =============================================================================
# LOCAL SETTINGS
# =============================================================================

LOCAL_CONFIG = {
    'auto_format': True,
    'strict_validation': True,
    'cache_results': False,
}
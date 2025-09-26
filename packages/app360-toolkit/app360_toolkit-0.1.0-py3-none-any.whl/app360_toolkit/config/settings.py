"""
Global configuration aggregator for app360-toolkit.

This file automatically discovers and aggregates all local settings
from processors, factories, and other modules.
"""

import importlib
from typing import Dict, Any, List


# =============================================================================
# MODULE DISCOVERY CONFIGURATION
# =============================================================================

# Lista simples dos módulos processors disponíveis
PROCESSOR_MODULES = [
    'document',
    'notification',
    # Adicione novos módulos aqui
]

# Lista simples dos módulos factories disponíveis  
FACTORY_MODULES = [
    'factories',
    # Adicione novos módulos aqui se necessário
]

# =============================================================================
# GLOBAL SETTINGS
# =============================================================================

GLOBAL_CONFIG = {
    'auto_discovery': True,
    'lazy_loading': True,
    'cache_imports': True,
    'debug_imports': False,
}


# =============================================================================
# AGGREGATION FUNCTIONS
# =============================================================================

def _load_processor_settings(module_name: str) -> Dict[str, Any]:
    """Load settings from a processor module."""
    try:
        settings_module = importlib.import_module(f'app360_toolkit.processors.{module_name}.settings')
        return {
            'enabled': getattr(settings_module, 'ENABLED', True),
            'module': f'processors.{module_name}',
            'components': getattr(settings_module, 'COMPONENTS', {}),
            'virtual_module': getattr(settings_module, 'VIRTUAL_MODULE', {}),
        }
    except ImportError as e:
        if GLOBAL_CONFIG.get('debug_imports', False):
            print(f"Warning: Could not load settings for processor {module_name}: {e}")
        return {}


def _load_factory_settings() -> Dict[str, Any]:
    """Load settings from factories module."""
    try:
        settings_module = importlib.import_module('app360_toolkit.factories.settings')
        return getattr(settings_module, 'FACTORIES', {})
    except ImportError as e:
        if GLOBAL_CONFIG.get('debug_imports', False):
            print(f"Warning: Could not load factory settings: {e}")
        return {}


def get_aggregated_processors() -> Dict[str, Dict[str, Any]]:
    """Aggregate all processor settings."""
    aggregated = {}
    
    for module_name in PROCESSOR_MODULES:
        module_settings = _load_processor_settings(module_name)
        if module_settings:
            aggregated[module_name] = module_settings
    
    return aggregated


def get_aggregated_factories() -> Dict[str, Any]:
    """Aggregate all factory settings."""
    return _load_factory_settings()


def get_aggregated_virtual_modules() -> Dict[str, Dict[str, Any]]:
    """Aggregate all virtual module configurations."""
    virtual_modules = {}
    
    for module_name in PROCESSOR_MODULES:
        module_settings = _load_processor_settings(module_name)
        if module_settings and 'virtual_module' in module_settings:
            virtual_config = module_settings['virtual_module']
            if virtual_config:
                virtual_modules[module_name] = {
                    'source': f'processors.{module_name}',
                    'exports': virtual_config.get('exports', []),
                }
    
    return virtual_modules


# =============================================================================
# DYNAMIC AGGREGATION (Lazy Loading)
# =============================================================================

# Estas variáveis são carregadas dinamicamente quando necessário
_processors_cache = None
_factories_cache = None
_virtual_modules_cache = None


def get_processors() -> Dict[str, Dict[str, Any]]:
    """Get aggregated processors (cached)."""
    global _processors_cache
    if _processors_cache is None or not GLOBAL_CONFIG.get('cache_imports', True):
        _processors_cache = get_aggregated_processors()
    return _processors_cache


def get_factories() -> Dict[str, Any]:
    """Get aggregated factories (cached)."""
    global _factories_cache
    if _factories_cache is None or not GLOBAL_CONFIG.get('cache_imports', True):
        _factories_cache = get_aggregated_factories()
    return _factories_cache


def get_virtual_modules() -> Dict[str, Dict[str, Any]]:
    """Get aggregated virtual modules (cached)."""
    global _virtual_modules_cache
    if _virtual_modules_cache is None or not GLOBAL_CONFIG.get('cache_imports', True):
        _virtual_modules_cache = get_aggregated_virtual_modules()
    return _virtual_modules_cache


# =============================================================================
# COMPATIBILITY (for existing code)
# =============================================================================

# Para compatibilidade com código existente, criamos propriedades dinâmicas
@property
def PROCESSORS():
    return get_processors()

@property  
def FACTORIES():
    return get_factories()

@property
def VIRTUAL_MODULES():
    return get_virtual_modules()
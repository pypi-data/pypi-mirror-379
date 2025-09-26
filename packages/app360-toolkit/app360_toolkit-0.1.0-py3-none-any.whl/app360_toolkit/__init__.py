"""
app360-toolkit: Comprehensive Python toolkit.

Auto-discovers ALL components from distributed configuration files.
"""

__version__ = "0.1.0"
__author__ = "Sergius Fortuna"
__email__ = "sfortuna1977@gmail.com"
__license__ = "MIT"

from .core.registry import registry
from .config.settings import get_virtual_modules
import sys
from types import ModuleType

# Load ALL components from distributed settings
registry.load_all()

# Create virtual modules dynamically based on distributed config
virtual_modules_config = get_virtual_modules()

for virtual_name, virtual_config in virtual_modules_config.items():
    # Create virtual module
    module = ModuleType(virtual_name)
    
    # Get components from the processor module
    components = registry.get_processor_module(virtual_name)
    
    # Add components to virtual module
    for component_name, component_class in components.items():
        setattr(module, component_name, component_class)
    
    # Add metadata
    module.__doc__ = f"""
{virtual_config.get('description', f'{virtual_name.title()} processors')}

Available components: {', '.join(components.keys())}
"""
    
    # Register virtual module
    sys.modules[f'{__name__}.{virtual_name}'] = module

# Make all components available at package level
all_components = registry.get_all_components_flat()
all_factories = registry.all_factories

# Add to module namespace
locals().update(all_components)
locals().update(all_factories)

# Dynamic __all__
__all__ = (
    list(virtual_modules_config.keys()) +  # Virtual modules
    list(all_components.keys()) +          # All processor components
    list(all_factories.keys())             # All factories
)

__doc__ = f"""
app360-toolkit: Comprehensive Python toolkit

Available virtual modules: {', '.join(virtual_modules_config.keys())}
Available components: {', '.join(all_components.keys())}
Available factories: {', '.join(all_factories.keys())}

Examples:
    # Via virtual modules
    >>> from app360_toolkit.document import CPF, CNPJ
    >>> from app360_toolkit.notification import Email
    
    # Direct import
    >>> from app360_toolkit import CPF, DocumentFactory
    
    # Factory usage
    >>> factory = DocumentFactory()
    >>> cpf = factory.create_cpf("12345678909")
"""
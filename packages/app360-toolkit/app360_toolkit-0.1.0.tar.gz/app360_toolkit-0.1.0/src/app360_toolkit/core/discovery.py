"""
Universal auto-discovery engine.

This module can discover and load ANY component type based on 
distributed configuration files.
"""

import importlib
from typing import Dict, Any, List, Optional
from ..config.settings import get_processors, get_factories, get_virtual_modules, GLOBAL_CONFIG


class UniversalDiscovery:
    """Universal component discovery engine."""
    
    def __init__(self, base_package: str = 'app360_toolkit'):
        self.base_package = base_package
        self._cache = {}
    
    def discover_processors(self) -> Dict[str, Dict[str, Any]]:
        """Discover all processor modules and their components."""
        all_processors = {}
        processors_config = get_processors()
        
        for module_name, module_config in processors_config.items():
            if not module_config.get('enabled', True):
                continue
                
            processors = self._load_processor_module(module_name, module_config)
            if processors:
                all_processors[module_name] = processors
                
        return all_processors
    
    def discover_factories(self) -> Dict[str, Any]:
        """Discover all factory classes."""
        factories = {}
        factories_config = get_factories()
        
        for factory_name, factory_config in factories_config.items():
            if not factory_config.get('enabled', True):
                continue
                
            factory_class = self._load_factory(factory_name, factory_config)
            if factory_class:
                factories[factory_name] = factory_class
                
        return factories
    
    def _load_processor_module(self, module_name: str, module_config: Dict) -> Optional[Dict[str, Any]]:
        """Load a specific processor module."""
        try:
            components = {}
            module_path = module_config['module']
            
            for component_name, component_config in module_config['components'].items():
                if not component_config.get('enabled', True):
                    continue
                    
                # Build full import path
                file_name = component_config['file']
                class_name = component_config['class']
                full_path = f"{self.base_package}.{module_path}.{file_name}"
                
                # Import and get class
                module = importlib.import_module(full_path)
                component_class = getattr(module, class_name)
                
                components[component_name] = component_class
                
            return components
            
        except (ImportError, AttributeError) as e:
            if GLOBAL_CONFIG.get('debug_imports', False):
                print(f"Warning: Could not load processor module {module_name}: {e}")
            return None
    
    def _load_factory(self, factory_name: str, factory_config: Dict) -> Optional[Any]:
        """Load a specific factory class."""
        try:
            module_path = factory_config['module']
            class_name = factory_config['class']
            full_path = f"{self.base_package}.{module_path}"
            
            module = importlib.import_module(full_path)
            factory_class = getattr(module, class_name)
            
            return factory_class
            
        except (ImportError, AttributeError) as e:
            if GLOBAL_CONFIG.get('debug_imports', False):
                print(f"Warning: Could not load factory {factory_name}: {e}")
            return None
    
    def get_virtual_module_config(self, module_name: str) -> Optional[Dict]:
        """Get configuration for a virtual module."""
        virtual_modules = get_virtual_modules()
        return virtual_modules.get(module_name)
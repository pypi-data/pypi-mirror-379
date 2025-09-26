"""
Global registry for ALL toolkit components.
"""

from .discovery import UniversalDiscovery
from typing import Dict, Any, List, Optional
from ..config.settings import GLOBAL_CONFIG, get_virtual_modules


class GlobalRegistry:
    """Global registry for all toolkit components."""
    
    def __init__(self):
        self.discovery = UniversalDiscovery()
        self._processors = {}
        self._factories = {}
        self._loaded = False
    
    def load_all(self):
        """Load ALL components from distributed configuration."""
        if self._loaded and GLOBAL_CONFIG.get('cache_imports', True):
            return
            
        # Discover all processors from their local settings
        self._processors = self.discovery.discover_processors()
        
        # Discover all factories from their local settings
        self._factories = self.discovery.discover_factories()
        
        self._loaded = True
        
        if GLOBAL_CONFIG.get('debug_imports', False):
            print(f"Loaded processors: {list(self._processors.keys())}")
            print(f"Loaded factories: {list(self._factories.keys())}")
    
    @property
    def all_processors(self) -> Dict[str, Dict[str, Any]]:
        """Get all processor modules."""
        if not self._loaded:
            self.load_all()
        return self._processors
    
    @property
    def all_factories(self) -> Dict[str, Any]:
        """Get all factories."""
        if not self._loaded:
            self.load_all()
        return self._factories
    
    def get_processor_module(self, module_name: str) -> Dict[str, Any]:
        """Get specific processor module."""
        return self.all_processors.get(module_name, {})
    
    def get_all_components_flat(self) -> Dict[str, Any]:
        """Get all components in a flat dictionary."""
        flat = {}
        for module_processors in self.all_processors.values():
            flat.update(module_processors)
        return flat
    
    def get_virtual_modules_info(self) -> Dict[str, Dict[str, Any]]:
        """Get virtual modules configuration."""
        return get_virtual_modules()


# Global registry instance
registry = GlobalRegistry()
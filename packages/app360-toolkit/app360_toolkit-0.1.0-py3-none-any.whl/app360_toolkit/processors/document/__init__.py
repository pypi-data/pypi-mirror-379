"""Document processors - Auto-discovered from local settings."""

from ...core.registry import registry

# Auto-load this specific module
registry.load_all()

# Get components for this module
_document_classes = registry.get_processor_module('document')

# Make available in this module
locals().update(_document_classes)

# Dynamic __all__
__all__ = list(_document_classes.keys())

__doc__ = f"""
Document Processors

Available: {', '.join(__all__)}

Auto-discovered from local settings.py
"""
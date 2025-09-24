"""
FSSG Error classes
"""


class FSSSGError(Exception):
    """Base FSSG error."""
    pass


class ConfigError(FSSSGError):
    """Configuration error."""
    pass


class RenderError(FSSSGError):
    """Rendering error."""
    pass


class ValidationError(FSSSGError):
    """Content validation error."""
    pass
"""
FSSG Configuration management

Handles loading and validation of fssg.config.json
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class FSSSGConfig:
    """FSSG Configuration."""

    # Site settings
    canonical_url: str = "https://example.com"
    lang_default: str = "en"
    timezone: str = "UTC"

    # Paths
    content_dir: str = "./content"
    layouts_dir: str = "./layouts"
    components_dir: str = "./components"
    theme_dir: str = "./theme"
    public_dir: str = "./public"
    output_dir: str = "./dist"

    # Build settings
    targets: list = None
    css_strategy: str = "vanilla"

    def __post_init__(self):
        if self.targets is None:
            self.targets = ["html"]

    @classmethod
    def from_file(cls, config_path: Path) -> 'FSSSGConfig':
        """Load configuration from JSON file."""
        if not config_path.exists():
            return cls()

        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FSSSGConfig':
        """Create config from dictionary."""
        config = cls()

        # Site settings
        if 'site' in data:
            site = data['site']
            config.canonical_url = site.get('canonical', config.canonical_url)
            config.lang_default = site.get('langDefault', config.lang_default)
            config.timezone = site.get('timezone', config.timezone)

        # Paths
        if 'paths' in data:
            paths = data['paths']
            config.content_dir = paths.get('content', config.content_dir)
            config.layouts_dir = paths.get('layouts', config.layouts_dir)
            config.components_dir = paths.get('components', config.components_dir)
            config.theme_dir = paths.get('theme', config.theme_dir)
            config.public_dir = paths.get('public', config.public_dir)
            config.output_dir = paths.get('output', config.output_dir)

        # Render settings
        if 'render' in data:
            render = data['render']
            config.targets = render.get('targets', config.targets)

        # CSS settings
        if 'css' in data:
            css = data['css']
            config.css_strategy = css.get('strategy', config.css_strategy)

        return config

    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return {
            'site': {
                'canonical': self.canonical_url,
                'langDefault': self.lang_default,
                'timezone': self.timezone
            },
            'paths': {
                'content': self.content_dir,
                'layouts': self.layouts_dir,
                'components': self.components_dir,
                'theme': self.theme_dir,
                'public': self.public_dir,
                'output': self.output_dir
            },
            'render': {
                'targets': self.targets
            },
            'css': {
                'strategy': self.css_strategy
            }
        }
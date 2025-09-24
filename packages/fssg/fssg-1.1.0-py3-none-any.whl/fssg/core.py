"""
FSSG Core - Main processing engine

Handles the complete pipeline:
1. Parse FACET files to canonical JSON
2. Validate web contracts
3. Build routing and redirects
4. Render to HTML
5. Optimize and emit assets
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
import subprocess

# Import FACET parser
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "FACET" / "facet-lang"))
try:
    from facet_lang.canon import canonize
    from facet_lang.errors import FacetError
except ImportError as e:
    raise ImportError(f"Cannot import FACET parser: {e}. Make sure FACET is properly installed.")

from .config import FSSSGConfig
from .renderer import HTMLRenderer
from .errors import FSSSGError


class FSSSGCore:
    """Main FSSG processing engine."""

    def __init__(self, config: FSSSGConfig):
        self.config = config
        self.renderer = HTMLRenderer(config)
        self.site_data = {}
        self.pages = {}

    def parse_facet_file(self, file_path: Path, host_vars: Optional[Dict] = None) -> Dict[str, Any]:
        """Parse a single FACET file to canonical JSON."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            result = canonize(
                content,
                host_vars=host_vars or {},
                resolve_mode='all',  # This should enable @vars resolution
                import_roots=[str(self.config.content_dir)],
                strict_merge=True,
                current_file=str(file_path)
            )

            return result

        except FacetError as e:
            raise FSSSGError(f"FACET parsing error in {file_path}: {e}")
        except Exception as e:
            print(f"Debug: Full error for {file_path}: {e}")
            print(f"Debug: Error type: {type(e)}")
            raise FSSSGError(f"Error processing {file_path}: {e}")

    def discover_content(self) -> List[Path]:
        """Discover all FACET files in content directory."""
        content_dir = Path(self.config.content_dir)
        if not content_dir.exists():
            raise FSSSGError(f"Content directory not found: {content_dir}")

        facet_files = []
        for pattern in ["**/*.facet"]:
            facet_files.extend(content_dir.glob(pattern))

        return facet_files

    def load_site_config(self):
        """Load site.facet configuration."""
        site_file = Path(self.config.content_dir) / "site.facet"
        if site_file.exists():
            self.site_data = self.parse_facet_file(site_file)
        else:
            self.site_data = {}

    def build_pages(self, facet_files: List[Path]):
        """Process all FACET files into pages."""
        for file_path in facet_files:
            if file_path.name == "site.facet":
                continue  # Already processed

            try:
                page_data = self.parse_facet_file(file_path)

                # Extract route from file path or meta.slug
                route = self._determine_route(file_path, page_data)

                self.pages[route] = {
                    'data': page_data,
                    'source_file': file_path,
                    'route': route
                }

            except Exception as e:
                print(f"Warning: Failed to process {file_path}: {e}")

    def _determine_route(self, file_path: Path, page_data: Dict) -> str:
        """Determine the route for a page."""
        # Try to get slug from @meta
        if 'meta' in page_data and 'slug' in page_data['meta']:
            slug = page_data['meta']['slug']
            if slug.startswith('/'):
                return slug
            return f"/{slug}"

        # Fall back to file path
        content_dir = Path(self.config.content_dir)
        relative_path = file_path.relative_to(content_dir)

        # Remove .facet extension and convert to route
        route_parts = relative_path.with_suffix('').parts

        if route_parts[-1] == 'index':
            route_parts = route_parts[:-1]

        route = '/' + '/'.join(route_parts) if route_parts else '/'
        return route

    def build(self):
        """Execute the complete build pipeline."""
        print("🚀 Starting FSSG build...")

        # 1. Load site configuration
        print("📋 Loading site configuration...")
        self.load_site_config()

        # 2. Discover content files
        print("🔍 Discovering content files...")
        facet_files = self.discover_content()
        print(f"   Found {len(facet_files)} FACET files")

        # 3. Process pages
        print("⚙️ Processing pages...")
        self.build_pages(facet_files)
        print(f"   Processed {len(self.pages)} pages")

        # 4. Render to HTML
        print("🎨 Rendering HTML...")
        self.render_all_pages()

        # 5. Copy static assets
        print("📁 Copying assets...")
        self.copy_static_assets()

        print("✅ Build complete!")

    def render_all_pages(self):
        """Render all pages to HTML."""
        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(exist_ok=True)

        for route, page in self.pages.items():
            html_content = self.renderer.render_page(page['data'], self.site_data)

            # Determine output file path
            if route == '/':
                output_file = output_dir / "index.html"
            else:
                # Create directory structure
                page_dir = output_dir / route.strip('/')
                page_dir.mkdir(parents=True, exist_ok=True)
                output_file = page_dir / "index.html"

            # Write HTML file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            print(f"   📄 {route} → {output_file}")

    def copy_static_assets(self):
        """Copy static assets to output directory."""
        public_dir = Path(self.config.public_dir)
        output_dir = Path(self.config.output_dir)

        if not public_dir.exists():
            return

        # Simple copy - can be enhanced with optimization later
        import shutil

        for item in public_dir.iterdir():
            if item.is_file():
                shutil.copy2(item, output_dir / item.name)
            elif item.is_dir():
                shutil.copytree(item, output_dir / item.name, dirs_exist_ok=True)

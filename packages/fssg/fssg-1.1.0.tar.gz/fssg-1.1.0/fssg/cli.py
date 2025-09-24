"""
FSSG CLI - Command Line Interface

Provides commands: init, build, dev, lint
"""

import click
import json
import shutil
import sys
from pathlib import Path
from typing import Optional

from .config import FSSSGConfig
from .core import FSSSGCore
from .errors import FSSSGError


@click.group()
@click.version_option(version="1.1.0")
def main():
    """FSSG - FACET Static Site Generator

    A production-grade static site generator built on deterministic principles.
    Uses FACET v1.1 as the source format and generates optimized HTML.
    """
    pass


@main.command()
@click.argument('project_name', required=False)
@click.option('--theme', default='retro', help='Theme to use (default: retro)')
def init(project_name: Optional[str], theme: str):
    """Initialize a new FSSG project."""
    if not project_name:
        project_name = 'my-site'

    project_dir = Path(project_name)

    if project_dir.exists():
        click.echo(f"Error: Directory '{project_name}' already exists", err=True)
        sys.exit(1)

    click.echo(f"🚀 Creating new FSSG project: {project_name}")

    # Create project structure
    project_dir.mkdir()
    (project_dir / 'content').mkdir()
    (project_dir / 'layouts').mkdir()
    (project_dir / 'components').mkdir()
    (project_dir / 'theme').mkdir()
    (project_dir / 'public').mkdir()

    # Create fssg.config.json
    config = FSSSGConfig()
    config_data = config.to_dict()

    with open(project_dir / 'fssg.config.json', 'w') as f:
        json.dump(config_data, f, indent=2)

    # Create site.facet
    site_content = '''@site

@meta
  title: "My FSSG Site"
  description: "A site built with FSSG and FACET"
  author: "Your Name"

@config
  nav:
    - { title: "Home", href: "/" }
    - { title: "About", href: "/about" }'''

    with open(project_dir / 'content' / 'site.facet', 'w') as f:
        f.write(site_content)

    # Create index page
    index_content = '''@page(type="page", layout="default")

@meta
  title: "Welcome to FSSG"
  description: "Your new FSSG site is ready!"
  slug: ""

@vars
  site_name: "My FSSG Site"
  features:
    - "Deterministic builds"
    - "FACET-powered content"
    - "Retro aesthetic"
    - "Zero JS by default"

@body
  @h1 "{{site_name}} █"

  @p """
    Welcome to your new FSSG site! This site is built with FACET v1.1
    and follows deterministic generation principles.
  """

  @div(class="retro-border")
    @h2 "Features"
    @ul
      - "Deterministic builds" (if="features")
      - "FACET-powered content" (if="features")
      - "Retro aesthetic" (if="features")
      - "Zero JS by default" (if="features")

  @p """
    Edit this file at content/index.facet to customize your homepage.
    Run 'fssg build' to generate your site.
  """'''

    with open(project_dir / 'content' / 'index.facet', 'w') as f:
        f.write(index_content)

    # Create about page
    about_content = '''@page(type="page", layout="default")

@meta
  title: "About"
  description: "About this FSSG site"
  slug: "about"

@body
  @h1 "About This Site █"

  @p """
    This site was generated using FSSG (FACET Static Site Generator).
    FSSG follows the principle of deterministic generation - the same
    input always produces the same output.
  """

  @h2 "Technology Stack"

  @ul
    - "FACET v1.1 - Source format"
    - "FSSG - Static site generator"
    - "HTML5 - Output format"
    - "Zero JavaScript by default"'''

    with open(project_dir / 'content' / 'about.facet', 'w') as f:
        f.write(about_content)

    # Create README
    readme_content = f'''# {project_name}

This is an FSSG (FACET Static Site Generator) project.

## Getting Started

1. Install FSSG:
   ```
   pip install -e path/to/fssg
   ```

2. Build your site:
   ```
   fssg build
   ```

3. Preview your site:
   ```
   cd dist && python -m http.server 8000
   ```

## Project Structure

- `content/` - FACET source files
- `public/` - Static assets
- `fssg.config.json` - Site configuration
- `dist/` - Generated output (created after build)

## Commands

- `fssg build` - Build the site
- `fssg dev` - Start development server (coming soon)
- `fssg lint` - Validate FACET files

## Learn More

- [FACET Language Specification](https://github.com/rokoss21/FACET)
- [FSSG Documentation](https://github.com/rokoss21/fssg)
'''

    with open(project_dir / 'README.md', 'w') as f:
        f.write(readme_content)

    click.echo(f"✅ Project created successfully!")
    click.echo(f"")
    click.echo(f"Next steps:")
    click.echo(f"  cd {project_name}")
    click.echo(f"  fssg build")
    click.echo(f"  cd dist && python -m http.server 8000")


@main.command()
@click.option('--config', '-c', default='fssg.config.json', help='Config file path')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def build(config: str, verbose: bool):
    """Build the site from FACET files."""
    config_path = Path(config)

    try:
        # Load configuration
        fssg_config = FSSSGConfig.from_file(config_path)

        # Initialize FSSG core
        core = FSSSGCore(fssg_config)

        # Execute build
        core.build()

        click.echo("🎉 Build completed successfully!")

    except FSSSGError as e:
        click.echo(f"❌ Build failed: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"💥 Unexpected error: {e}", err=True)
        sys.exit(1)


@main.command()
@click.option('--config', '-c', default='fssg.config.json', help='Config file path')
@click.option('--port', '-p', default=8000, help='Development server port')
def dev(config: str, port: int):
    """Start development server with auto-rebuild."""
    click.echo("🚧 Development server is coming soon!")
    click.echo("For now, use: fssg build && cd dist && python -m http.server 8000")


@main.command()
@click.option('--config', '-c', default='fssg.config.json', help='Config file path')
def lint(config: str):
    """Validate FACET files."""
    click.echo("🔍 Linting FACET files...")

    config_path = Path(config)

    try:
        fssg_config = FSSSGConfig.from_file(config_path)
        core = FSSSGCore(fssg_config)

        # Discover and validate files
        facet_files = core.discover_content()

        errors = 0
        for file_path in facet_files:
            try:
                core.parse_facet_file(file_path)
                click.echo(f"✅ {file_path}")
            except Exception as e:
                click.echo(f"❌ {file_path}: {e}", err=True)
                errors += 1

        if errors == 0:
            click.echo("🎉 All files are valid!")
        else:
            click.echo(f"💥 {errors} file(s) have errors")
            sys.exit(1)

    except Exception as e:
        click.echo(f"❌ Lint failed: {e}", err=True)
        sys.exit(1)


@main.command()
def version():
    """Show FSSG version information."""
    click.echo("FSSG (FACET Static Site Generator) v1.1.0")
    click.echo("Built on FACET v1.1 r3 specification")
    click.echo("Author: Emil Rokossovsky <ecsiar@gmail.com>")


if __name__ == '__main__':
    main()
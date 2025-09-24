"""
FSSG HTML Renderer

Converts canonical JSON from FACET to HTML output.
Supports the FACET Web DSL extensions.
"""

from typing import Dict, Any, List, Optional
from pathlib import Path
import html

from .config import FSSSGConfig
from .errors import RenderError


class HTMLRenderer:
    """Converts FACET JSON to HTML."""

    def __init__(self, config: FSSSGConfig):
        self.config = config

    def render_page(self, page_data: Dict[str, Any], site_data: Dict[str, Any]) -> str:
        """Render a complete page to HTML."""
        try:
            # Extract page metadata
            meta = page_data.get('meta', {})
            body = page_data.get('body', {})

            # Generate HTML document
            html_doc = self._render_html_document(meta, body, site_data)

            return html_doc

        except Exception as e:
            raise RenderError(f"Failed to render page: {e}")

    def _render_html_document(self, meta: Dict, body: Dict, site_data: Dict) -> str:
        """Render complete HTML document."""
        title = html.escape(meta.get('title', 'Untitled'))
        description = html.escape(meta.get('description', ''))
        lang = meta.get('lang', self.config.lang_default)

        # Build head section
        head_content = self._render_head(meta, site_data)

        # Build body content
        body_content = self._render_body_content(body)

        return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head_content}
</head>
<body>
{body_content}
</body>
</html>'''

    def _render_head(self, meta: Dict, site_data: Dict) -> str:
        """Render HTML head section."""
        lines = []

        # Basic meta
        lines.append(f'  <meta charset="utf-8">')
        lines.append(f'  <meta name="viewport" content="width=device-width, initial-scale=1">')

        title = html.escape(meta.get('title', 'Untitled'))
        lines.append(f'  <title>{title}</title>')

        if 'description' in meta:
            desc = html.escape(meta['description'])
            lines.append(f'  <meta name="description" content="{desc}">')

        # SEO meta tags
        if 'robots' in meta:
            lines.append(f'  <meta name="robots" content="{meta["robots"]}">')

        if 'author' in meta:
            author = html.escape(meta['author'])
            lines.append(f'  <meta name="author" content="{author}">')

        # OpenGraph
        if 'title' in meta:
            lines.append(f'  <meta property="og:title" content="{html.escape(meta["title"])}">')

        if 'description' in meta:
            lines.append(f'  <meta property="og:description" content="{html.escape(meta["description"])}">')

        lines.append(f'  <meta property="og:type" content="website">')

        # Canonical URL
        canonical = self.config.canonical_url
        if 'slug' in meta:
            slug = meta['slug'].lstrip('/')
            if slug:
                canonical = f"{canonical.rstrip('/')}/{slug}"
        lines.append(f'  <link rel="canonical" href="{canonical}">')

        # CSS
        lines.append(f'  <style>')
        lines.append(self._get_base_css())
        lines.append(self._get_interactive_css())
        lines.append(f'  </style>')

        return '\n'.join(lines)

    def _get_base_css(self) -> str:
        """Get base CSS styles."""
        return '''    /* FSSG Base Styles - Retro Theme */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
      background: #0a0a0a;
      color: #00ff00;
      line-height: 1.6;
      padding: 20px;
    }

    h1, h2, h3, h4, h5, h6 {
      color: #00ffff;
      margin: 20px 0 10px 0;
      text-shadow: 0 0 10px currentColor;
    }

    h1 {
      font-size: 2rem;
      border-bottom: 2px solid #00ffff;
      padding-bottom: 10px;
    }

    p {
      margin: 15px 0;
    }

    ul, ol {
      margin: 15px 0;
      padding-left: 30px;
    }

    li {
      margin: 5px 0;
    }

    a {
      color: #ff00ff;
      text-decoration: none;
      text-shadow: 0 0 5px currentColor;
    }

    a:hover {
      color: #ffffff;
      text-shadow: 0 0 10px #ff00ff;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
    }

    .retro-border {
      border: 2px solid #00ff00;
      padding: 20px;
      margin: 20px 0;
      background: rgba(0, 255, 0, 0.05);
    }

    /* Accessibility */
    :focus {
      outline: 2px solid #00ffff;
      outline-offset: 2px;
    }

    /* Print styles */
    @media print {
      body {
        background: white;
        color: black;
      }
      h1, h2, h3, h4, h5, h6 {
        color: black;
        text-shadow: none;
      }
      a {
        color: black;
        text-shadow: none;
      }
    }'''

    def _render_body_content(self, body: Dict) -> str:
        """Render body content from FACET body block."""
        if not body:
            return '<div class="container"><p>No content</p></div>'

        content_html = []
        content_html.append('<div class="container">')

        # Render body elements
        for key, value in body.items():
            element_html = self._render_element(key, value, 1)
            if element_html:
                content_html.append(element_html)

        content_html.append('</div>')

        # Add JavaScript islands at the end
        js_scripts = self._get_js_includes(body)
        content_html.extend(js_scripts)

        return '\n'.join(content_html)

    def _get_html_mapping(self):
        """HTML element mapping for FACET keys."""
        return {
            # Headers
            'h1': 'h1', 'h2': 'h2', 'h3': 'h3', 'h4': 'h4', 'h5': 'h5', 'h6': 'h6',
            'title': 'h1', 'headline': 'h1', 'header': 'h1',

            # Text elements
            'p': 'p', 'text': 'p', 'para': 'p', 'paragraph': 'p',
            'intro': 'p', 'description': 'p', 'summary': 'p',

            # Lists
            'ul': 'ul', 'ol': 'ol', 'list': 'ul', 'items': 'ul',
            'benefits': 'ul', 'features': 'ul', 'steps': 'ol',

            # Structural
            'div': 'div', 'section': 'section', 'article': 'article',
            'header': 'header', 'footer': 'footer', 'nav': 'nav',
            'content': 'div', 'container': 'div', 'wrapper': 'div',

            # Interactive
            'link': 'a', 'button': 'button', 'cta': 'a',

            # Media
            'img': 'img', 'image': 'img',

            # Special
            'separator': 'hr', 'hr': 'hr', 'break': 'hr',
            'code': 'code', 'pre': 'pre'
        }

    def _render_element(self, tag: str, content: Any, indent_level: int = 1) -> str:
        """Render a single FACET element to HTML."""
        indent = '  ' * indent_level
        html_mapping = self._get_html_mapping()

        # Remove @ prefix if present (shouldn't be in body content)
        clean_tag = tag[1:] if tag.startswith('@') else tag

        if isinstance(content, str):
            # Simple text element
            escaped_content = html.escape(content)

            # Remove terminal cursor symbol if present
            escaped_content = escaped_content.replace(' █', '')

            # Get HTML tag from mapping
            html_tag = html_mapping.get(clean_tag, 'div')

            if html_tag == 'hr':
                return f'{indent}<hr>'
            elif html_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
                return f'{indent}<{html_tag}>{escaped_content}</{html_tag}>'
            elif html_tag == 'a':
                # For links, content should be the text
                return f'{indent}<a href="#" class="{clean_tag}">{escaped_content}</a>'
            else:
                return f'{indent}<div class="{clean_tag}">{escaped_content}</div>'

        elif isinstance(content, bool):
            # Boolean values (like separator: true)
            if clean_tag in ['separator', 'hr'] and content:
                return f'{indent}<hr>'
            return f'{indent}<!-- {clean_tag}: {content} -->'

        elif isinstance(content, dict):
            # Complex element with nested content
            html_tag = html_mapping.get(clean_tag, 'div')

            # Special handling for interactive elements
            if 'href' in content and 'text' in content:
                href = html.escape(content['href'])
                text = html.escape(content['text'])
                css_class = f' class="{content.get("class", clean_tag)}"' if content.get('class') else ''
                return f'{indent}<a href="{href}"{css_class}>{text}</a>'

            # Special handling for buttons with ID
            if 'id' in content and 'text' in content:
                button_id = html.escape(content['id'])
                text = html.escape(content['text'])
                css_class = f' class="{content.get("class", "btn")}"' if content.get('class') else ' class="btn"'
                return f'{indent}<button id="{button_id}"{css_class}>{text}</button>'

            # Special handling for text inputs/editors
            if 'id' in content and ('content' in content or 'placeholder' in content):
                element_id = html.escape(content['id'])
                css_class = f' class="{content.get("class", clean_tag)}"' if content.get('class') else ''

                if 'content' in content:
                    # Code editor (textarea)
                    text_content = html.escape(str(content['content']))
                    return f'{indent}<textarea id="{element_id}"{css_class} rows="10" cols="50">{text_content}</textarea>'
                else:
                    # Output div
                    placeholder = html.escape(content.get('placeholder', ''))
                    return f'{indent}<div id="{element_id}"{css_class}>{placeholder}</div>'

            # Render nested content
            nested_html = []
            for key, value in content.items():
                if key not in ['class', 'href', 'text', 'id', 'content', 'placeholder']:  # Skip attributes
                    nested_html.append(self._render_element(key, value, indent_level + 1))

            if nested_html:
                nested_content = '\n' + '\n'.join(nested_html) + '\n' + indent
                css_class = f' class="{clean_tag}"' if html_tag == 'div' else ''
                return f'{indent}<{html_tag}{css_class}>{nested_content}</{html_tag}>'
            else:
                # Empty container or special element
                css_class = f' class="{clean_tag}"' if html_tag == 'div' else ''
                return f'{indent}<{html_tag}{css_class}></{html_tag}>'

        elif isinstance(content, list):
            # List of items
            html_tag = html_mapping.get(clean_tag, 'ul')

            if html_tag in ['ul', 'ol']:
                items = []
                for item in content:
                    if isinstance(item, str):
                        items.append(f'{indent}  <li>{html.escape(item)}</li>')
                    elif isinstance(item, dict):
                        # Complex list item
                        items.append(f'{indent}  <li>')
                        for sub_key, sub_value in item.items():
                            items.append(self._render_element(sub_key, sub_value, indent_level + 2))
                        items.append(f'{indent}  </li>')

                if items:
                    items_content = '\n' + '\n'.join(items) + '\n' + indent
                    return f'{indent}<{html_tag}>{items_content}</{html_tag}>'
                else:
                    return f'{indent}<{html_tag}></{html_tag}>'
            else:
                # Generic list container
                items = []
                for item in content:
                    if isinstance(item, str):
                        items.append(f'{indent}  <div class="item">{html.escape(item)}</div>')

                if items:
                    items_content = '\n' + '\n'.join(items) + '\n' + indent
                    return f'{indent}<div class="{clean_tag}">{items_content}</div>'

        return f'{indent}<!-- Unknown element: {clean_tag} ({type(content).__name__}) -->'

    def _get_interactive_css(self) -> str:
        """Get CSS for interactive elements."""
        return '''
    /* Interactive Elements */
    button, .btn-primary, .btn-secondary {
      background: transparent;
      border: 2px solid #00ffff;
      color: #00ffff;
      padding: 12px 24px;
      font-family: inherit;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      display: inline-block;
      margin: 10px;
    }

    button:hover, .btn-primary:hover, .btn-secondary:hover {
      background: rgba(0, 255, 255, 0.1);
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
    }

    .btn-secondary {
      border-color: #ff00ff;
      color: #ff00ff;
    }

    .btn-secondary:hover {
      background: rgba(255, 0, 255, 0.1);
      box-shadow: 0 5px 15px rgba(255, 0, 255, 0.3);
    }

    /* Code Editor Styles */
    .code-editor {
      background: #111;
      border: 2px solid #333;
      color: #00ff00;
      font-family: 'Monaco', 'Menlo', monospace;
      font-size: 14px;
      width: 100%;
      padding: 15px;
      margin: 10px 0;
      resize: vertical;
      min-height: 200px;
    }

    .json-output {
      background: #0a0a0a;
      border: 2px solid #333;
      color: #00ff00;
      font-family: 'Monaco', 'Menlo', monospace;
      font-size: 14px;
      padding: 15px;
      margin: 10px 0;
      min-height: 200px;
      white-space: pre-wrap;
      overflow-x: auto;
    }

    /* Grid layouts */
    .principle_grid, .feature_list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 20px 0;
    }

    .principle_grid > div, .feature_list > div {
      border: 1px solid #333;
      padding: 20px;
      background: rgba(0, 255, 0, 0.03);
    }

    .demo_container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }

    @media (max-width: 768px) {
      .demo_container {
        grid-template-columns: 1fr;
      }
    }

    /* Theme Toggle */
    .theme-btn {
      position: fixed;
      top: 20px;
      right: 20px;
      z-index: 1000;
      background: rgba(0, 0, 0, 0.8) !important;
      border-radius: 50%;
      width: 60px;
      height: 60px;
    }'''

    def _get_js_includes(self, body: Dict) -> List[str]:
        """Generate JavaScript includes for islands."""
        js_includes = []

        # Check if we have js_islands in the body
        if 'js_islands' in body:
            islands = body['js_islands']

            for island_name, js_file in islands.items():
                if isinstance(js_file, str):
                    js_includes.append(f'<script src="/js/{js_file}"></script>')

        # Always include core scripts if we have interactive elements
        if self._has_interactive_elements(body):
            js_includes.extend([
                '<script src="/js/theme-toggle.js"></script>',
                '<script src="/js/facet-demo.js"></script>',
                '<script src="/js/smooth-scroll.js"></script>'
            ])

        return js_includes

    def _has_interactive_elements(self, body: Dict) -> bool:
        """Check if body contains interactive elements."""
        # Simple check for common interactive element patterns
        body_str = str(body).lower()
        interactive_markers = ['button', 'id=', 'onclick', 'demo', 'toggle', 'parse', 'copy']
        return any(marker in body_str for marker in interactive_markers)
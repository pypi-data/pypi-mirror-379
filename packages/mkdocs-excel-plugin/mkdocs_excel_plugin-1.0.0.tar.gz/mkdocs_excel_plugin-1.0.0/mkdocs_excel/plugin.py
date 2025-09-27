"""MkDocs Excel Plugin - Main plugin class."""

import os
import re
from typing import Any, Dict, Optional

from mkdocs.config import config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File
from mkdocs.structure.pages import Page

from .renderer import ExcelRenderer


class ExcelPlugin(BasePlugin):
    """MkDocs plugin for rendering Excel files as HTML tables."""

    config_scheme = (
        ("cache_enabled", config_options.Type(bool, default=True)),
        ("max_file_size_mb", config_options.Type(int, default=5)),
        ("default_max_rows", config_options.Type(int, default=1000)),
        ("default_max_cols", config_options.Type(int, default=50)),
        ("theme", config_options.Type(str, default="material")),
    )

    def __init__(self):
        super().__init__()
        self.renderer: Optional[ExcelRenderer] = None

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        """Initialize the Excel renderer with plugin configuration."""
        self.renderer = ExcelRenderer(
            cache_enabled=self.config["cache_enabled"],
            max_file_size_mb=self.config["max_file_size_mb"],
            default_max_rows=self.config["default_max_rows"],
            default_max_cols=self.config["default_max_cols"],
        )

        # Add CSS to extra_css if not already present
        css_path = "assets/excel-plugin.css"
        if css_path not in config.get("extra_css", []):
            if "extra_css" not in config:
                config["extra_css"] = []
            config["extra_css"].append(css_path)

        return config

    def on_page_markdown(
        self, markdown: str, page: Page, config: MkDocsConfig, files
    ) -> str:
        """Process Excel macros in markdown content."""
        if not self.renderer:
            return markdown

        # Set current page context for relative path resolution
        self.renderer.set_page_context(page)

        # Process Excel macros
        markdown = self._process_excel_macros(markdown)

        return markdown

    def _process_excel_macros(self, content: str) -> str:
        """Process all Excel macro patterns in the content."""
        patterns = [
            # render_excel_sheet patterns
            (
                r'\{\{\s*render_excel_sheet\(\s*[\'"]([^\'"]+)[\'"]\s*,\s*[\'"]([^\'"]+)[\'"](?:\s*,\s*max_rows=(\d+))?(?:\s*,\s*max_cols=(\d+))?\s*\)\s*\}\}',
                self._render_sheet_macro,
            ),
            # render_excel_all_sheets patterns
            (
                r'\{\{\s*render_excel_all_sheets\(\s*[\'"]([^\'"]+)[\'"](?:\s*,\s*include_sheets=\[([^\]]+)\])?(?:\s*,\s*exclude_sheets=\[([^\]]+)\])?\s*\)\s*\}\}',
                self._render_all_sheets_macro,
            ),
            # list_excel_sheets pattern
            (
                r'\{\{\s*list_excel_sheets\(\s*[\'"]([^\'"]+)[\'"]\s*\)\s*\}\}',
                self._list_sheets_macro,
            ),
        ]

        for pattern, handler in patterns:
            content = re.sub(pattern, handler, content)

        return content

    def _render_sheet_macro(self, match) -> str:
        """Handle render_excel_sheet macro."""
        file_path = match.group(1)
        sheet_name = match.group(2)
        max_rows = (
            int(match.group(3)) if match.group(3) else self.config["default_max_rows"]
        )
        max_cols = (
            int(match.group(4)) if match.group(4) else self.config["default_max_cols"]
        )

        return self.renderer.render_excel_sheet(
            file_path, sheet_name, max_rows, max_cols
        )

    def _render_all_sheets_macro(self, match) -> str:
        """Handle render_excel_all_sheets macro."""
        file_path = match.group(1)

        # Parse include_sheets and exclude_sheets
        include_sheets = None
        exclude_sheets = None

        if match.group(2):  # include_sheets
            include_sheets = [s.strip().strip("'\"") for s in match.group(2).split(",")]

        if match.group(3):  # exclude_sheets
            exclude_sheets = [s.strip().strip("'\"") for s in match.group(3).split(",")]

        return self.renderer.render_excel_all_sheets(
            file_path,
            max_rows=self.config["default_max_rows"],
            max_cols=self.config["default_max_cols"],
            include_sheets=include_sheets,
            exclude_sheets=exclude_sheets,
        )

    def _list_sheets_macro(self, match) -> str:
        """Handle list_excel_sheets macro."""
        file_path = match.group(1)
        return self.renderer.list_excel_sheets(file_path)

    def on_post_build(self, config: MkDocsConfig) -> None:
        """Copy CSS assets to build directory."""
        assets_dir = os.path.join(config["site_dir"], "assets")
        os.makedirs(assets_dir, exist_ok=True)

        # Copy CSS file
        css_content = self._get_css_content()
        css_path = os.path.join(assets_dir, "excel-plugin.css")

        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css_content)

    def _get_css_content(self) -> str:
        """Get the CSS content for Excel tables."""
        return """
/* Excel Plugin Styles */
.excel-table-wrapper {
    overflow-x: auto;
    margin: 1rem 0;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.excel-table {
    border-collapse: collapse;
    font-size: 0.9rem;
    width: 100%;
    min-width: 100%;
    margin: 0;
}

.excel-table td, .excel-table th {
    border: 1px solid #ddd;
    padding: 8px;
    background-color: transparent;
    color: inherit;
    text-align: left;
    vertical-align: top;
}

.excel-info {
    background-color: rgba(68, 138, 255, 0.1);
    border: 1px solid rgba(68, 138, 255, 0.2);
    border-radius: 4px;
    padding: 12px;
    margin: 1rem 0;
}

.excel-error {
    background-color: rgba(255, 68, 68, 0.1);
    border: 1px solid rgba(255, 68, 68, 0.2);
    border-radius: 4px;
    padding: 12px;
    margin: 1rem 0;
}

.excel-warning {
    background-color: rgba(255, 193, 7, 0.1);
    border: 1px solid rgba(255, 193, 7, 0.2);
    border-radius: 4px;
    padding: 12px;
    margin: 1rem 0;
}

.excel-sheet-section {
    margin: 2rem 0;
}

.excel-sheet-title {
    color: #1976d2;
    border-bottom: 2px solid #1976d2;
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

.excel-sheet-divider {
    margin: 2rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #ddd, transparent);
}

/* Dark theme support */
[data-md-color-scheme="slate"] .excel-table td,
[data-md-color-scheme="slate"] .excel-table th {
    border-color: #404040;
}

[data-md-color-scheme="slate"] .excel-info {
    background-color: rgba(68, 138, 255, 0.2);
    border-color: rgba(68, 138, 255, 0.3);
}

[data-md-color-scheme="slate"] .excel-error {
    background-color: rgba(255, 68, 68, 0.2);
    border-color: rgba(255, 68, 68, 0.3);
}

[data-md-color-scheme="slate"] .excel-warning {
    background-color: rgba(255, 193, 7, 0.2);
    border-color: rgba(255, 193, 7, 0.3);
}

/* Responsive design */
@media (max-width: 768px) {
    .excel-table {
        font-size: 0.8rem;
    }

    .excel-table td, .excel-table th {
        padding: 6px;
    }
}
"""

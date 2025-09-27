"""Tests for the Excel plugin."""

import os
import tempfile
from unittest.mock import Mock, patch

import pytest

from mkdocs_excel.cache import ExcelCache
from mkdocs_excel.color_utils import apply_tint, get_rgb_from_color
from mkdocs_excel.renderer import ExcelRenderer


class TestExcelRenderer:
    """Test the Excel renderer functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.renderer = ExcelRenderer(
            cache_enabled=False,  # Disable cache for testing
            max_file_size_mb=5,
            default_max_rows=100,
            default_max_cols=20,
        )

    def test_file_not_found(self):
        """Test handling of non-existent files."""
        result = self.renderer.render_excel_sheet("nonexistent.xlsx", "Sheet1")
        assert "Excel File Not Found" in result
        assert "nonexistent.xlsx" in result

    def test_resolve_file_path_absolute(self):
        """Test absolute path resolution."""
        abs_path = "/absolute/path/file.xlsx"
        resolved = self.renderer._resolve_file_path(abs_path)
        assert resolved == abs_path

    def test_resolve_file_path_relative(self):
        """Test relative path resolution."""
        # Mock page context
        mock_page = Mock()
        mock_page.file.src_path = "docs/subdir/page.md"
        self.renderer.set_page_context(mock_page)

        resolved = self.renderer._resolve_file_path("data.xlsx")
        assert resolved == "docs/docs/subdir/data.xlsx"

    def test_file_size_warning(self):
        """Test file size warning generation."""
        with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
            # Create a small file for testing
            tmp.write(b"x" * 1024)  # 1KB
            tmp.flush()

            warning = self.renderer._get_file_size_warning(tmp.name)
            # Should not warn for small file
            assert warning == ""

            os.unlink(tmp.name)


class TestColorUtils:
    """Test color processing utilities."""

    def test_get_rgb_from_color_none(self):
        """Test handling of None color objects."""
        result = get_rgb_from_color(None)
        assert result is None

    def test_get_rgb_from_color_zero_rgb(self):
        """Test handling of zero RGB values."""
        mock_color = Mock()
        mock_color.rgb = "00000000"
        result = get_rgb_from_color(mock_color)
        assert result is None

    def test_get_rgb_from_color_valid_rgb(self):
        """Test handling of valid RGB values."""
        mock_color = Mock()
        mock_color.rgb = "FFFF0000"  # Red with alpha
        result = get_rgb_from_color(mock_color)
        assert result == "FF0000"

    def test_apply_tint_lighten(self):
        """Test color lightening with positive tint."""
        result = apply_tint("808080", 0.5)  # Gray -> lighter
        # Should be lighter than original
        assert int(result[:2], 16) > 0x80

    def test_apply_tint_darken(self):
        """Test color darkening with negative tint."""
        result = apply_tint("808080", -0.5)  # Gray -> darker
        # Should be darker than original
        assert int(result[:2], 16) < 0x80

    def test_apply_tint_no_change(self):
        """Test color with zero tint."""
        original = "FF0000"
        result = apply_tint(original, 0)
        assert result == original


class TestExcelCache:
    """Test cache functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.cache = ExcelCache()

    def test_cache_miss(self):
        """Test cache miss behavior."""
        assert not self.cache.is_valid("key", "nonexistent.txt")
        assert self.cache.get("key") is None

    def test_cache_set_get(self):
        """Test basic cache operations."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(b"test content")
            tmp.flush()

            # Set cache
            self.cache.set("test_key", "<html>test</html>", tmp.name)

            # Should be valid and retrievable
            assert self.cache.is_valid("test_key", tmp.name)
            assert self.cache.get("test_key") == "<html>test</html>"

            os.unlink(tmp.name)

    def test_cache_invalidation(self):
        """Test cache invalidation when file changes."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(b"original content")
            tmp.flush()

            # Set initial cache
            self.cache.set("test_key", "<html>original</html>", tmp.name)
            assert self.cache.is_valid("test_key", tmp.name)

            # Modify file (update mtime)
            import time

            time.sleep(0.1)  # Ensure mtime difference
            with open(tmp.name, "w") as f:
                f.write("modified content")

            # Cache should be invalid now
            assert not self.cache.is_valid("test_key", tmp.name)

            os.unlink(tmp.name)

    def test_cache_clear(self):
        """Test cache clearing."""
        self.cache._cache["key1"] = {"html": "test1", "mtime": 123}
        self.cache._cache["key2"] = {"html": "test2", "mtime": 456}

        self.cache.clear()
        assert len(self.cache._cache) == 0

    def test_cache_info(self):
        """Test cache information retrieval."""
        self.cache._cache["key1"] = {"html": "test1", "mtime": 123}
        self.cache._cache["key2"] = {"html": "test2", "mtime": 456}

        info = self.cache.get_cache_info()
        assert info["total_entries"] == 2
        assert "key1" in info["cache_keys"]
        assert "key2" in info["cache_keys"]
        assert info["memory_usage_estimate"] > 0


if __name__ == "__main__":
    pytest.main([__file__])

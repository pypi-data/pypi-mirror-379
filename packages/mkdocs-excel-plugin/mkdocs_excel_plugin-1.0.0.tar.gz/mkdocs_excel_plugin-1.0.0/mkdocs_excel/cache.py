"""Excel rendering cache management."""

import os
from datetime import datetime
from typing import Any, Dict, Optional


class ExcelCache:
    """Smart caching system for Excel rendering results."""

    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}

    def is_valid(self, cache_key: str, file_path: str) -> bool:
        """Check if cached result is still valid."""
        if cache_key not in self._cache:
            return False

        try:
            file_mtime = os.path.getmtime(file_path)
            cached_mtime = self._cache[cache_key].get("mtime", 0)
            return file_mtime <= cached_mtime
        except OSError:
            return False

    def get(self, cache_key: str) -> Optional[str]:
        """Get cached HTML content."""
        if cache_key in self._cache:
            return self._cache[cache_key].get("html")
        return None

    def set(self, cache_key: str, html: str, file_path: str) -> None:
        """Cache HTML content with file modification time."""
        try:
            file_mtime = os.path.getmtime(file_path)
            self._cache[cache_key] = {
                "html": html,
                "mtime": file_mtime,
                "cached_at": datetime.now(),
            }
        except OSError:
            pass

    def clear(self) -> None:
        """Clear all cached data."""
        self._cache.clear()

    def clear_file(self, file_path: str) -> None:
        """Clear cache for specific file."""
        keys_to_remove = []
        file_prefix = f"{file_path}#"

        for key in self._cache.keys():
            if key.startswith(file_prefix):
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self._cache[key]

    def get_cache_info(self) -> Dict[str, Any]:
        """Get cache statistics."""
        return {
            "total_entries": len(self._cache),
            "cache_keys": list(self._cache.keys()),
            "memory_usage_estimate": sum(
                len(entry.get("html", "")) for entry in self._cache.values()
            ),
        }

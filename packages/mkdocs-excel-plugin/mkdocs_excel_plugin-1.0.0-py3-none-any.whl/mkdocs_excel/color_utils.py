"""Excel color processing utilities."""

from typing import Optional


def get_rgb_from_color(color_obj, workbook=None) -> Optional[str]:
    """
    Extract RGB values from openpyxl color objects.

    Supports multiple color formats and strictly distinguishes between
    "has color setting" vs "no color setting" to avoid incorrect defaults.

    Args:
        color_obj: openpyxl color object
        workbook: Workbook object (for theme color conversion)

    Returns:
        RGB color value (e.g., "FF0000") or None (no color)
    """
    if not color_obj:
        return None

    try:
        # Pre-check: If RGB is all zeros, no color is set
        if hasattr(color_obj, "rgb") and color_obj.rgb:
            rgb = color_obj.rgb
            if isinstance(rgb, str) and rgb == "00000000":
                return None  # Explicitly no color, don't use default

        # Method 1: Direct RGB string processing
        if hasattr(color_obj, "rgb") and color_obj.rgb:
            rgb = color_obj.rgb
            if isinstance(rgb, str) and len(rgb) == 8:
                # AARRGGBB format, remove alpha channel
                if rgb != "00000000" and rgb[2:] != "000000":
                    return rgb[2:]  # Return RRGGBB

        # Method 2: Theme color processing (only process valid themes)
        if hasattr(color_obj, "theme") and color_obj.theme is not None:
            # Strict check: ensure theme is a valid integer value
            try:
                theme_value = int(color_obj.theme)
            except (ValueError, TypeError):
                return None  # Invalid theme value, return None instead of default

            theme_colors = {
                0: "FFFFFF",  # White (background1)
                1: "000000",  # Black (text1)
                2: "E7E6E6",  # Light gray (background2)
                3: "44546A",  # Dark gray (text2)
                4: "5B9BD5",  # Blue (accent1)
                5: "70AD47",  # Green (accent2)
                6: "C5504B",  # Red (accent3)
                7: "FFC000",  # Orange (accent4)
                8: "264478",  # Dark blue (accent5)
                9: "7030A0",  # Purple (accent6)
            }

            # Only process known themes, return None for unknown themes
            if theme_value not in theme_colors:
                return None

            base_color = theme_colors[theme_value]

            # Apply tint adjustment
            if hasattr(color_obj, "tint") and color_obj.tint != 0:
                base_color = apply_tint(base_color, color_obj.tint)

            return base_color

        # Method 3: Indexed color processing
        if hasattr(color_obj, "indexed") and color_obj.indexed is not None:
            # Excel standard color palette (simplified)
            indexed_colors = {
                0: "000000",
                1: "FFFFFF",
                2: "FF0000",
                3: "00FF00",
                4: "0000FF",
                5: "FFFF00",
                6: "FF00FF",
                7: "00FFFF",
                8: "000000",
                9: "FFFFFF",
                10: "FF0000",
                11: "00FF00",
                12: "0000FF",
                13: "FFFF00",
                14: "FF00FF",
                15: "00FFFF",
            }
            return indexed_colors.get(color_obj.indexed, None)

    except Exception:
        pass

    return None


def apply_tint(rgb_hex: str, tint_value: float) -> str:
    """
    Apply tint adjustment to RGB color.

    Args:
        rgb_hex: RGB color value (e.g., "70AD47")
        tint_value: Tint value (-1.0 to 1.0)

    Returns:
        Adjusted RGB color value
    """
    try:
        # Convert hex to RGB
        r = int(rgb_hex[0:2], 16)
        g = int(rgb_hex[2:4], 16)
        b = int(rgb_hex[4:6], 16)

        # Apply tint adjustment
        if tint_value > 0:
            # Lighten
            r = int(r + (255 - r) * tint_value)
            g = int(g + (255 - g) * tint_value)
            b = int(b + (255 - b) * tint_value)
        elif tint_value < 0:
            # Darken
            r = int(r * (1 + tint_value))
            g = int(g * (1 + tint_value))
            b = int(b * (1 + tint_value))

        # Ensure values are in 0-255 range
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        return f"{r:02X}{g:02X}{b:02X}"
    except:
        return rgb_hex  # Return original value on failure

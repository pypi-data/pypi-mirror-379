# materialgui/core/style.py

def generate_stylesheet(theme_colors):
    return f"""
    QWidget {{
        background-color: {theme_colors.background};
        color: {theme_colors.on_surface};
        font-family: "Roboto", "Segoe UI", sans-serif;
        font-size: 14px;
    }}

    MaterialButton {{
        background-color: {theme_colors.primary};
        color: {theme_colors.on_primary};
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 500;
        font-size: 14px;
    }}

    MaterialButton:hover {{
        background-color: {adjust_brightness(theme_colors.primary, 1.2)};
    }}

    MaterialButton:pressed {{
        background-color: {adjust_brightness(theme_colors.primary, 0.8)};
    }}

    MaterialCard {{
        background-color: {theme_colors.surface};
        border-radius: 16px;
        padding: 24px;
    }}

    MaterialTextField {{
        background-color: {theme_colors.surface};
        border: 1px solid {theme_colors.primary_container};
        border-radius: 12px;
        padding: 12px;
        color: {theme_colors.on_surface};
    }}
    """

def adjust_brightness(hex_color, factor):
    """Упрощённая корректировка яркости цвета"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = min(255, max(0, int(r * factor)))
    g = min(255, max(0, int(g * factor)))
    b = min(255, max(0, int(b * factor)))
    return f"#{r:02x}{g:02x}{b:02x}"

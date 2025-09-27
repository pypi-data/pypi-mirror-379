# materialgui/core/theme.py

from dataclasses import dataclass
from typing import Literal

@dataclass
class ThemeColors:
    primary: str
    on_primary: str
    primary_container: str
    on_primary_container: str
    secondary: str
    on_secondary: str
    surface: str
    on_surface: str
    background: str
    error: str
    on_error: str

class Theme:
    LIGHT = ThemeColors(
        primary="#6750A4",
        on_primary="#FFFFFF",
        primary_container="#EADDFF",
        on_primary_container="#22005D",
        secondary="#625B71",
        on_secondary="#FFFFFF",
        surface="#FFFBFE",
        on_surface="#1C1B1F",
        background="#FFFBFE",
        error="#B3261E",
        on_error="#FFFFFF",
    )

    DARK = ThemeColors(
        primary="#D0BCFF",
        on_primary="#381E72",
        primary_container="#4F378B",
        on_primary_container="#EADDFF",
        secondary="#CCC2DC",
        on_secondary="#332D41",
        surface="#141218",
        on_surface="#E6E0E9",
        background="#141218",
        error="#F2B8B5",
        on_error="#601410",
    )

    def __init__(self, mode: Literal["light", "dark"] = "light"):
        self.mode = mode
        self.colors = self.LIGHT if mode == "light" else self.DARK

    def toggle(self):
        self.mode = "dark" if self.mode == "light" else "light"
        self.colors = self.LIGHT if self.mode == "light" else self.DARK

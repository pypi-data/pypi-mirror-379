# materialgui/core/app.py

from PyQt6.QtWidgets import QApplication
from .theme import Theme
from .style import generate_stylesheet

class MaterialApp(QApplication):
    def __init__(self, argv, theme_mode="light"):
        super().__init__(argv)
        self.theme = Theme(theme_mode)
        self.setStyleSheet(generate_stylesheet(self.theme.colors))

    def toggle_theme(self):
        self.theme.toggle()
        self.setStyleSheet(generate_stylesheet(self.theme.colors))

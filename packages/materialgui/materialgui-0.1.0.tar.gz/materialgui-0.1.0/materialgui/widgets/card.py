# materialgui/widgets/card.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class MaterialCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        self.setLayout(layout)

        # Добавляем текст для проверки
        label = QLabel("Hello from MaterialCard!")
        label.setStyleSheet("font-size: 18px; color: #1c1b1f;")
        layout.addWidget(label)

        # Стили
        self.setStyleSheet("""
            MaterialCard {
                background-color: #ffffff;
                border-radius: 20px;
                color: #1c1b1f;
            }
        """)

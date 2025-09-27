# materialgui/widgets/button.py

from PyQt6.QtWidgets import QPushButton

class MaterialButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedHeight(48)
        self.setStyleSheet("""
            MaterialButton {
                background-color: #6750A4;
                color: white;
                border: none;
                border-radius: 24px;
                padding: 0 24px;
                font-size: 14px;
                font-weight: 500;
            }
            MaterialButton:hover {
                background-color: #7c4dff;
            }
            MaterialButton:pressed {
                background-color: #3700b3;
            }
        """)

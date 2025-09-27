# examples/demo.py

import sys
from materialgui.core.app import MaterialApp
from materialgui.widgets.button import MaterialButton
from materialgui.widgets.card import MaterialCard
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MaterialGUI Demo")
        self.setGeometry(300, 300, 400, 300)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setSpacing(24)
        layout.setContentsMargins(24, 24, 24, 24)

        card = MaterialCard()
        card_layout = QVBoxLayout(card)
        button = MaterialButton("Click Me!")
        button.clicked.connect(self.toggle_theme)
        card_layout.addWidget(button)
        layout.addWidget(card)

        self.setCentralWidget(central)

    def toggle_theme(self):
        app.toggle_theme()

if __name__ == "__main__":
    app = MaterialApp(sys.argv)
    window = DemoApp()
    window.show()
    sys.exit(app.exec())

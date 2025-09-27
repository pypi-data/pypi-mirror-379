# examples/demo.py

import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from materialgui.core.app import MaterialApp
from materialgui.widgets.card import MaterialCard
from materialgui.widgets.button import MaterialButton

class DemoApp(QMainWindow):
    def __init__(self, app_instance):
        super().__init__()
        self.app_instance = app_instance
        self.setWindowTitle("MaterialGUI Demo")
        self.resize(400, 300)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)

        card = MaterialCard()  # ← уже содержит текст
        layout.addWidget(card)

        button = MaterialButton("Click Me!")
        button.clicked.connect(lambda: print("Clicked!"))
        layout.addWidget(button)

        self.setCentralWidget(central)

if __name__ == "__main__":
    app = MaterialApp(sys.argv)
    window = DemoApp(app)
    window.show()
    sys.exit(app.exec())

# materialgui/effects/ripple.py

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QBrush, QPainterPath
from PyQt6.QtCore import QPropertyAnimation, pyqtProperty, QPoint, QEasingCurve
import math

class RippleEffect:
    def __init__(self, widget):
        self.widget = widget
        self.radius = 0
        self.center = QPoint(0, 0)
        self.animation = QPropertyAnimation(self, b"radius")
        self.animation.setDuration(600)
        self.animation.setStartValue(0)
        self.animation.setEndValue(200)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.finished.connect(self.widget.update)

    @pyqtProperty(int)
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.widget.update()

    def start(self):
        self.center = self.widget.rect().center()
        self.radius = 0
        self.animation.start()

    def draw(self):
        painter = QPainter(self.widget)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        color = QColor(255, 255, 255, 60)
        painter.setBrush(QBrush(color))
        painter.drawEllipse(self.center, self.radius, self.radius)

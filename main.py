import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QPointF
from PyQt6 import uic


class CirclePainter(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('UI.ui', self)

        self.circles = []

        self.pushButton.clicked.connect(self.add_circle)
        self.pushButton.setText("Добавить окружность")

    def add_circle(self):
        diameter = random.randint(20, 100)

        max_x = self.width() - diameter - 20
        max_y = self.height() - diameter - 100

        if max_x > 0 and max_y > 0:
            x = random.randint(20, max_x)
            y = random.randint(50, max_y)

            self.circles.append({
                'center': QPointF(x + diameter / 2, y + diameter / 2),
                'radius': diameter / 2
            })

            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        try:
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            for circle in self.circles:
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QColor(255, 255, 0))
                painter.drawEllipse(circle['center'], circle['radius'], circle['radius'])
        finally:
            painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CirclePainter()
    window.show()

    sys.exit(app.exec())

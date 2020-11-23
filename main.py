import sys
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5 import uic


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.do_paint = False

        self.size = 0
        self.x = 0
        self.y = 0

    def initUi(self):
        uic.loadUi('UI.ui', self)

        self.but.clicked.connect(self.upgrade_circle)

    def upgrade_circle(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, qp):
        if self.do_paint:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.do_paint = False

    def draw_flag(self, qp):
        size = randint(1, 200)
        x = randint(1, 1000 - size)
        y = randint(1, 680 - size)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x - size // 2, y - size // 2, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
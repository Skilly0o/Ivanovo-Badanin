import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        qp.setBrush(QColor(255, 225, 0))
        qp.drawEllipse(int(random.random(0, 300)), random.random(0, 300), random.random(0, 300))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    ex.setFixedSize(1000, 600)
    sys.exit(app.exec_())

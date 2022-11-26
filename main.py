import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow

SIZE = [800, 600]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False

    def mousePressEvent(self, event):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        size = randint(10, 100)
        color = (255, 255, 0)
        qp.setPen(QColor(*color))
        qp.setBrush(QColor(*color))
        x, y = randint(100, SIZE[0] - 100), randint(100, SIZE[1] - 100)
        qp.drawEllipse(x, y, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
    exit(app.exec())

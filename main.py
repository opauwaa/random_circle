import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QPoint, Qt
from form import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.run)
        self.go = False

    def paintEvent(self, event):
        if self.go:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        r = randint(10, 200)
        pen = QPen()
        pen.setWidth(8)
        qp.setBrush(Qt.NoBrush)
        pen.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.setPen(pen)
        qp.drawEllipse(QPoint(300, 300), r, r)

    def run(self):
        self.go = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

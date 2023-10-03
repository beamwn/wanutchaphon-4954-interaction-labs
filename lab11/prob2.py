from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
import sys
from functools import partial
from PyQt6.QtGui import QColor, QBrush, QFont

class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(300, 200)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)

        self.pen_color = QtGui.QColor('#000000')

    def set_pen_color(self, c):
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)

        brush = QtGui.QBrush()
        pen.setColor(QtGui.QColor("#000000"))
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        brush.setColor(QtGui.QColor(c))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(100, 50, 100, 100)

        painter.end()
        self.setPixmap(canvas)
        
COLORS = [
 '#982020','#ffd035','#d27676','#8fd970','#d36036','#35e3e3',  '#81588d'
]

class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24,24))
        self.color = color
        self.setStyleSheet(f"background-color: {color};")
        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color of the Day")
        self.canvas = Canvas()
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.setFont(QFont('text', 40))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        widget.setLayout(layout)
        layout.addWidget(self.canvas)
        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        layout.addLayout(palette)
        self.setCentralWidget(widget)


    def change_background(self, color):
        print(color)
        if color == '#982020':
            self.label.setText("Sunday")
            self.label.setStyleSheet(f"background-color:{color}; color:white")
        elif color == '#ffd035':
            self.label.setText("Monday")
            self.label.setStyleSheet(f"background-color:{color}")
        elif color == '#d27676':
            self.label.setText("Tuesday")
            self.label.setStyleSheet(f"background-color:{color}")
        elif color == '#8fd970':
            self.label.setText("Wednesday")
            self.label.setStyleSheet(f"background-color:{color}")
        elif color == '#d36036':
            self.label.setText("Thursday")
            self.label.setStyleSheet(f"background-color:{color}; color:white")
        elif color == '#35e3e3':
            self.label.setText("Friday")
            self.label.setStyleSheet(f"background-color:{color}")
        elif color == '#81588d':
            self.label.setText("Saturday")
            self.label.setStyleSheet(f"background-color:{color}; color:white")
        

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(partial(self.canvas.set_pen_color,c))
            b.pressed.connect(partial(self.change_background,c))
            layout.addWidget(b)

   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

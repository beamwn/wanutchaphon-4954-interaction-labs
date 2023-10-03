import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        canvas = QtGui.QPixmap(500,500)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.drawing()
    
    def drawing(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        
        pen.setColor(QtCore.Qt.GlobalColor.black)
        pen.setStyle(Qt.PenStyle.DashLine)
        painter.setPen(pen)
        painter.drawRect(100, 100, 300, 300)

        brush = QtGui.QBrush()
        pen.setColor(QtGui.QColor("#EB5160"))
        pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        brush.setColor(QtGui.QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawEllipse(150, 150, 200, 200)


        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(20)
        painter.setFont(font)
        pen = QtGui.QPen()
        painter.drawText(185, 255, 'Wanutchaphon')
        painter.setPen(pen)

        painter.end()
        self.label.setPixmap(canvas)


app = QApplication(sys.argv)
window = Mainwindow()
window.show()
app.exec()
        


        



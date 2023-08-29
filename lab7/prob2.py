import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        

        self.setWindowTitle('Calculator')


        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet("background-color: yellow; font-size: 20pt;")
        self.line_edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        grid.addWidget(self.line_edit,0,0,1,6)

        names = ['7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        
        positions = [(i, j) for i in range(1, 6) for j in range(1,5)]

        for position, name in zip(positions, names):
            
            
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300,150)
        


app = QApplication(sys.argv)
window = Calculator()
window.show()
app.exec()
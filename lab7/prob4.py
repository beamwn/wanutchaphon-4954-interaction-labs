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
        grid.addWidget(self.line_edit, 0, 0, 1, 6)

        names = ["7", "8", "9", "/",
                 "4", "5", "6", "*",
                 "1", "2", "3", "-",
                 "0", ".", "=", "+"]

        self.operators = {'/': '/', '*': '*', '-': '-', '+': '+'}
        position = [(i, j) for i in range(1, 6) for j in range(1, 5)]
        self.buttons = []


        for position, name in zip(position, names):
            
            
            button = QPushButton(name)
            button = QPushButton(name)
            button.clicked.connect(lambda _, n=name: self.handle_button_click(n))
            grid.addWidget(button, *position)

        self.move(300,150)
          
        self.current_input = ""
        self.pending_operator = ""
        self.last_result = ""
          

    def handle_button_click(self, text):
        if text in self.operators:
            if self.current_input:
                self.pending_operator = text
                self.last_result = self.current_input
                self.current_input = ""
        elif text == '=':
            if self.current_input and self.pending_operator:
                expression = self.last_result + self.pending_operator + self.current_input
                if self.pending_operator == "/" and self.current_input == "0":
                    self.line_edit.setText("Error")
                    self.current_input = ""
                else:
                    result = str(eval(expression))
                    self.line_edit.setText(result)
                    self.current_input = result
                    self.current_input = ""
                    self.pending_operator = ""
                    self.last_result = ""
        else: 
            self.current_input += text
            self.line_edit.setText(self.current_input)

        
        
app = QApplication(sys.argv)
window = Calculator()
window.show()
app.exec()
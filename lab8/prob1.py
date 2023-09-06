import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Simple Calculator")

        self.mainLayout = QVBoxLayout()
        self._createNumbersLayout()
        self._createButtonLayout()
        self._createResultLayout()
        self.mainLayout.addLayout(self.numberLayout)
        self.mainLayout.addLayout(self.number1Layout)
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addLayout(self.resultLayout)

        self.container = QWidget()
        self.container.setLayout(self.mainLayout)
        self.setCentralWidget(self.container)
        self._createMenuBar()

        self._handleEvents()
    
    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.configMenu = self.menuBar.addMenu("config")

    def _createNumbersLayout(self):
        self.numberLayout = QHBoxLayout()
        self.number1Layout = QHBoxLayout()
        
        self.first_number_label = QLabel("Enter the first number:")
        self.first_number_entry = QLineEdit()
        self.first_number_entry.setStyleSheet("background-color: yellow; color: black;")
        self.first_number_entry.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.numberLayout.addWidget(self.first_number_label,1)
        self.numberLayout.addWidget(self.first_number_entry)

        self.second_number_label = QLabel("Enter the second number:")
        self.second_number_entry = QLineEdit()
        self.second_number_entry.setStyleSheet("background-color: yellow; color: black;")
        self.second_number_entry.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.number1Layout.addWidget(self.second_number_label,1)
        self.number1Layout.addWidget(self.second_number_entry)


    
    def _createButtonLayout(self):
        self.buttonLayout = QHBoxLayout()
        self.plus_button = QPushButton("+")
        self.minus_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.divide_button = QPushButton("/")

        button = [self.plus_button, self.minus_button, self.multiply_button,
                  self.divide_button]
        
        for button in button:
            self.buttonLayout.addWidget(button)


    def calculate(self, operator):
        num1 = float(self.first_number_entry.text())
        num2 = float(self.second_number_entry.text())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                self.result_text.append("Error: Division by zero")
                return
            result = num1 / num2

        self.result_text.append(f"{num1} {operator} {num2} = {result:.2f}")
    
    def _handleEvents(self):
        self.plus_button.clicked.connect(lambda: self.calculate("+"))
        self.minus_button.clicked.connect(lambda: self.calculate("-"))
        self.multiply_button.clicked.connect(lambda: self.calculate("*"))
        self.divide_button.clicked.connect(lambda: self.calculate("/"))
        

    def _createResultLayout(self):
        self.resultLayout = QHBoxLayout()
        self.result_label = QLabel("Result:")
        self.result_text = QTextEdit()
        self.result_text.setStyleSheet("background-color: lightgreen; color: black;")
        self.resultLayout.addWidget(self.result_label)
        self.resultLayout.addWidget(self.result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from lab10.prob2 import ActionConfiguration

class MessageBoxDisplay(ActionConfiguration):
    def __init__(self):
        super(MessageBoxDisplay, self).__init__()
        self.setWindowTitle("Calculator with Message Box")
        self.first_number_entry.returnPressed.connect(self.check_first)
        self.second_number_entry.returnPressed.connect(self.check_second)

    def check_first(self):
        num1 = self.first_number_entry.text()
        num2 = self.second_number_entry.text()
        if not num1:
            QMessageBox.warning(self, "none", "Please enter the first number")
        elif not num1.isdigit():
            QMessageBox.warning(self, "Invalid input", "Please enter the first number")
        elif not num2:
            QMessageBox.warning(self, "none", "Please enter the second number")


    
    def check_second(self):
        num2 = self.second_number_entry.text()
        num1 = self.first_number_entry.text()
        if not num2:
            QMessageBox.warning(self, "none", "Please enter the second number")
        elif not num2.isdigit():
            QMessageBox.warning(self, "Invalid input", "Please enter the second number")
        elif not num1:
            QMessageBox.warning(self, "none", "Please enter the first number")

if __name__ == "__main__":
    app = QApplication([])
    window = MessageBoxDisplay()
    window.show()
    app.exec()
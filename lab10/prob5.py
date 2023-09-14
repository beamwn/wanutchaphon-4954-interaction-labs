from pathlib import Path
import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from lab10.prob4 import CalculatorFileDialog

class CalculatorDialogs(CalculatorFileDialog):
     
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator Dialogs")
        self.colorAction.triggered.connect(self.change_color)
        self.sizeAction.triggered.connect(self.change_size)

    def change_color(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.result_text.setStyleSheet(f"background-color:{col.name()}")

    def change_size(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result_text.setFont(font)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorDialogs()
    window.show()
    sys.exit(app.exec())
    
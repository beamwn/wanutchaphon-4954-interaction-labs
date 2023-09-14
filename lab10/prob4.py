from pathlib import Path
import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from lab10.prob3 import MessageBoxDisplay
class CalculatorFileDialog(MessageBoxDisplay):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator with File Dialog")


    def _handleSaveMenus(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getSaveFileName(self, 'save file', home_dir)

        if fname[0]:
            f = open(fname[0], 'w')
            with f:
                f.write(self.result_text.toPlainText()) 
    def _handleOpenMenus(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.result_text.setText(data)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorFileDialog()
    window.show()
    sys.exit(app.exec())

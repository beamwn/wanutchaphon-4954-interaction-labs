import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from PyQt6.QtGui import QAction, QIcon
from lab10.prob1 import WindowsMenusToolBar

class ActionConfiguration(WindowsMenusToolBar):
    def __init__(self):
        super(ActionConfiguration, self).__init__()
        self.setWindowTitle("Calculator with Status and Shortcuts")
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Ready")
        self.openAction.setStatusTip("Open a file")
        self.openAction.setShortcut("Ctrl+O")

        self.saveAction.setStatusTip("Save a file")
        self.saveAction.setShortcut("Ctrl+S")

        self.clearAction.setStatusTip("Clear a file")
        self.clearAction.setShortcut("Ctrl+R")

        self.exitAction.setStatusTip("Exit a file")
        self.exitAction.setShortcut("Ctrl+Q")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActionConfiguration()
    window.show()
    app.exec()


        
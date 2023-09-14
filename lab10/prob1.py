import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from PyQt6.QtGui import QAction, QIcon
from lab8.prob2 import MainWindowMenus

class WindowsMenusToolBar(MainWindowMenus):
    def __init__(self):
        super(WindowsMenusToolBar, self).__init__()
        self.setWindowTitle("Calculator with Menus and Toolbar")
        self._createActions()
        self._createToolBars()

    def _createActions(self):
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.saveAction.setIcon(QIcon("images/file-save.png"))
        self.openAction.setIcon(QIcon("images/file-open.svg"))
        self.clearAction.setIcon(QIcon("images/edit-clear.png"))

    def _createToolBars(self):
        fileToolBars = self.addToolBar("File")
        fileToolBars.addAction(self.openAction)
        fileToolBars.addAction(self.saveAction)
        fileToolBars.addAction(self.clearAction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowsMenusToolBar()
    window.show()
    app.exec()

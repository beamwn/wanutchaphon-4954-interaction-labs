import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction
from prob1 import MainWindow



class MainWindow(MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Calculator with Menus")
        self._addMenus()
        self._handleMenus()
        
    def _addMenus(self):
        self._addFileMenu()
        self._addEditMenu()
        self._addConfigMenu()

    def _handleMenus(self):
        self.saveAction.triggered.connect(self._handleSaveMenus)
        self.openAction.triggered.connect(self._handleOpenMenus)
        self.exitAction.triggered.connect(self._handleExitMenus)
        self.clearAction.triggered.connect(self._handleClearMenus)

    
    def _addFileMenu(self):
        self.openAction = QAction("Open", self)
        self.saveAction = QAction("Save", self)
        self.exitAction = QAction("Exit", self)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)
     


    def _addEditMenu(self):
        self.clearAction = QAction("Clear", self)
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.editMenu.addAction(self.clearAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)

    def _addConfigMenu(self):
        self.colorAction = QAction("Color", self)
        self.sizeAction = QAction("Size", self)
        self.configMenu.addAction(self.colorAction)
        self.configMenu.addAction(self.sizeAction)

    def _handleSaveMenus(self):
        filename = "result.txt"
        with open(filename, "w") as f:
            f.write(self.result_text.toPlainText()) 
        self.show_alert(f"Writing result to file {filename}")

    def _handleOpenMenus(self):
        filename = "result.txt"
        with open(filename, "r") as file:
            text = file.read()
        self.result_text.setText(text)
        self.show_alert(f"Reading result from file {filename}")


    def _handleClearMenus(self):
        boxs = [self.first_number_entry, self.second_number_entry, self.result_text]
        for box in boxs:
            box.clear()

    def _handleExitMenus(self):
        self.close()

    def show_alert(self, message):
        alert_msg = QMessageBox()
        alert_msg.setText(message)
        alert_msg.exec()
 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

        

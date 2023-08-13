import sys

from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()

        self.setWindowTitle("My App")
        self.name = name
        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.on_text_change)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        

    def on_text_change(self, name_ids):
        greeting_text = f"{name_ids}, " + self.name["name"] + self.name["id"]
        self.label.setText(greeting_text)


app = QApplication(sys.argv)

name_ids = {"name": "Wanutchaphon ", "id": "4954"} 
window = MainWindow(name_ids)
window.show()

app.exec()
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self, name, id):
        super().__init__()

        self.setWindowTitle(name)
        self.name = name
        self.id = id
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        #set the central widget of the window.
        self.setCentralWidget(self.button)

   
    def the_button_was_clicked(self):
        self.button.setText(self.id)
        self.button.setEnabled(False)
        self.setWindowTitle(self.id)

app = QApplication(sys.argv)

student = {"name": "Wanutchaphon Haema", "id": "653040495-4"} 
window = MainWindow(student["name"], student["id"])
window.show()

app.exec()
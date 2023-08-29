import sys

from PyQt6.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Name Form")


        layout = QVBoxLayout()
        
        self.firstname_layout = self.set_name_widget("First Name:")
        self.lastname_layout = self.set_name_widget("Last Name:")
        layout.addLayout(self.firstname_layout)
        layout.addLayout(self.lastname_layout)

        button_layout = QHBoxLayout()
        self.cancel_button = self.config_button(QPushButton("Cancel"), "red")
        self.submit_button = self.config_button(QPushButton("Submit"), "green")
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.submit_button)
        
        layout.addLayout(button_layout)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        


    def set_name_widget(self, name_str):
        name_layout = QHBoxLayout()
        label = QLabel(name_str)
        label.setStyleSheet("font-size: 20pt;")
        line_edit = QLineEdit()
        line_edit.setStyleSheet("font-size: 20pt;")
        name_layout.addWidget(label)
        name_layout.addWidget(line_edit)

        return name_layout
        
    def config_button(self, button, color):
        button.setStyleSheet(f"color: {color};")
        button.setFont(self.create_font(20))
        
        return button
    
    def create_font(self, size):
        font = self.font()
        font.setPointSize(size)

        return font
        
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

    

   
        


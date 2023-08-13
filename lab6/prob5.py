import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt



class CourseSelectionApp(QDialog):
    def __init__(self, parent=None):
        super(CourseSelectionApp, self).__init__(parent)
        
        self.setWindowTitle('My app')
        
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Enter your name')
        self.name_input.returnPressed.connect(self.status_message)
        
        self.course_list = QListWidget(self)
        self.course_list.setSelectionMode(
            QAbstractItemView.SelectionMode.MultiSelection
        )
        courses = ["EN842300", "EN842314", "EN842315"]
        self.course_list.addItems(courses)
        self.course_list.itemClicked.connect(self.status_message)

        self.status = QLabel(self)
        self.status.setStyleSheet("background-color: yellow;")
        self.status.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.course_list)
        layout.addWidget(self.status)

        self.setLayout(layout)


    def status_message(self):
        name = self.name_input.text()
        selected_course = [item.text() for item in self.course_list.selectedItems()]

        if name and selected_course:
            courses_text = ', '.join(selected_course)
            message = f"Hello {name}! You are interested in these courses {courses_text}"
            self.status.setText(message)
        else:
            self.status.setText(f"Hello {name}!")
        
    
    

        

app = QApplication(sys.argv)

window = CourseSelectionApp()
window.show()
app.exec()


        
        

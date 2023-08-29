import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
    

        self.setWindowTitle("Name Form")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.first_name_label = QLabel("First name:")
        self.first_name_entry = QLineEdit()

        first_name_layout = QHBoxLayout()
        first_name_layout.addWidget(self.first_name_label)
        first_name_layout.addStretch()
        first_name_layout.addWidget(self.first_name_entry)
        layout.addLayout(first_name_layout)

        self.last_name_label = QLabel("Last name:")
        self.last_name_entry = QLineEdit()

        last_name_layout = QHBoxLayout()
        last_name_layout.addWidget(self.last_name_label)
        last_name_layout.addStretch()
        last_name_layout.addWidget(self.last_name_entry)
        layout.addLayout(last_name_layout)

        gender_label = QLabel("Gender:")
        self.gender_layout = QHBoxLayout()
        self.gender_layout.addWidget(gender_label)
        self.gender_layout.addStretch()
        genders = ["Male", "Female", "Other"]
        self.gender_buttons = []
        
        for gender in genders:
            radio_button = QRadioButton(gender)
            self.gender_buttons.append(radio_button)
            self.gender_layout.addWidget(radio_button)

        layout.addLayout(self.gender_layout)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: white; color: red;")
        self.cancel_button.clicked.connect(self.cancel)
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: white; color: green;")
        self.submit_button.clicked.connect(self.submit)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.submit_button)
        layout.addLayout(button_layout)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignRight)


        result = QHBoxLayout()
        result_text = QLabel("Result: ")
        self.result_text = QTextEdit()
        result.addWidget(result_text)
        result.addWidget(self.result_text)
        layout.addLayout(result)

    def submit(self):
        first_name = self.first_name_entry.text()
        last_name = self.last_name_entry.text()
        gender_value = ""
        for radio_button in self.gender_buttons:
            if radio_button.isChecked():
                gender_value = radio_button.text()
                break

        result = f"First name:{first_name}\nLast name:{last_name}\n{gender_value} is selected"
        self.result_text.setPlainText(result)

    def cancel(self):
        self.first_name_entry.clear()
        self.last_name_entry.clear()

        for button in self.gender_buttons:
            button.setAutoExclusive(False)
            button.setChecked(False)
        self.result_text.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()

        





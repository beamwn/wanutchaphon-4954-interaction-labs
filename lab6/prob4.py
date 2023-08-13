import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Information of 6530404954")
        label = QLabel("Wanutchaphon Haema")
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                           Qt.AlignmentFlag.AlignVCenter)
    

        self.checkbox1 = QCheckBox("Orenge Juice")
        self.checkbox2 = QCheckBox("Green Tea")
        self.checkbox1.stateChanged.connect(self.state_change)
        self.checkbox2.stateChanged.connect(self.state_change)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["COE", "DME" ])
        self.combo_box.currentIndexChanged.connect(self.index_change)

        self.status = QLabel()
        self.status.setStyleSheet("background-color: lightgreen;")
        self.status.setText("Status:")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        
        quit_button = QPushButton()
        quit_button.setText("Quit")
        quit_button.clicked.connect(QApplication.instance().quit)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.status)
        layout.addWidget(quit_button)
        


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        
    def state_change(self, value):
            state = Qt.CheckState(value)
            if state == Qt.CheckState.Checked:
                 self.status.setText(f"You want to drink {self.sender().text()}")
            else:
                 self.status.setText(f"You don't want to drink {self.sender().text()}")

    def index_change(self):
         self.status.setText(f"You have studied in {self.sender().currentText()} ")


        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())


        

        

    
    


            
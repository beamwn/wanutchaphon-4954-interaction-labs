import sys

from PyQt6.QtWidgets import *

class GreetingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("653040495-4")

        label = QLabel()
        label.setText("Wanutchaphon Haema")

        quit_button = QPushButton()
        quit_button.setText("Quit")
        quit_button.setToolTip("Click to quit!")
        quit_button.clicked.connect(QApplication.instance().quit)


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(quit_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)

window = GreetingApp()
window.show()

sys.exit(app.exec())

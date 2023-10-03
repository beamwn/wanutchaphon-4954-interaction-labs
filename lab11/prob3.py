from PyQt6 import  QtWidgets 
from PyQt6.QtCore import  QPropertyAnimation , QRect
import sys , os
from PyQt6.QtGui import  QAction, QIcon
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from lab11.prob2 import MainWindow

class AnimationWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color of the Day with Animation")
        self._createMenuBar()
        self._createToolBars()
        self._setStatusBar()

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.AnimationMenu = self.menuBar.addMenu("Animation")
        self.AnimationAction = QAction("Size", self)
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.AnimationAction.setIcon(QIcon("icon-size.png"))
        self.AnimationAction.setShortcut("Ctrl+Shift+S")
        self.AnimationMenu.addAction(self.AnimationAction)
        self.AnimationAction.triggered.connect(self.Animation)


    def _createToolBars(self):
        fileToolBars = self.addToolBar("Animation")
        fileToolBars.addAction(self.AnimationAction)

    def _setStatusBar(self):
        self.statusBar = self.statusBar()
        self.statusBar.showMessage("Ready")
        self.AnimationAction.setStatusTip("Animate the size of the label")


    def Animation(self):
        self.anim = QPropertyAnimation(self.label, b"geometry")
        self.anim.setStartValue(QRect(10, 10, 100, 30))
        self.anim.setEndValue(QRect(100,20,150, 40))
        self.anim.setDuration(3000)
        self.anim.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    app.exec()
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout,
                             QVBoxLayout, QGridLayout, QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

# close window
class CloseW(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(500, 50)
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('excise')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CloseW()
    sys.exit(app.exec_())

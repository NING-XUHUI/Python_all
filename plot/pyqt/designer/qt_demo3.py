import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
        QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout,
        QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication

class PrompText(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b>widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(300, 100)
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('ToolTips')
        self.show()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PrompText()
    sys.exit(app.exec_())


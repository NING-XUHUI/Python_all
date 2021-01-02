import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


def onClick_button():
    print("onclick")


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_button)
btn.move(24, 52)
widget.resize(300, 240)
widget.move(250,200)
widget.setWindowTitle("屏幕坐标系")
widget.show()
sys.exit(app.exec_())


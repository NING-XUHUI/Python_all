import sys
from PyQt5.QtWidgets import QApplication, QWidget


def show_w():
    app = QApplication(sys.argv)  # 所有的pyqt5应用必须创建一个应用对象
    # sys.argv参数是一个来自命令行的参数列表

    w = QWidget()  # QWidget组件是朋友圈图5所有用户界面类的基础类，我们给QWidget提供默认构造方法
    # 默认构造方法没有父类，没有父类的widget组件将被作为窗口使用

    w.resize(500, 500)  # 调整组件大小，500px x 500px
    w.move(500, 100)  # 移动到某一个位置，这个位置时屏幕上x=500， y=100的坐标
    w.setWindowTitle('Simple')  # 设置标题
    w.show()  # 在屏幕中显示出widget
    sys.exit(app.exec_())  # 应用进入主循环。在这个地方，事件处理开始执行，主循环用于接受来自窗口触发的事件
    # sys.exit()方法确保一个不留垃圾的退出，系统环境将会被通知应用是怎么被结束的。


if __name__ == '__main__':
    show_w()

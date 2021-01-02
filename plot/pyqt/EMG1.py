# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EMG1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1059, 837)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1041, 511))
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 1011, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 520, 741, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(30, 50, 671, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(800, 560, 160, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "EMG数据"))
        self.groupBox_2.setTitle(_translate("Dialog", "EMG分析"))
        self.pushButton.setText(_translate("Dialog", "波形还原"))
        self.pushButton_2.setText(_translate("Dialog", "频率分析"))
        self.pushButton_3.setText(_translate("Dialog", "小波分析"))


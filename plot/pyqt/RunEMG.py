from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from EMG2 import Ui_MainWindow

import matplotlib
from sklearn.preprocessing import StandardScaler

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../FMW/L-wanshen_FMW.csv')

columns = data.columns
time = data.iloc[:, :1].copy()
time.dropna(axis=0, inplace=True)
EMG_cols = [c for c in columns if "EMG" in c]
times = len(time)


L_wanshen_FMW = pd.read_csv('../FMW/L-wanshen_FMW.csv')
column_L_wanshen_FMW = L_wanshen_FMW.columns


class MyFigure(FigureCanvas):
    def __init__(self, width, height, dpi):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("肌电信号分析")
        self.setMinimumSize(500, 500)

        self.F = MyFigure(width=30, height=30, dpi=100)
        self.plotData()
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.addWidget(self.F)

        self.F1 = MyFigure(width=1, height=1, dpi=100)
        self.plotData1()
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.addWidget(self.F1)

    def plotData(self):
        for i in range(len(EMG_cols)):
            axes = self.F.fig.add_subplot(4, 2, i+1)
            emg = data[EMG_cols[i]]
            emg = emg.iloc[:times]
            axes.get_xaxis().set_visible(False)

            axes.plot(time, emg)
            # axes.set_title("{}".format(EMG_cols[i]))

    def plotData1(self):
        self.F1.axes = self.F1.fig.add_subplot(111)
        data1 = L_wanshen_FMW[column_L_wanshen_FMW[1]][0:2048].reset_index()
        data2 = L_wanshen_FMW[column_L_wanshen_FMW[21]][0:2048].reset_index()
        data3 = L_wanshen_FMW[column_L_wanshen_FMW[41]][0:2048].reset_index()
        data4 = L_wanshen_FMW[column_L_wanshen_FMW[61]][0:2048].reset_index()
        data5 = L_wanshen_FMW[column_L_wanshen_FMW[81]][0:2048].reset_index()
        data6 = L_wanshen_FMW[column_L_wanshen_FMW[101]][0:2048].reset_index()
        data1.drop(['index'], axis=1, inplace=True)
        data2.drop(['index'], axis=1, inplace=True)
        data3.drop(['index'], axis=1, inplace=True)
        data4.drop(['index'], axis=1, inplace=True)
        data5.drop(['index'], axis=1, inplace=True)
        data6.drop(['index'], axis=1, inplace=True)
        scaler = StandardScaler()
        trans_data1 = scaler.fit_transform(data1)
        trans_data2 = scaler.fit_transform(data2)
        trans_data3 = scaler.fit_transform(data3)
        trans_data4 = scaler.fit_transform(data4)
        trans_data5 = scaler.fit_transform(data5)
        trans_data6 = scaler.fit_transform(data6)
        # plt.figure(figsize=(30, 8))
        self.F1.axes.plot(L_wanshen_FMW[column_L_wanshen_FMW[0]][1024:1536], trans_data1[1024:1536], label='1', color='blue')
        self.F1.axes.plot(L_wanshen_FMW[column_L_wanshen_FMW[20]][1024:1536], trans_data2[1024:1536], label='2')
        self.F1.axes.plot(L_wanshen_FMW[column_L_wanshen_FMW[40]][1024:1536], trans_data3[1024:1536], label='3')
        self.F1.axes.plot(L_wanshen_FMW[column_L_wanshen_FMW[60]][1024:1536], trans_data4[1024:1536], label='4')
        self.F1.axes.plot(L_wanshen_FMW[column_L_wanshen_FMW[80]][1024:1536], trans_data5[1024:1536], label='5', color='black')
        self.F1.axes.plot(L_wanshen_FMW[column_L_wanshen_FMW[100]][1024:1536], trans_data6[1024:1536], label='6')
        self.F1.axes.legend()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

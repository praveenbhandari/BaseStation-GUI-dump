import threading

import serial
from serial.tools import list_ports
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1958, 1032)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1951, 1001))
        self.label.setStyleSheet("background-image: url(:/k/k.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = Widget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 260, 171, 191))
        self.widget.setObjectName("widget")
        self.widget_2 = Widgets(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(590, 260, 211, 191))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = Cool(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(1090, 260, 211, 191))
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 620, 151, 51))
        self.label_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 730, 151, 51))
        self.label_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 840, 151, 51))
        self.label_4.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 620, 181, 51))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 730, 181, 51))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 840, 181, 51))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 620, 151, 51))
        self.label_5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 730, 151, 51))
        self.label_6.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 840, 151, 51))
        self.label_7.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 620, 181, 51))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(720, 730, 181, 51))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(720, 840, 181, 51))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1070, 680, 231, 81))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(251,252,83);\n"
"    border-radius:20px;\n"
"    background-color: rgb(251,252,83);\n"
"     font-size:24px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-colour:rgb(255, 255, 127)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1070, 810, 231, 91))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border :2px solid rgb(255,255,255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(255,255,255);\n"
"    font-size:24px\n"
"}\n"
"QPushButton:hover{\n"
"    background-colour:rgb(198, 198, 198)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(1450, 190, 401, 361))
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1490, 640, 321, 301))
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:10px;\n"
"    background-color: rgb(85, 255, 255);\n"
"    font-size:330px\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 80, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(410, 80, 231, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(740, 60, 151, 51))
        self.label_8.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(870, 60, 121, 51))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(102, 255, 102);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1010, 60, 151, 51))
        self.label_9.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1958, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ROLL</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">PITCH</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">YAW</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">AIR SPEED</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">TIMER</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ACCE.</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "CALIBRATE"))
        self.pushButton_2.setText(_translate("MainWindow", "PADA"))
        self.lineEdit_8.setText(_translate("MainWindow", "1"))
        '''self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(5, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(6, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(7, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(8, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(9, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(10, _translate("MainWindow", "New Item"))'''

        self.comboBox_2.setItemText(0, _translate("MainWindow", "4800"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "9600"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "19200"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "38400"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "57600"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "111100"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "115200"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "230400"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;background-color:green;\">BATTERY</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">%</span></p></body></html>"))
        comss = []
        for i in list_ports.comports():
            print(i[1])
            comss.append(i[1])
            for j in range(len(list_ports.comports())):
                self.comboBox.setItemText(j, _translate("MainWindow", i[1]))
    def read_com(self,ser):
        # for i in range(0,10):
        while True:
            preo = [str(str(str(ser.readline()).split("'")[1]).split("\\")[0]).split(" ")]
            print(preo[0])
            if(len(preo[0]) > 1 ):
                self.roll.setText(preo[0][0])
                self.pitch.setText(preo[0][1])
                self.yaw.setText(preo[0][2])
                self.lineEdit_8.setText(preo[0][3])
                self.a_speed.setText(preo[0][4])
            else:
                print(preo[0])
            

    def ser_conn(self,comm, baud):
        print("construct : ")
        ser = serial.Serial(comm, baud, timeout=1)
        try:
            
            print(ser.name)
            # tt = threading.Thread(target=self.read_com,args=(ser,))
            # tt.start()
            print("after")
        except:
            print('except')
        finally:
            print('nal')

from pitch import Widgets
from compass import Widget
from pyqtgraph import PlotWidget
from roll1 import Cool
import d


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    t1 = threading.Thread(target=MainWindow.show())
    t2 = threading.Thread(target=ui.ser_conn, args=('COM14', 115200))
   
    # starting thread 2
    t2.start()
    # print("thread 2 started")
    t1.start()
    # MainWindow.show()
    sys.exit(app.exec_())

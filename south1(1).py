import serial
from serial.tools import list_ports
# from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import asyncio

class Ui_MainWindow(object):
    # def c_label(self,name,x,y,l,w):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.

        MainWindow.resize(1754, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 20, 1811, 971))
        self.label.setObjectName("label")
        label_style_sheet = "QLabel{\n""    border :2px solid rgb(0, 255, 255);\n" "    border-radius:20px;\n" "    background-color: rgb(85, 255, 255);\n""    font-size:18pt;\n""}"
        self.roll = QtWidgets.QLabel(self.centralwidget)
        self.roll.setGeometry(QtCore.QRect(270, 420, 181, 51))
        self.roll.setStyleSheet(label_style_sheet)
        self.roll.setObjectName("rolll")

#         self.label_211 = QtWidgets.QLabel(self.centralwidget)
#         self.label_211.setGeometry(QtCore.QRect(270, 420, 181, 51))
#         self.label_211.setStyleSheet("QLabel{\n"
# "    border :2px solid rgb(0, 255, 255);\n"
# "    border-radius:20px;\n"
# "    background-color: rgb(85, 255, 255);\n"
# "}")
#         self.label_211.setObjectName("label_211")


        self.pitch = QtWidgets.QLabel(self.centralwidget)
        self.pitch.setGeometry(QtCore.QRect(270, 520, 181, 51))
        self.pitch.setStyleSheet(label_style_sheet)
        self.pitch.setObjectName("pitch")




        self.yaw = QtWidgets.QLabel(self.centralwidget)
        self.yaw.setGeometry(QtCore.QRect(270, 630, 181, 51))
        self.yaw.setStyleSheet(label_style_sheet)
        self.yaw.setObjectName("yaw")


        self.acce = QtWidgets.QLabel(self.centralwidget)
        self.acce.setGeometry(QtCore.QRect(700, 630, 181, 51))
        self.acce.setStyleSheet(label_style_sheet)
        self.acce.setObjectName("acce")


        self.timerr = QtWidgets.QLabel(self.centralwidget)
        self.timerr.setGeometry(QtCore.QRect(700, 520, 181, 51))
        self.timerr.setStyleSheet(label_style_sheet)
        self.timerr.setObjectName("timerr")


        self.a_speed = QtWidgets.QLabel(self.centralwidget)
        self.a_speed.setGeometry(QtCore.QRect(700, 420, 181, 51))
        self.a_speed.setStyleSheet(label_style_sheet)
        self.a_speed.setObjectName("a_speed")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(980, 600, 231, 91))
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
        # self.pushButton_2.setText("test")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(980, 490, 231, 81))
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

        self.d_alt = QtWidgets.QLineEdit(self.centralwidget)
        self.d_alt.setGeometry(QtCore.QRect(980, 410, 231, 51))
        self.d_alt.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:20px;\n"
"    background-color: rgb(85, 255, 255);\n"
"}")
        self.d_alt.setObjectName("d_alt")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(920, 60, 321, 301))
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"    border :2px solid rgb(0, 255, 255);\n"
"    border-radius:10px;\n"
"    background-color: rgb(85, 255, 255);\n"
"    font-size:330px\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        # self.lineEdit_8.setText("test")

        self.roll_label = QtWidgets.QLabel(self.centralwidget)
        self.roll_label.setGeometry(QtCore.QRect(50, 420, 151, 51))
        self.roll_label.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.roll_label.setObjectName("roll_label")

        self.label_pitch = QtWidgets.QLabel(self.centralwidget)
        self.label_pitch.setGeometry(QtCore.QRect(50, 520, 151, 51))
        self.label_pitch.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_pitch.setObjectName("pitch")
        self.label_yaw = QtWidgets.QLabel(self.centralwidget)
        self.label_yaw.setGeometry(QtCore.QRect(50, 630, 151, 51))
        self.label_yaw.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_yaw.setObjectName("label_yaw")
        self.label_a_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_a_speed.setGeometry(QtCore.QRect(490, 420, 151, 51))
        self.label_a_speed.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_a_speed.setObjectName("label_a_speed")
        self.label_timer = QtWidgets.QLabel(self.centralwidget)
        self.label_timer.setGeometry(QtCore.QRect(490, 520, 151, 51))
        self.label_timer.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_timer.setObjectName("label_timer")
        self.label_acc = QtWidgets.QLabel(self.centralwidget)
        self.label_acc.setGeometry(QtCore.QRect(490, 630, 151, 51))
        self.label_acc.setStyleSheet("\n" "color: rgb(255, 255, 255);")
        self.label_acc.setObjectName("label_acc")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(1320, 40, 401, 361))
        self.graphicsView.setObjectName("graphicsView")
        self.widget = AnalogGaugeWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(470, 60, 391, 301))
        self.widget.setObjectName("widget")
        self.widget_2 = Widget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 50, 431, 331))
        self.widget_2.setObjectName("widget_2")





        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1754, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/g1/----------.png\"/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "PADA"))
        self.pushButton_3.setText(_translate("MainWindow", "CALIBRATE"))
        self.lineEdit_8.setText(_translate("MainWindow", "1"))
        roll_html = "<html><head/><body><p><span style=\" font-size:18pt;\">ROLL</span></p></body></html>"
        pitch_html = "<html><head/><body><p><span style=\" font-size:18pt;\">PITCH</span></p></body></html>"
        yaw_html = "<html><head/><body><p><span style=\" font-size:18pt;\">YAW</span></p></body></html>"
        a_speed_html = "<html><head/><body><p><span style=\" font-size:18pt;\">AIR SPEED</span></p></body></html>"
        timer_html = "<html><head/><body><p><span style=\" font-size:18pt;\">TIMER</span></p></body></html>"
        acce_html = "<html><head/><body><p><span style=\" font-size:18pt;\">ACCE.</span></p></body></html>"
        self.roll_label.setText(_translate("MainWindow",roll_html ))
        self.label_pitch.setText(_translate("MainWindow",pitch_html ))
        self.label_yaw.setText(_translate("MainWindow",yaw_html))
        self.label_a_speed.setText(_translate("MainWindow", a_speed_html))
        self.label_timer.setText(_translate("MainWindow", timer_html))
        self.label_acc.setText(_translate("MainWindow", acce_html))
        # self.roll.setText('roll')
        # self.pitch.setText('pitch')
        # self.yaw.setText('yaw')

    def shit(self,c_roll,c_pitch,c_yaw):
        print("construct : ", c_roll)
        print("construct : ", c_pitch)
        print("construct : ", c_yaw)

    def r_ser(self):
        for i in list_ports.comports():
            print(i[1])

    def read_com(self,ser):
        while True:
            # print(type(ser.read()))
            # print(ser.read().decode().strip())
            prii = [str(str(ser.readline()).split(':')[1]).split('\\')[0]]
            # rr=prii.split(",")
            # print(prii[0].split(","))
            self.roll.setText(prii[0].split(",")[0])
            self.pitch.setText(prii[0].split(",")[1])
            self.yaw.setText(prii[0].split(",")[2])
            # self.roll.setText("dhit")

    def s_un(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        main_window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(main_window)
        # ui.shit("shit")
        main_window.show()
        sys.exit(app.exec_())

    def ser_conn(self,comm, baud):
        print("construct : ")
        # uui = Ui_MainWindow()
        # # uui.shit()
        # uui.shit("11.111", "22.22", "33.33")
        # self.s_un()
        # s_un()
        # self.roll.setText('c_roll')
        # self.pitch.setText('c_pitch')
        # self.yaw.setText('c_yaw')
        # try:
        ser = serial.Serial(comm, baud, timeout=1)
        print(ser.name)
        self.read_com(ser)
        # except:
        #     print('except')
        # finally:
        #     print('nal')

from AnalogGaugeWidget import AnalogGaugeWidget
from compass import Widget
from pyqtgraph import PlotWidget
import g1

async def main():
    await asyncio.sleep(1)
    retranslateUi()
    shit()
    r_ser()
    read_com()
    s_un()
    ser_conn()
#
# def shit(ass):
#     print("construct : ",self.ass)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.shit("shit")
    asyncio.run(main())

    ui.ser_conn('COM8', 115200)
    MainWindow.show()
    sys.exit(app.exec_())

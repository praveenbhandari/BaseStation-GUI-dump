
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1244, 862)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(740, 270, 470, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.debid = QtWidgets.QWidget(self.widget)
        self.debid.setStyleSheet("QWidget#debid{\n"
"background-color:rgb(35,34,39);\n"
"}")
        self.debid.setObjectName("debid")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.debid)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.debid)
        self.widget_4.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"color:rgb(255,255,255);\n"
"font-size:17px;\n"
"font-family:Wingdings;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(144,144,144,30);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:rgb(27,27,27);\n"
"border-radius:12px;\n"
"color:rgb(240,240,240);\n"
"padding-left:15px;\n"
"border:1px solid rgba (255,255,255,50)\n"
"}\n"
"QLineEdit:focus{\n"
"\n"
"border:1px solid rgba (99,173,229,150)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.debid)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(740, 310, 461, 491))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.webEngineView = QWebEngineView(self.widget)
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45,45,45,225))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "è"))
        self.pushButton_2.setText(_translate("Form", "ç"))
        self.pushButton_3.setText(_translate("Form", "¡"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Type a URL"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


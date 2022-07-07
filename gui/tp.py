from PyQt5 import QtWidgets , QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from gui import tiger
from tiger import Ui_Form
import sys

class moWidget(QtWidgets.QWidget):
    def __init__(self):
        super(moWidget,self).__init__()
    def mousePressEvent(self,event):
        if event.button()== QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos()- self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

 

class browerserApp(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(browerserApp,self).__init()
        self.setupUi(self)
        self.lineEdit.returnPressed.connect(self.load)
    

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit())
        if url.isValid():
            self.webEngineView.load(url)
          





import sys
app= QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = tiger(Form)
Form.show()
sys.exit(app.exec_())
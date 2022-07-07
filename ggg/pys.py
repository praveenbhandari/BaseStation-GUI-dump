import serial
from serial.tools import list_ports
from PyQt5 import QtWidgets
# python -m serial.tools.list_ports
# from south import Ui_MainWindow
# from south import Ui_MainWindow
comss=[]
for i in list_ports.comports():
	print(i[1])
	comss.append(i[1])
# uui = Ui_MainWindow()
print(comss)

def read_com(ser):
	while True:
		# print(type(ser.read()))
		# print(ser.read().decode().strip())
		# print(str(str(ser.readline()).split(':')[1]).split('\\')[0])
		print(str(str(str(str(ser.readline()).split("\'")[1]).split("/")[0]).split(":")).split("\\")[0])
		# prii = [str(str(str(str(ser.readline()).split("\'")[1]).split("/")[0]).split(":"))]
		# prii =str(prii[0]).split(",")
		# # # # rr=prii.split(",")
		# # # self.roll.setText(self.str(30))
		# print(str(str(str(ser.readline()).split("\'")[1]).split("/")[0]).split(":"))
		# print(srt(str(str(ser.readline()).split("'")[1]).split("\\")[0]))
		# print(str(str(str(ser.readline()).split("'")[1]).split("\\")[0]).split(" "))
		# print(prii)
		# print(prii[0])
		# try:
		# 	ui_wala(self.prii[0].split(",")[0],self.prii[0].split(",")[1],self.prii[0].split(",")[2])
		# except():
		# 	print("eeeeeee")
		# finally:
		# 	print("fffff	")
# def s_un():
# 	import sys
# 	app = QtWidgets.QApplication(sys.argv)
# 	main_window = QtWidgets.QMainWindow()
# 	ui = Ui_MainWindow()
# 	ui.setupUi(main_window)
# 	# ui.shit("shit")
# 	main_window.show()
# 	sys.exit(app.exec_())
# def ui_wala(x,y,z):
	# print("construct : ")
	
	# # uui.shit()
	# Ui_MainWindow().shit(x, y, z)

def ser_conn(comm, baud):
	
	# s_un()
	try:
		ser = serial.Serial(comm, baud, timeout=1)
		print(ser.name)
		read_com(ser)
	except:
		print('except')
	finally:
		print('nal')
# def drop_c():
# 	ser.write(b'1')     # write a string for DROP
#


ser_conn('COM14', 115200)


# ser.close()

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer
import sys
import win32con
import win32gui
import win32process
def window():
	class cssden(QMainWindow):
		    def __init__(self):
		        super().__init__()


		        self.mwidget = QMainWindow(self)
		        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


		        #size
		        self.setFixedSize(320, 450)
		        self.center


		        #label
		        self.lbl = QLabel(self)
		        self.lbl.setText("test")
		        self.lbl.setStyleSheet("background-color: rgb(0,0,0);"
		                               "border: 1px solid red;"
		                               "color: rgb(255,255,255);"
		                               "font: bold italic 20pt 'Times New Roman';")
		        self.lbl.setGeometry(5,5,60,40)

		        self.show()

		    #center
		    def center(self):
		        qr = self.frameGeometry()
		        cp = QDesktopWidget().availableGeometry().center()
		        qr.moveCenter(cp)
		        self.move(qr.topLeft())

	app = QApplication(sys.argv)
	app.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")

	ex = cssden()
	sys.exit(app.exec_())
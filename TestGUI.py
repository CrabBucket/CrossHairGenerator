from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer,QTimer
import overlay
import sys
import win32con
import win32gui
import win32process
## Functions for GUI
def create_windows(box):
	#Callback handles/creates the list of windows
	def callback(hwnd,hwnds):
		if(win32gui.GetWindowText(hwnd)!=""):
			hwnds.append(hwnd)
	hwnds = []
	win32gui.EnumWindows(callback,hwnds)
	for a in hwnds:
		box.addItem(win32gui.GetWindowText(a),a)
def on_press():
	app.quit()
	timer = QTimer()
	timer.setInterval(2000)
	timer.start()
	timer.timeout.connect(overlay.window())
	
def window_select(index):
	print(win32gui.GetWindowRect(windows.itemData(index)))

##
## GUI Styling and Startup
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
##

##GUI Button adding and linking
on = QPushButton('On')
on.clicked.connect(on_press)
windows = QComboBox()
create_windows(windows)
windows.activated.connect(window_select)
layout.addWidget(windows)
layout.addWidget(on)
layout.addWidget(QPushButton('Off'))
##
## Gui final setup and run
window.setLayout(layout)
window.show()
app.exec_()




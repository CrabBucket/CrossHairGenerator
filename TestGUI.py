from PyQt5.QtWidgets import *
import psutil
def create_processes(box):
	for a in psutil.process_iter():
		box.addItem(a.name())
def on_press():
	print('button click')
app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()
on = QPushButton('On')
on.clicked.connect(on_press)
processes = QComboBox()
create_processes(processes)
layout.addWidget(processes)
layout.addWidget(on)
layout.addWidget(QPushButton('Off'))

window.setLayout(layout)
window.show()
app.exec_()




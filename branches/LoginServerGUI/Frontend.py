import sys
from threading import Thread
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtGui import *

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, gui_thread):
		QMainWindow.__init__(self, None)
		self.setupUi(self)
		self.gui_thread = gui_thread
		
	def add_text(self, t):
		self.textBrowser.append(t)
		
	def showEvent(self, ev):
		self.gui_thread.InitComplete()
	
class GUI(Thread):
	"""
		Your custom GUI class must contain these methods:
			GUI.AddLog(data, log_type)
			GUI.EventHandler(data, event_type, **args)
	"""
	def __init__(self, LS = None):
		"""
			@LS
				LoginServer Instance
		"""
		super(GUI, self).__init__()
		self.LoginServer = LS
		self.buffer = []
		self.window = None
		
	def AddLog(self, data, log_type = None):
		if not self.window:
			self.buffer += [(data, log_type)]
		else:
			self.window.add_text(data)
	
	def InitComplete(self):
		if self.buffer:
			for _data, _log_type in self.buffer:
				self.AddLog(_data, _log_type)
		
	def run(self):
		app = QApplication(sys.argv)
		self.window = MainWindow(self)
		self.window.show()
		sys.exit(app.exec_())
		
		#self.window.emit(SIGNAL('add_text(QString)'), data)
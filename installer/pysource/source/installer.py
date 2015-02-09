import os,sys
from installer_ui import Ui_MainWindow

class MainWindow(object):
	def __init__(self,parent=0):
		super(MainGUI,self).__init__(parent)
		self.UI = Ui_MainWindow()

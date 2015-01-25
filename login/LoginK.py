import MySQLdb
from PyQt4 import QtCore
from PyQt4 import QtGui
#~ from PyQt4 import QtSvg
#~ from PyQt4.QtCore import *
#~ from PyQt4.QtGui import *
#~ import sip 
#~ import sys,os
import functools
import itertools
import re
from datetime import datetime

from login_ui import  Ui_fr_Main

class Login(Ui_fr_Main):
	def __init__(self, parent=None):
		pass
	def Login_init(self):
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		self.fr_Login_Frame = QtGui.QFrame(self.centralwidget)
		self.LoginUI = Ui_fr_Main()
		self.LoginUI.setupUi(self.fr_Login_Frame)
		self.fr_Login_Frame.show()
		self.fr_Login_Frame.setGeometry(QtCore.QRect(0,0,WinW,WinH))
		self.fr_Login_Frame.setStyleSheet("background:white;")
		
		
		aatime = QtCore.QTimer(self)
		aatime.timeout.connect(self.Login_Redraw)
		print(str(dir (aatime.timeout)))
		aatime.start(500)
		
		
		self.LoginUI.chk_Connect_Lokal.stateChanged.connect(self.Login_Connect_SetLokal)
		
		self.LoginUI.tb_Connect_Ok.clicked.connect(self.Login_Connect_Act_OK)
		
		self.INDEX_ST_LOGIN = ["CONNECT","LOGIN","DATABASE"]
	#--- end Login_init
	
	def Login_Goto(self,room):
		if (type(room)==str):
			self.LoginUI.st_Main.setCurrentIndex(self.INDEX_ST_LOGIN.index(room.upper()))
		else:
			self.LoginUI.st_Main.setCurrentIndex(room)
		
	def Login_Connect(self):
		self.Login_Goto("connect")
		
	def Login_Connect_SetLokal(self,state):
		if (state>0):
			self.LoginUI.le_Connect_Alamat.setReadOnly(True)
			self.LoginUI.le_Connect_Alamat.setText("localhost")
		else:
			self.LoginUI.le_Connect_Alamat.setReadOnly(False)
	
	def Login_Redraw(self):
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		self.fr_Login_Frame.setGeometry(QtCore.QRect(0,0,WinW,WinH))
		
	
	def Login_Test(self):
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		print WinW,WinH

	def Login_Connect_Act_OK(self):
		self.dbHost = str(self.LoginUI.le_Connect_Alamat.text())
		self.Login_Database()

	def Login_Database(self):
		self.Login_Goto("Database")
		sql = "SHOW DATABASES"
		
		

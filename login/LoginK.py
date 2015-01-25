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
		if (self.dbHost.lower().find("localhost") != -1):
			self.dbHost = "127.0.0.1"
		self.Login_Database()

	def Login_Database(self):
		self.Login_Goto("Database")
		self.dbUser = "gd_user_akunting"
		self.dbPassword = "nyungsep"
		databases = self.DatabaseRunQuery("SHOW DATABASES")
		for x in range(len(databases)):
			if (str(databases[x][0]).find("gd_db_") != -1):
				tb_data = self.LoginUI.scontent_Database_List.findChild(QtGui.QPushButton,"dtb_Login_Database_List"+str(x))
				if (tb_data == None):
					tb_data = QtGui.QPushButton(self.LoginUI.scontent_Database_List)
					tb_data.setObjectName("dtb_Login_Database_List"+str(x))
					tb_data.setText(str(databases[x][0]))
					self.LoginUI.ivl_Database_ListContent.addWidget(tb_data)
					tb_data.clicked.connect(functools.partial(self.Login_Database_SetDatabase,databases[x][0]))
	def Login_Database_SetDatabase(self,dbname):
		self.dbDatabase = dbname
		self.Login_Done()
		
	def Login_Done(self):
		""" done from login, exit the login frame"""
		self.fr_Login_Frame.close()

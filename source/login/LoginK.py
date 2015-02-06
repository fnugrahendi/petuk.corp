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
import md5 #-- hashing buat password

from login_ui import  Ui_fr_Main
from Admin import Admin

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
		self.Login_Login_Password_Inputed = ""
		#-- password echo
		self.LoginUI.le_Login_Password.setEchoMode(QtGui.QLineEdit.Password)
		self.LoginUI.le_Login_Password_Confirm.setEchoMode(QtGui.QLineEdit.Password)
		#-- confirm password
		self.LoginUI.lb_Login_Password_Confirm.hide()
		self.LoginUI.le_Login_Password_Confirm.hide()
		
		
		
		aatime = QtCore.QTimer(self)
		aatime.timeout.connect(self.Login_Redraw)
		aatime.start(500)
		
		
		#-- signal
		self.LoginUI.chk_Connect_Lokal.stateChanged.connect(self.Login_Connect_SetLokal)
		self.LoginUI.le_Login_User.editingFinished.connect(self.Login_SaveLastLogin)
		
		self.LoginUI.tb_Connect_Ok.clicked.connect(self.Login_Connect_Act_OK)
		self.LoginUI.tb_Login_Ok.clicked.connect(self.Login_Login_Auth)
		
		
		self.INDEX_ST_LOGIN = ["CONNECT","LOGIN","DATABASE"]
		#--- end Login_init
		
		self.Login_Connect()
	
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

	def Login_Connect_Act_OK(self):
		self.dbHost = str(self.LoginUI.le_Connect_Alamat.text())
		if (self.dbHost.lower().find("localhost") != -1):
			self.dbHost = "127.0.0.1"
		self.Login_Database()

	def Login_Database(self):
		self.Login_Goto("Database")
		self.dbUser = "gd_user_akunting"
		self.dbPassword = "nyungsep"
		self.dbDatabase = "INFORMATION_SCHEMA" #-- mandatory, sql connect ask for database name, we open INFORMATION_SCHEMA database at first to escape the error
		databases = self.DatabaseRunQuery("SHOW DATABASES")
		for x in range(len(databases)):
			if (str(databases[x][0]).find("gd_db_") != -1):
				tb_data = self.LoginUI.scontent_Database_List.findChild(QtGui.QPushButton,"dtb_Login_Database_List"+str(x))
				if (tb_data == None):
					tb_data = QtGui.QPushButton(self.LoginUI.scontent_Database_List)
					tb_data.setObjectName("dtb_Login_Database_List"+str(x))
					tb_data.setText(str(databases[x][0]).replace("gd_db_",""))
					self.LoginUI.ivl_Database_ListContent.addWidget(tb_data)
					tb_data.clicked.connect(functools.partial(self.Login_Database_SetDatabase,databases[x][0]))
			else:
				#--- create database baru 
				pass
	def Login_Database_SetDatabase(self,dbname):
		self.dbDatabase = dbname
		
		#--- recalculate users, super Mandatory!
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_user';")
		self.Login_User_Field = list(itertools.chain.from_iterable(result))
		
		self.Login_Login()
	
	def Login_SaveLastLogin(self):
		lastlogin = str(self.LoginUI.le_Login_User.text())
		self.GarvinSetConfig("Last Login",lastlogin)
	
	def Login_Login(self):
		self.Login_Goto("Login")
		
		#~ self.GarvinSetConfig("Last Login","sukimin ingin login namun dia kesusahan karena belum punya userid")
		#~ LastLogin = self.userdata.
		
		self.LoginUI.le_Login_User.clear()
		self.LoginUI.le_Login_Password.clear()
		self.LoginUI.le_Login_Password_Confirm.clear()
		self.Login_Login_Password_Inputed = ""
		users = self.DatabaseFetchResult(self.dbDatabase,"gd_user","level",0)
				
		if len(users)<1:
			#--- Create user and password for admin!
			self.LoginUI.le_Login_User.setText("admin")
			developernote = functools.partial(self.DataMaster_Popup,"Note for Developer (Andrew & E-Qraw) : \nCheck ulang apakah field password di table gd_user bertipe varchar(64)!",self.DataMaster_None)
			self.DataMaster_Popup("User admin belum ada! silahkan beri user dan password untuk admin!",self.DataMaster_None,500,300,developernote)
			self.LoginUI.lb_Login_Password_Confirm.show()
			self.LoginUI.le_Login_Password_Confirm.show()
			self.GarvinDisconnect(self.LoginUI.tb_Login_Ok.clicked)
			self.LoginUI.tb_Login_Ok.clicked.connect(self.Login_Login_CreateAdmin)
		else:
			self.LoginUI.lb_Login_Password_Confirm.hide()
			self.LoginUI.le_Login_Password_Confirm.hide()
			#--- signal tombol sudah di sambungkan di init
			self.GarvinDisconnect(self.LoginUI.tb_Login_Ok.clicked)
			self.GarvinDisconnect(self.LoginUI.le_Login_Password.returnPressed)
			self.GarvinDisconnect(self.LoginUI.le_Login_User.returnPressed)
			self.LoginUI.tb_Login_Ok.clicked.connect(self.Login_Login_Auth)
			self.LoginUI.le_Login_Password.returnPressed.connect(self.Login_Login_Auth)
			self.LoginUI.le_Login_User.returnPressed.connect(self.Login_Login_Auth)
		
		lastlogin = self.GarvinGetConfig("Last Login")
		self.LoginUI.le_Login_User.setText(lastlogin)
		
	
	def Login_Login_CreateAdmin(self):
		user = str(self.LoginUI.le_Login_User.text())
		password = str(self.LoginUI.le_Login_Password_Confirm.text())
		if (password==str(self.LoginUI.le_Login_Password.text())):
			self.Login_Login_CreateUser(user,password,"0") #-- "0" = level admin
		else:
			self.DataMaster_Popup("Password yang anda masukkan tidak sama",self.DataMaster_None)
		
		
	def Login_Login_HashPassword(self,username,password):
		""" hash password, it uses username for word twisting so it will take that for parameter too 
			Note : hashing format shouldn't be changed in the future (as if users have made with previous format)
		"""
		kode = md5.md5
		#-- the format
		return kode(str(username).lower()+kode(str(password)).hexdigest()+str(username).upper()).hexdigest()
		
	def Login_Login_CreateUser(self,username,password,level):
		""" Create user, with parameters: unique username, (unhashed/plain) password, and level """
		hashedpassword = self.Login_Login_HashPassword(username,password)
		sukses = self.DatabaseInsertAvoidreplace(self.dbDatabase,"gd_user","username",username,
										["id","username","password","level","lastActivity"],
										["NULL",username,hashedpassword,str(level),"CURRENT_TIMESTAMP"]
										,"User dengan nama "+username+" sudah digunakan, gunakan nama user lain!")
		if (sukses):
			self.DataMaster_Popup("User "+username+" berhasil dibuat.",self.DataMaster_None)
			#--- succeed. then we hide the confirm, and get the room to login
			self.LoginUI.lb_Login_Password_Confirm.hide()
			self.LoginUI.le_Login_Password_Confirm.hide()
			self.Login_Login()
	
	def Login_Login_Auth(self):
		#~ print self.Login_Login_Password_Inputed
		#~ sql = "SELECT * FROM `gd_user` WHERE `username` LIKE 'askljn' AND `password` LIKE 'sakjn'"
		username = str(self.LoginUI.le_Login_User.text())
		password = self.Login_Login_HashPassword(username,str(self.LoginUI.le_Login_Password.text()))
		cucok = self.DatabaseFetchResult(self.dbDatabase,"gd_user",["username","password"],[username,password])
		if (len(cucok)>0):
			LEVELFIELD = 3
			if (int(cucok[0][LEVELFIELD])==0):
				self.Login_Admin()
			self.Login_Done()
		else:
			self.DataMaster_Popup("Username atau password salah",self.DataMaster_None)
		
	
	def Login_Done(self):
		""" done from login, exit the login frame"""
		self.fr_Login_Frame.close()
		self.GarvinInit()
	
	def Login_Admin(self):
		#--- construct an admin 
		self.Admin = Admin(self)
		
		pass
	
	

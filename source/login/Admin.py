import MySQLdb
from PyQt4 import QtCore
from PyQt4 import QtGui
import functools
import itertools
import re
from datetime import datetime
import md5 #-- hashing buat password

from admin_ui import Ui_fr_Admin

class Admin(object):
	def __init__(self,parent):
		parent.tab_Admin = QtGui.QWidget()
		parent.tab_Admin.setObjectName("tab_Admin")
		parent.ivl_Admin = QtGui.QVBoxLayout(parent.tab_Admin)
		parent.ivl_Admin.setObjectName("ivl_Admin")
		parent.fr_Admin = QtGui.QFrame(parent.tab_Admin)
		parent.fr_Admin.setFrameShape(QtGui.QFrame.StyledPanel)
		parent.fr_Admin.setFrameShadow(QtGui.QFrame.Raised)
		parent.fr_Admin.setObjectName("fr_Admin")
		parent.ivl_Admin.addWidget(parent.fr_Admin)
		parent.tabWidget.addTab(parent.tab_Admin, "Admin")
		
		self.si_om = parent
		
		self.INDEX_ST = ["MENU","LIST USER"]
		
		self.UI = Ui_fr_Admin()
		self.UI.setupUi(parent.fr_Admin) #-- widih mantab banget broh
		self.UI.tb_TutupAdmin.clicked.connect(self.__exit__) #-- test exit
		self.UI.tb_ListUser.clicked.connect(self.ListUser) #-- test exit
		
		
	def Goto(self,room):
		if (type(room)==str):
			if (room.upper() in self.INDEX_ST):
				self.UI.st_Admin.setCurrentIndex(self.INDEX_ST.index(room.upper()))
		elif (type(room)==int):
			self.UI.st_Admin.setCurrentIndex(room)
	
	def __exit__(self):
		self.si_om.tab_Admin.close()
		self.si_om.tabWidget.removeTab(5) #-- soft code this parameter so that it will make sure which tab is removed??

	
	def ListUser(self):
		self.Goto("List User")
		self.si_om.clearTable(self.UI.tbl_ListUser_List)
		KOLOMTABLE = ["username", "password", "level"]
		users = self.si_om.DatabaseFetchResult(self.si_om.dbDatabase,"gd_user")
		for row in xrange(len(users)):
			self.UI.tbl_ListUser_List.insertRow(row)
			for kolom in xrange(len(KOLOMTABLE)):
				if (self.UI.tbl_ListUser_List.item(row,kolom)==None):
					item = QtGui.QTableWidgetItem()
					self.UI.tbl_ListUser_List.setItem(row,kolom,item)
					item.setText(str(users[row][self.si_om.Login_User_Field.index(KOLOMTABLE[kolom])]))
		self.UI.tbl_ListUser_List.setColumnWidth(0,300)
		self.UI.tbl_ListUser_List.setColumnWidth(1,400)
		self.UI.tbl_ListUser_List.setColumnWidth(2,100)
		
		
		def setactiveindex(row,column):
			self.ListUser_RowColumnTerpilih = [row,column]
		
		def tambahbaris():
			newrow = self.UI.tbl_ListUser_List.rowCount()
			self.UI.tbl_ListUser_List.insertRow(newrow)
			for x in range(len(KOLOMTABLE)):
				if (self.UI.tbl_ListUser_List.item(newrow,x)==None):
					item = QtGui.QTableWidgetItem()
					self.UI.tbl_ListUser_List.setItem(newrow, x, item)
			
		def deletecertainrow():
			baris = self.ListUser_RowColumnTerpilih[0]
			if baris<0:
				return
			namauser = str(self.UI.tbl_ListUser_List.itemAt(baris,KOLOMTABLE.index("username")).text())
			self.si_om.DatabaseRunQuery("DELETE FROM `gd_user` WHERE `gd_user`.`username` LIKE '"+namauser+"' ;")
			self.UI.tbl_ListUser_List.removeRow(baris)
			
			
		def confirmdeletecertainrow():
			""" show popup to delete certain row, if user make sure, commit the delete with deletecertainrow"""
			baris = self.ListUser_RowColumnTerpilih[0]
			if (baris<0):
				return
			self.si_om.DataMaster_Popup("Anda yakin akan menghapus data baris "+str(baris+1)+"?",deletecertainrow)
		
		self.si_om.GarvinDisconnect(self.UI.tb_Users_Tambah.clicked)
		self.si_om.GarvinDisconnect(self.UI.tbl_ListUser_List.cellClicked)
		self.si_om.GarvinDisconnect(self.UI.tb_Users_Hapus.clicked)
		self.UI.tb_Users_Tambah.clicked.connect(tambahbaris)
		self.UI.tbl_ListUser_List.cellClicked.connect(setactiveindex)
		self.UI.tb_Users_Hapus.clicked.connect(confirmdeletecertainrow)
	
		

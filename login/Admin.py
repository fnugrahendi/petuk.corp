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
			#~ 
		#~ for row in range(0,len(result)):
				#~ if (row in idies):
					#~ continue
				#~ self.KasBankUI.tbl_KasMasuk.insertRow(row)
				#~ idies.append(row)
				#~ for kolom in range(0,len(TABLECOLUMNS[1])):
					#~ if (self.KasBankUI.tbl_KasMasuk.item(row,kolom)==None):
						#~ item = QtGui.QTableWidgetItem()
						#~ self.KasBankUI.tbl_KasMasuk.setItem(row, kolom, item)
					#~ self.KasBankUI.tbl_KasMasuk.item(row,kolom).setText(str(result[row][	field(TABLECOLUMNS[1][kolom])	]))

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
		
		self.UI = Ui_fr_Admin()
		self.UI.setupUi(parent.fr_Admin) #-- widih mantab banget broh
		self.UI.pushButton.clicked.connect(self.__exit__) #-- test exit
	
	def __exit__(self):
		self.si_om.tab_Admin.close()
		self.si_om.tabWidget.removeTab(5) #-- soft code this parameter so that it will make sure which tab is removed??


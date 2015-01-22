import MySQLdb
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSvg
from PyQt4.QtCore import * #nganggo QDateTime, ra apal e package ngarepe opo QtCore.QDateTime rung nyobo
from PyQt4.QtGui import *
import sip #lali nggo ngopo
import sys,os
import functools #partial
import itertools #ubah tuple ke array
import re #regular expression
from datetime import datetime #tanggal, a= datetime.now(); cobo dicheck dir(a); a.year,

from ui_kasbank import Ui_st_KasBank
from KasMasuk import KasMasuk


class KasBank(KasMasuk):
	def KasBank_init(self,parent=None):
		
		self.INDEX_ST_KASBANK_MENU = 0
		self.INDEX_ST_KASBANK_KASMASUK = 1
		self.INDEX_ST_KASBANK_KASMASUK_TAMBAH = 2
		self.INDEX_ST_KASBANK_KASKELUAR = 3
		self.INDEX_ST_KASBANK_KASKELUAR_TAMBAH = 4
		
		self.INDEX_ST_KASBANK = ["MENU", "KASMASUK", "KASMASUK_TAMBAH", "KASKELUAR", "KASKELUAR_TAMBAH"]
		
		self.st_kasbank = QtGui.QStackedWidget(self.tab_KasBank)
		self.KasBankUI = Ui_st_KasBank()
		self.KasBankUI.setupUi(self.st_kasbank)
		self.tab_KasBank.findChild(QtGui.QVBoxLayout).addWidget(self.st_kasbank)
		
		#--- after KasBankUI this is the line where init should be invoked
		super(KasBank,self).__init__(parent)
		
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_kas_masuk';")
		self.KasBank_KasMasuk_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_detail_kas_masuk';")
		self.KasBank_DetailKasMasuk_Field = list(itertools.chain.from_iterable(result))
		
		#--- menu signal
		self.KasBankUI.tb_Menu_KasMasuk.clicked.connect(self.KasBank_KasMasuk)
	
	def KasBank_Goto(self,roomindex):
		if (type(roomindex)==str):
			#-- do the find. which each page is no more than a widget (not to be confused with QStackedWidget with st_ name)
			idx = self.INDEX_ST_KASBANK.index(roomindex.upper())
			if roomindex<0:
				return False
			self.st_kasbank.setCurrentIndex(idx)
			print "masuk ke "+roomindex
		else:
			self.st_kasbank.setCurrentIndex(roomindex)
		return True
	def KasBank_Menu(self):
		self.KasBank_Goto("MENU")

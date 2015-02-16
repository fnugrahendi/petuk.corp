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
from KasKeluar import KasKeluar
from BankMasuk import BankMasuk
from BankKeluar import BankKeluar

class KasBank(KasMasuk,KasKeluar,BankMasuk,BankKeluar):
	def KasBank_init(self,parent=None):
		
		self.INDEX_ST_KASBANK_MENU = 0
		self.INDEX_ST_KASBANK_KASMASUK = 1
		self.INDEX_ST_KASBANK_KASMASUK_TAMBAH = 2
		self.INDEX_ST_KASBANK_KASKELUAR = 3
		self.INDEX_ST_KASBANK_KASKELUAR_TAMBAH = 4
		
		self.INDEX_ST_KASBANK = ["MENU", "KASMASUK", "KASMASUK_TAMBAH", "KASKELUAR", "KASKELUAR_TAMBAH", "BANKMASUK", "BANKMASUK_TAMBAH", "BANKKELUAR", "BANKKELUAR_TAMBAH"]
		
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
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_kas_keluar';")
		self.KasBank_KasKeluar_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_detail_kas_keluar';")
		self.KasBank_DetailKasKeluar_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_bank_keluar';")
		self.KasBank_BankKeluar_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_bank_masuk';")
		self.KasBank_BankMasuk_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_detail_bank_keluar';")
		self.KasBank_DetailBankKeluar_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_detail_bank_masuk';")
		self.KasBank_DetailBankMasuk_Field = list(itertools.chain.from_iterable(result))
		
		
		
		#--- menu signal
		self.KasBankUI.tb_Menu_KasMasuk.clicked.connect(self.KasBank_KasMasuk)
		self.KasBankUI.tb_Menu_KasKeluar.clicked.connect(self.KasBank_KasKeluar)
		self.KasBankUI.tb_Menu_BankMasuk.clicked.connect(self.KasBank_BankMasuk)
		self.KasBankUI.tb_Menu_BankKeluar.clicked.connect(self.KasBank_BankKeluar)
		
		#--- validators
		
		#--- set certain validator
		lineedits = self.tab_KasBank.findChildren(QtGui.QLineEdit)
		for lineedit in lineedits:
			self.GarvinValidate(lineedit) #-- default : huruf, angka, spasi, titik, dash
		self.GarvinValidate(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor,"[cdCD0-9]+")
		self.GarvinValidate(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor,"[crCR0-9]+")
		self.GarvinValidate(self.KasBankUI.le_KasMasuk_Search,"search")
		self.GarvinValidate(self.KasBankUI.le_KasKeluar_Search,"search")
	
	def KasBank_Goto(self,roomindex):
		if (type(roomindex)==str):
			#-- do the find. which each page is no more than a widget (not to be confused with QStackedWidget with st_ name)
			idx = self.INDEX_ST_KASBANK.index(roomindex.upper())
			if idx<0:
				return False
			self.st_kasbank.setCurrentIndex(idx)
		else:
			self.st_kasbank.setCurrentIndex(roomindex)
		return True
	def KasBank_Menu(self):
		self.KasBank_Goto("MENU")

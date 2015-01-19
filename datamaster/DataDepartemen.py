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

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class DataDepartemen(object):
	def __init__(self, parent=None):
		print "Data departemen init invoked!"
		
	def DataMaster_DataDepartemen_RefreshList(self):
		"""sql karena sinyal je, threading bro, most updated value comes by sql"""
		self.clearLayout(self.scontent_DataMaster_DataDepartemen_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_data_departemen","namaDepartemen","%"+str(self.le_DataMaster_DataDepartemen_Search.text()+"%"))
		#~ result = self.DatabaseRunQuery(sql)
		tinggi = len(result)*80
		self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
		for x in range(0,len(result)):
			Tb_ListDepartemen = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataDepartemen_List"+str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")]))
			if (len(Tb_ListDepartemen)<1):
				Tb_Departemen = QtGui.QPushButton(self.scontent_DataMaster_DataDepartemen_Fbody_Slist)
				Tb_Departemen.setObjectName(_fromUtf8("dtb_DataMaster_DataDepartemen_ListDepartemen"+str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")])))
				local_name = str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")])
				Tb_Departemen.setText(local_name)
				self.ivl_DataMaster_DataDepartemen_Fbody_Slist.addWidget(Tb_Departemen,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				Tb_Departemen.clicked.connect(functools.partial(self.DataMaster_DataDepartemen_DrawInfo,result[x]))
			else:
				for y in range(0, len(Tb_ListDepartemen)):
					self.ivl_DataMaster_DataDepartemen_Fbody_Slist.addWidget(Tb_ListDepartemen[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
					Tb_ListDepartemen[y].show()
					Tb_ListDepartemen[y].setText(str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")]))
					self.GarvinDisconnect(Tb_ListDepartemen[y].clicked)
					Tb_ListDepartemen[y].clicked.connect(functools.partial(self.DataMaster_DataDepartemen_DrawInfo,result[x]))
	
	def DataMaster_DataDepartemen(self):
		self.st_DataMaster.setCurrentIndex(self.INDEX_ST_DATAMASTER_DATADEPARTEMEN)
		self.lb_DataMaster_DataDepartemen_Judul.setText("Data Departemen ")
		self.tb_DataMaster_DataDepartemen_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATADEPARTEMEN_TAMBAH))
		self.tb_DataMaster_DataDepartemen_Edit.clicked.connect(self.DataMaster_DataDepartemen_Edit)
		self.clearLayout(self.scontent_DataMaster_DataDepartemen_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		self.GarvinDisconnect(self.le_DataMaster_DataDepartemen_Search.textChanged)
		self.le_DataMaster_DataDepartemen_Search.textChanged.connect(self.DataMaster_DataDepartemen_RefreshList)
		#~ self.le_DataMaster_DataDepartemen_Tambah_KodeDepartemen.setReadOnly(False)
		#~ if (not keep):
			#~ """Kosongkan isi line edit"""
			#~ lels = self.fr_DataMaster_DataDepartemen_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
			#~ for x in range(0,len(lels)):
				#~ lels[x].setText("")
		
		#~ self.DataMaster_DataDepartemen_Tambah_GenerateKode()
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_data_departemen` "
		result = self.DatabaseRunQuery(sql)
		tinggi = len(result)*65
		self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
		for x in range(0,len(result)):
			Tb_ListDepartemen = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataDepartemen_List"+str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")]))
			if (len(Tb_ListDepartemen)<1):
				Tb_Departemen = QtGui.QPushButton(self.scontent_DataMaster_DataDepartemen_Fbody_Slist)
				Tb_Departemen.setObjectName(_fromUtf8("dtb_DataMaster_DataDepartemen_ListDepartemen"+str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")])))
				local_name = str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")])
				Tb_Departemen.setText(local_name)
				self.ivl_DataMaster_DataDepartemen_Fbody_Slist.addWidget(Tb_Departemen,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				Tb_Departemen.clicked.connect(functools.partial(self.DataMaster_DataDepartemen_DrawInfo,result[x]))
			else:
				for y in range(0, len(Tb_ListDepartemen)):
					self.ivl_DataMaster_DataDepartemen_Fbody_Slist.addWidget(Tb_ListDepartemen[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
					Tb_ListDepartemen[y].show()
					Tb_ListDepartemen[y].setText(str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")]))
					self.GarvinDisconnect(Tb_ListDepartemen[y].clicked)
					Tb_ListDepartemen[y].clicked.connect(functools.partial(self.DataMaster_DataDepartemen_DrawInfo,result[x]))
		self.GarvinDisconnect(self.tb_DataMaster_DataDepartemen_Tutup.clicked)
		self.GarvinDisconnect(self.tb_DataMaster_DataDepartemen_Tambah.clicked)
		self.GarvinDisconnect(self.tb_DataMaster_DataDepartemen_Edit.clicked)
		self.GarvinDisconnect(self.tb_DataMaster_DataDepartemen_Delete.clicked)
		self.tb_DataMaster_DataDepartemen_Tutup.clicked.connect(self.DataMaster_Menu)
		self.tb_DataMaster_DataDepartemen_Tambah.clicked.connect(self.DataMaster_DataDepartemen_Tambah)
		#~ self.tb_DataMaster_DataDepartemen_Tutup.clicked.connect(tulis)
	#~ def DataMaster_DataDepartemen_DrawInfo(self,data):
		
	
	def DataMaster_DataDepartemen_Edit(self):
		pass
	def DataMaster_DataDepartemen_DrawInfo(self,data):
		fdepartemen = self.DataMaster_DataDepartemen_Field.index
		#------------------ Draw Form Layout Left
		FrameDepartemenL = self.findChildren(QtGui.QFrame,"dfr_DataMaster_DataDepartemen_FrameInfo_Left")
		if (len(FrameDepartemenL)<1):
			FrameDepartemenL = QtGui.QFrame(self.fr_DataMaster_DataDepartemen_Fbody_FR_Ftop)
			FrameDepartemenL.setObjectName(_fromUtf8("dfr_DataMaster_DataDepartemen_FrameInfo_Left"))
			FrameDepartemenL.setStyleSheet(_fromUtf8("QFrame{background:#FFFFFF;border-radius:0px;border-style: solid;border-width: 0px;border-color:#FFFFFF;}"))
			ivl_FrameDepartemenL = QtGui.QVBoxLayout(FrameDepartemenL)
			ivl_FrameDepartemenL.setObjectName(_fromUtf8("divl_DataMaster_DataDepartemen_FrameInfo_Left"))
		
		else:
			FrameDepartemenL = FrameDepartemenL[0]
			#~ ivl_FrameDepartemenL = ivl_FrameDepartemenL[0]
		self.igr_DataMaster_DataDepartemen_Fbody_FR_Ftop.addWidget(FrameDepartemenL, 0, 0, 1, 1)
		FrameDepartemenL.setMaximumSize(QtCore.QSize(150,15000))
		
		#------------------ Draw Form Layout Right
		FrameDepartemenR = self.findChildren(QtGui.QFrame,"dfr_DataMaster_DataDepartemen_FrameInfo_Right")
		if (len(FrameDepartemenR)<1):
			FrameDepartemenR = QtGui.QFrame(self.fr_DataMaster_DataDepartemen_Fbody_FR_Ftop)
			FrameDepartemenR.setObjectName(_fromUtf8("dfr_DataMaster_DataDepartemen_FrameInfo_Right"))
			FrameDepartemenR.setStyleSheet(_fromUtf8("QFrame{background:#FFFFFF;border-radius:0px;border-style: solid;border-width: 0px;border-color:#FFFFFF;}"))
			ivl_FrameDepartemenR = QtGui.QVBoxLayout(FrameDepartemenR)
			ivl_FrameDepartemenR.setObjectName(_fromUtf8("divl_DataMaster_DataDepartemen_FrameInfo_Right"))
		else:
			FrameDepartemenR = FrameDepartemenR[0]
			#~ ivl_FrameDepartemenR = ivl_FrameDepartemenR[0]
		self.igr_DataMaster_DataDepartemen_Fbody_FR_Ftop.addWidget(FrameDepartemenR, 0, 1, 1, 1)
		
		self.clearLayout(FrameDepartemenL.findChild(QtGui.QVBoxLayout))
		self.clearLayout(FrameDepartemenR.findChild(QtGui.QVBoxLayout))
		
		
		#-------------------Frame Bawah (graphic)
		
		FrameGrafik = self.findChildren(QtGui.QFrame,_fromUtf8("dfr_DataMaster_DataDepartemen_FrameGrafik"))
		if len(FrameGrafik)<1:
			FrameGrafik = QtGui.QFrame(self.fr_DataMaster_DataDepartemen_Fbody_FR_Ftop)
			FrameGrafik.setObjectName(_fromUtf8("dfr_DataMaster_DataDepartemen_FrameGrafik"))
			FrameGrafik.setStyleSheet(_fromUtf8("QFrame{background:#FFFFFF;border-radius:0px;border-style: solid;border-width: 1px;border-color:#E1E1E1;}"))
		else:
			FrameGrafik = FrameGrafik[0]
		self.igr_DataMaster_DataDepartemen_Fbody_FR_Ftop.addWidget(FrameGrafik, 1, 0, 1, 2)
		
		
		#-------------------Draw labels
		#------------------ semua raceto gara2 Form Layout ra ono remove row, nganggo ivl sidane, soft coding ra dadi
		objecttag = "dlb_"
		roomname = "DataMaster_DataDepartemen_"
		tablename = "gd_data_departemen"
		specialfield = ["parentDepartemen","kodePenjab"]
		specialfieldvalue = [
								["gd_data_departemen","kodeDepartemen",
								self.DataMaster_DataDepartemen_Field.index("namaDepartemen")],
								["gd_nama_alamat","kodePelanggan",
								self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]
							]
		#---- Makin try to use regex 18 Jan 2015
		regexlabel = QRegExp("("+objecttag+""+roomname+"\d+\w+)")
		Labels = self.findChildren(QtGui.QLabel,regexlabel)
		if len(Labels)<1:
			"""
				Label di form layout:
				
				Label   |  LabelValue
				Label   |  LabelValue
				Label   |  LabelValue
			"""
			l = QtGui.QLabel(FrameDepartemenL)
			l.setObjectName(objecttag+""+roomname+"1Nama___Departemen") #---- angka ini urutan di formlayout
			l = QtGui.QLabel(FrameDepartemenR)
			l.setObjectName(objecttag+""+roomname+"V_1namaDepartemen") #--- Yang ini label Value, berisi nilai dari nama label
																				#----- _V_(URUTAN)(NAMAFIELD)
			l = QtGui.QLabel(FrameDepartemenL)
			l.setObjectName(objecttag+""+roomname+"2Kode___Departemen")
			l = QtGui.QLabel(FrameDepartemenR)
			l.setObjectName(objecttag+""+roomname+"V_2kodeDepartemen")
			
			l = QtGui.QLabel(FrameDepartemenL)
			l.setObjectName(objecttag+""+roomname+"3Departemen___Induk")
			l = QtGui.QLabel(FrameDepartemenR)
			l.setObjectName(objecttag+""+roomname+"V_3parentDepartemen")
			
			l = QtGui.QLabel(FrameDepartemenL)
			l.setObjectName(objecttag+""+roomname+"4Penanggung___Jawab")
			l = QtGui.QLabel(FrameDepartemenR)
			l.setObjectName(objecttag+""+roomname+"V_4kodePenjab")
			
			l = QtGui.QLabel(FrameDepartemenL)
			l.setObjectName(objecttag+""+roomname+"5Catatan")
			l = QtGui.QLabel(FrameDepartemenR)
			l.setObjectName(objecttag+""+roomname+"V_5catatan")
			
			
			#---- now we refresh the labels
			Labels = self.findChildren(QtGui.QLabel,regexlabel)
		
		#~ self.clearLayout(FrameDepartemenL.findChild(QtGui.QVBoxLayout))
		for label in Labels:
			#---fetch text dari format dlb_"+roomname+"(PRINT TEXT)
			text = re.findall(objecttag+""+roomname+"\d+(\w+)",str(label.objectName())).pop().replace("___"," ")
			label.setText(text)
			nomor = int(re.findall(objecttag+""+roomname+"(\d+)\w+",str(label.objectName())).pop())
			FrameDepartemenL.findChild(QtGui.QVBoxLayout).addWidget(label)
			label.show()
		
		#~ FrameDepartemenL.findChild(QtGui.QVBoxLayout).addItem(QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
			
		#---- this ought to be success at this line as it built along labels 
		ValueLabels = self.findChildren(QtGui.QLabel,QRegExp("("+objecttag+""+roomname+"V_\d+\w+)"))
		#~ self.clearLayout(FrameDepartemenR.findChild(QtGui.QVBoxLayout))
		for vlabel in ValueLabels:
			nomor = int(re.findall(objecttag+""+roomname+"V_(\d+)\w+",str(vlabel.objectName())).pop())
			fieldname = re.findall(objecttag+""+roomname+"V_\d+(\w+)",str(vlabel.objectName())).pop()
			text = ""
			try:
				x = specialfield.index(fieldname)
				text = ": "+str(self.DatabaseRunQuery("SELECT * FROM `"+specialfieldvalue[x][0]+\
											"` WHERE `"+specialfieldvalue[x][1]+"` LIKE '"+data[fdepartemen(fieldname)]+"'")[0][specialfieldvalue[x][2]])
			except:
				text = ": "+data[fdepartemen(fieldname)]
			vlabel.setText(text)
			FrameDepartemenR.findChild(QtGui.QVBoxLayout).addWidget(vlabel)
			vlabel.show()
		#~ FrameDepartemenR.findChild(QtGui.QVBoxLayout).addItem(QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
			
			
		#---end of def DataMaster_DataDepartemen_DrawInfo
	
	def DataMaster_DataDepartemen_Popup_Pilih(self,dipilih,fcb_ok=False, fcb_cancel=False, hideSurrounding=False):
		"""Buka popup untuk pilih datadepartemen, carane hack dewe yoh neng fcb_ok
		"""
		self.GarvinDisconnect(self.le_DataMaster_DataDepartemen_Search.textChanged)
		self.le_DataMaster_DataDepartemen_Search.textChanged.connect(self.DataMaster_DataDepartemen_RefreshList)
		
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		#--- fungsi exit:kembalikan
		def revertDataDepartemen():
			self.fr_DataMaster_DataDepartemen_Fbody_Slist_Container.setParent(self.fr_DataMaster_DataDepartemen_Fbody)
			self.ihl_DataMaster_DataDepartemen_Fbody.insertWidget(0,self.fr_DataMaster_DataDepartemen_Fbody_Slist_Container,1)
			self.fr_DataMaster_DataDepartemen_Fbody_Slist_Container.show()
		
		#------ Is it weak reference? when will python's garbage collector delete this revertDataDepartemen()?
		#--- set to none
		if (fcb_ok==False):
			fcb_ok = self.DataMaster_None
		if (fcb_cancel==False):
			fcb_cancel = self.DataMaster_None
		
		#--- bila arraykosong
		if len(dipilih)<1:
			dipilih.append("-")
		
		def ubahDipilih(data):
			""" karena threading, bisa ngubah pakai fungsi: nunggu fungsi dipanggil"""
			dipilih[0] = data
			revertDataDepartemen()
		
		
		#--- Popup dipanggil dulu, baru dimanipulasi isinya
		#thanks to function_exit
		self.DataMaster_Popup("",fcb_ok,360,WinH-250,revertDataDepartemen,False,True)
		
		
		FrameWindow = self.findChild(QtGui.QFrame,"DataMaster_Popup_FrameWindow")
		PopupW = FrameWindow.geometry().width()
		PopupH = FrameWindow.geometry().height()
		self.fr_DataMaster_DataDepartemen_Fbody_Slist_Container.setParent(FrameWindow)
		self.fr_DataMaster_DataDepartemen_Fbody_Slist_Container.show()
		self.fr_DataMaster_DataDepartemen_Fbody_Slist_Container.setGeometry(QtCore.QRect(5,5,PopupW-5,PopupH-50))
		
		#Hapus layout list, buat baru
		self.clearLayout(self.scontent_DataMaster_DataDepartemen_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_data_departemen")
		tinggi = len(result)*80
		#~ self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMinimumSize(QtCore.QSize(330, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMinimumSize(QtCore.QSize(330, 600))
		#~ self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMaximumSize(QtCore.QSize(330, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataDepartemen_Fbody_Slist.setMaximumSize(QtCore.QSize(330, 600))
		for x in range(0,len(result)):
			Tb_ListDepartemen = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataDepartemen_List"+str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")]))
			if (len(Tb_ListDepartemen)<1):
				Tb_Departemen = QtGui.QPushButton(self.scontent_DataMaster_DataDepartemen_Fbody_Slist)
				Tb_Departemen.setObjectName(_fromUtf8("dtb_DataMaster_DataDepartemen_ListDepartemen"+str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")])))
			else:
				Tb_Departemen = Tb_ListDepartemen[0]

			local_name = str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")])
			Tb_Departemen.setText(local_name)
			Tb_Departemen.show()
			self.ivl_DataMaster_DataDepartemen_Fbody_Slist.addWidget(Tb_Departemen)
			self.GarvinDisconnect(Tb_Departemen.clicked)
			Tb_Departemen.clicked.connect(functools.partial(ubahDipilih,str(result[x][self.DataMaster_DataDepartemen_Field.index("kodeDepartemen")])))
			Tb_Departemen.clicked.connect(self.DataMaster_Popup_Tutup)
			Tb_Departemen.clicked.connect(fcb_ok)
        
		#~ Tb_ListDepartemen = self.findChildren(QtGui.QPushButton,QRegExp("dynamic_tb_DataMaster_DataDepartemen_List\w+"))
		
	def DataMaster_DataDepartemen_Tambah(self, clear=False):
		self.st_DataMaster.setCurrentIndex(self.INDEX_ST_DATAMASTER_DATADEPARTEMEN_TAMBAH)
		
		if (not clear):
			self.DataMaster_DataDepartemen_Tambah_GenerateKode()
		
		self.GarvinDisconnect(self.tb_DataMaster_DataDepartemen_Tambah_Batal.clicked)
		self.GarvinDisconnect(self.tb_DataMaster_DataDepartemen_Tambah_Simpan.clicked)
		self.tb_DataMaster_DataDepartemen_Tambah_Simpan.clicked.connect(self.DataMaster_DataDepartemen_Tambah_Act_Simpan)
		self.tb_DataMaster_DataDepartemen_Tambah_Batal.clicked.connect(self.DataMaster_DataDepartemen)
		return #--- end Tambah
	
	def DataMaster_DataDepartemen_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_data_departemen` ORDER BY `gd_data_departemen`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<8):
			kode_default = "0"+kode_default
		self.le_DataMaster_DataDepartemen_KodeDepartemen.setText(kode_default)
		return #--- end generate kode

	def DataMaster_DataDepartemen_Tambah_Act_Simpan(self):
		kode = self.le_DataMaster_DataDepartemen_KodeDepartemen.text()
		nama = self.le_DataMaster_DataDepartemen_NamaDepartemen.text()
		induk = self.le_DataMaster_DataDepartemen_ParentDepartemen.text()
		penjab = self.le_DataMaster_DataDepartemen_KodePenjab.text()
		catatan = self.le_DataMaster_DataDepartemen_Catatan.text()
		
		return #-- end simpan

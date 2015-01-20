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

class DataProyek(object):
	def __init__(self, parent=None):
		pass
	
	def DataMaster_DataProyek_Delete(self):
		try:
			kode = str(self.lb_DataMaster_DataProyek_Kode.text()).replace("\n","")
		except:
			return
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_proyek` WHERE `gd_proyek`.`kodeProyek` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPROYEK)
	
	
	def DataMaster_DataProyek_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataProyek_Tambah_KodeProyek, 
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_proyek` ORDER BY `gd_proyek`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = "PROYEK" + "."+kode_default
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setText(kode_default)
	
	def DataMaster_DataProyek_DrawInfo(self,data):
		field = self.DataMaster_DataProyek_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		
		f12b = QtGui.QFont()
		f12b.setPointSize(9)
		f12b.setBold(False)
		f12b.setItalic(False)
		f12b.setWeight(50)
		
		f12i = QtGui.QFont()
		f12i.setPointSize(9)
		f12i.setBold(False)
		f12i.setItalic(True)
		f12i.setWeight(50)
		common_width = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()/3
		
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			self.lb_DataMaster_DataProyek_Nama.setText(data[field("namaProyek")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_Nama.show()
		except:
			self.lb_DataMaster_DataProyek_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_Nama.setText(data[field("namaProyek")])
			self.lb_DataMaster_DataProyek_Nama.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Nama.setMaximumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Nama.setFont(f14)
		
		#--------------------------------------------------------------------------------------------------------Kode
		try:
			self.lb_DataMaster_DataProyek_Kode.setText(data[field("kodeProyek")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_Kode.show()
		except:
			self.lb_DataMaster_DataProyek_Kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_Kode.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_Kode.setText(data[field("kodeProyek")])
			self.lb_DataMaster_DataProyek_Kode.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Kode.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Kode.setFont(f12b)
		
		#--------------------------------------------------------------------------------------------------------Penjab
		try:
			sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+str(data[field("kodePenjab")])+"'"
			try:
				penjab = str(self.DatabaseRunQuery(sql)[0][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
			except:
				penjab = "Mohon perbarui data"
			self.lb_DataMaster_DataProyek_Penjab.setText("Penanggung Jawab: "+penjab)
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_Penjab, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_Penjab.show()
		except:
			self.lb_DataMaster_DataProyek_Penjab = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_Penjab.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Penjab"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Penjab, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			
			sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+str(data[field("kodePenjab")])+"'"
			try:
				penjab = str(self.DatabaseRunQuery(sql)[0][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
			except:
				penjab = "Mohon perbarui data"
			
			self.lb_DataMaster_DataProyek_Penjab.setText("Penanggung Jawab: "+penjab)
			self.lb_DataMaster_DataProyek_Penjab.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Penjab.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Kode.setFont(f12)
		
		#--------------------------------------------------------------------------------------------------------TMulai
		try:
			self.lb_DataMaster_DataProyek_TMulai.setText("Tanggal Mulai: "+str(data[field("tanggalMulai")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_TMulai, 2, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_TMulai.show()
		except:
			self.lb_DataMaster_DataProyek_TMulai = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_TMulai.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_TMulai"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_TMulai, 2, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_TMulai.setText("Tanggal Mulai: "+str(data[field("tanggalMulai")]))
			self.lb_DataMaster_DataProyek_TMulai.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_TMulai.setMaximumSize(QtCore.QSize(common_width, 22))
		
		
		#--------------------------------------------------------------------------------------------------------TSelesai
		try:
			self.lb_DataMaster_DataProyek_TSelesai.setText("Tanggal Selesai: "+str(data[field("tanggalSelesai")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_TSelesai, 3, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_TSelesai.show()
		except:
			self.lb_DataMaster_DataProyek_TSelesai = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_TSelesai.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_TSelesai"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_TSelesai, 3, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_TSelesai.setText("Tanggal Selesai: "+str(data[field("tanggalSelesai")]))
			self.lb_DataMaster_DataProyek_TSelesai.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_TSelesai.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------AnggaranTotal
		try:
			self.lb_DataMaster_DataProyek_AnggaranTotal.setText("Anggaran Total: "+str(data[field("anggaranTotal")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_AnggaranTotal, 2, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_AnggaranTotal.show()
		except:
			self.lb_DataMaster_DataProyek_AnggaranTotal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_AnggaranTotal.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_AnggaranTotal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_AnggaranTotal, 2, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_AnggaranTotal.setText("Anggaran Total: "+str(data[field("anggaranTotal")]))
			self.lb_DataMaster_DataProyek_AnggaranTotal.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_AnggaranTotal.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------RealisasiTotal
		try:
			self.lb_DataMaster_DataProyek_RealisasiTotal.setText("Realisasi Total: "+str(data[field("realisasiTotal")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_RealisasiTotal, 3, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_RealisasiTotal.show()
		except:
			self.lb_DataMaster_DataProyek_RealisasiTotal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_RealisasiTotal.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_RealisasiTotal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_RealisasiTotal, 3, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_RealisasiTotal.setText("Realisasi Total: "+str(data[field("realisasiTotal")]))
			self.lb_DataMaster_DataProyek_RealisasiTotal.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_RealisasiTotal.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------Progress
		try:
			self.pb_DataMaster_DataProyek_Progress.setProperty("value", data[field("progress")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.pb_DataMaster_DataProyek_Progress, 0, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.pb_DataMaster_DataProyek_Progress.show()
		except:
			self.pb_DataMaster_DataProyek_Progress = QtGui.QProgressBar(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.pb_DataMaster_DataProyek_Progress.setProperty("value", data[field("progress")])
			self.pb_DataMaster_DataProyek_Progress.setObjectName(_fromUtf8("pb_DataMaster_DataProyek_Progress"))
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.pb_DataMaster_DataProyek_Progress, 0, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.pb_DataMaster_DataProyek_Progress.setMinimumSize(QtCore.QSize(100, 22))
			self.pb_DataMaster_DataProyek_Progress.setMaximumSize(QtCore.QSize(100, 22))
			
			#~ self.lb_DataMaster_DataProyek_Progress = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			#~ self.lb_DataMaster_DataProyek_Progress.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Progress"))
			#~ self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Progress, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			#~ self.lb_DataMaster_DataProyek_Progress.setText(data[field("kodeProgress")])
			#~ self.lb_DataMaster_DataProyek_Progress.setMinimumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Progress.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Kode.setFont(f12)
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataProyek_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataProyek_FGraph.show()
				#~ print "no rebuild"
				
		except:
			self.fr_DataMaster_DataProyek_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataProyek_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataProyek_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataProyek_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataProyek_FGraph"))
			self.fr_DataMaster_DataProyek_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataProyek_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataProyek_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataProyek_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataProyek_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataProyek_FGraph)
			self.ihl_DataMaster_DataProyek_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataProyek_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataProyek_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataProyek_FGraph"))
			
			svgW = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()-100
			svgH = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().height()/2
			svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					"<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#444444; fill: #ffffff'/>"+\
					"<rect x='"+str(10+0*svgW/6)+"' y='"+str(-10+svgH-100)+"' height='100' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
					"<rect x='"+str(10+1*svgW/6)+"' y='"+str(-10+svgH-200)+"' height='200' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
				"</svg>"
			f = open("./img/DataMaster_svg.svg","w")
			f.write(svg)
			f.close()
			
			self.svg_DataMaster_DataProyek_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataProyek_FGraph)
			self.svg_DataMaster_DataProyek_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataProyek_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			
		self.DataMaster_CommonRoom_cleared = 0
		try:
			self.tb_DataMaster_DataCommon_Delete.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataProyek_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataProyek_Delete,500,200,None,None))
	
	
	def DataMaster_DataProyek_Edit(self):
		field = self.DataMaster_DataProyek_Field.index
		try:
			kode = str(self.lb_DataMaster_DataProyek_Kode.text()).replace("\n","")
		except:
			return
		sql = "SELECT * FROM `gd_proyek` WHERE `kodeProyek` = '"+kode+"' LIMIT 0 , 1"
		proyek = self.DatabaseRunQuery(sql)[0]
		
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setText(_fromUtf8(kode))
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setReadOnly(True)
		self.le_DataMaster_DataProyek_Tambah_NamaProyek.setText(proyek[field("namaProyek")])
		self.tb_DataMaster_DataProyek_Tambah_KodePenjab.setText(proyek[field("kodePenjab")])
		#~ sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+proyek[field("kodePenjab")]+"'"
		#~ try:
			#~ penjab = self.DatabaseRunQuery(sql)[0][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]
		#~ except:
			#~ penjab = "Mohon perbarui data"
		#~ self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setText(penjab)
		self.dsb_DataMaster_DataProyek_Tambah_Progress.setValue(float(proyek[field("progress")]))
		self.dte_DataMaster_DataProyek_Tambah_TanggalMulai.setDateTime(QDateTime.fromString(str(proyek[field("tanggalMulai")]),"yyyy-MM-dd hh:mm:ss"))
		self.dte_DataMaster_DataProyek_Tambah_TanggalSelesai.setDateTime(QDateTime.fromString(str(proyek[field("tanggalSelesai")]),"yyyy-MM-dd hh:mm:ss"))
		self.le_DataMaster_DataProyek_Tambah_AnggaranTotal.setText(str(proyek[field("anggaranTotal")]))
		self.le_DataMaster_DataProyek_Tambah_RealisasiTotal.setText(str(proyek[field("realisasiTotal")]))
		self.chk_DataMaster_DataProyek_Tambah_PakaiFase.setCheckState(	int(proyek[field("isFase")])*2	)
		self.DataMaster_DataProyek_Edit_idEDIT = proyek[field("id")]
		self.DataMaster_DataProyek_Tambah()
		
	
	def DataMaster_DataProyek_Tambah(self):
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAPROYEK_TAMBAH)
		self.GarvinDisconnect(self.tb_DataMaster_DataProyek_Tambah_KodePenjab.clicked)
		self.tb_DataMaster_DataProyek_Tambah_KodePenjab.clicked.connect(self.DataMaster_DataProyek_Tambah_PilihPenjab)
		pass
	
	def DataMaster_DataProyek_Tambah_PilihPenjab(self):
		data = []
		def isi():
			self.tb_DataMaster_DataProyek_Tambah_KodePenjab.setText(str(data[0]))
		def batal():
			self.tb_DataMaster_DataProyek_Tambah_KodePenjab.setText("-")
		self.DataMaster_DataNamaAlamat_Popup_Pilih(data,isi,batal)
		
	def DataMaster_DataProyek_Tambah_Act_Simpan(self):
		kode = str(self.le_DataMaster_DataProyek_Tambah_KodeProyek.text())
		nama = str(self.le_DataMaster_DataProyek_Tambah_NamaProyek.text())
		penjab = str(self.tb_DataMaster_DataProyek_Tambah_KodePenjab.text())
		progress = str(self.dsb_DataMaster_DataProyek_Tambah_Progress.value())
		tmulai = str(self.dte_DataMaster_DataProyek_Tambah_TanggalMulai.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		tslsai = str(self.dte_DataMaster_DataProyek_Tambah_TanggalSelesai.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		anggaran =str(self.le_DataMaster_DataProyek_Tambah_AnggaranTotal.text())
		realisasi=str(self.le_DataMaster_DataProyek_Tambah_RealisasiTotal.text())
		pakaifase= str("1" if (self.chk_DataMaster_DataProyek_Tambah_PakaiFase.checkState()>0) else "0")
		
		if (self.DataMaster_DataProyek_Edit_idEDIT>=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_proyek` "+\
			"SET `kodeProyek` = '"+kode+"',"+\
				"`namaProyek` = '"+nama+"',"+\
				"`kodePenjab` = '"+penjab+"',"+\
				"`progress` = '"+progress+"',"+\
				"`tanggalMulai` = '"+tmulai+"',"+\
				"`tanggalSelesai` = '"+tslsai+"',"+\
				"`anggaranTotal` = '"+anggaran+"',"+\
				"`realisasiTotal` = '"+realisasi+"',"+\
				"`isFase` = '"+pakaifase+"'"+\
			"WHERE `gd_proyek`.`id`='"+str(self.DataMaster_DataProyek_Edit_idEDIT)+"'"
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_proyek`"+\
				" (`id`, `kodeProyek`, `namaProyek`, `kodePenjab`, `progress`, `tanggalMulai`, `tanggalSelesai`, `anggaranTotal`, `realisasiTotal`, `isFase`) "+\
				"VALUES (NULL, '"+kode+"', '"+nama+"', '"+penjab+"', "+progress+", '"+tmulai+"', '"+tslsai+"', '"+anggaran+"', '"+realisasi+"', "+pakaifase+");"
		self.DatabaseRunQuery(sql)
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setReadOnly(False)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPROYEK)
	
	#show list DataProyek
	def DataMaster_DataProyek_Tambah_Showlist(self):
		self.sc_DataMaster_DataProyek_Tambah_Penjab.show()
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setPlaceholderText("Type to search")
		
	def DataMaster_DataProyek_Tambah_Showlist_Change(self):
		self.lb_DataMaster_DataProyek_Tambah_PilihPenjab.show()
		self.sc_DataMaster_DataProyek_Tambah_Penjab.show()
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setPlaceholderText("Type to search")
		#~ self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setCompleter(
		
		if self.sc_DataMaster_DataProyek_Tambah_Penjab.isVisible():
			self.clearLayout(self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0])
			self.initDatabase()
			cursor = self.db.cursor()
			if str(self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.text()) != "":
				self.clearLayout(self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0])
				sql = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '%"+str(self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.text())+"%' "
			else:
				sql = "SELECT * FROM `gd_nama_alamat` "
			cursor.execute(sql)
			result = cursor.fetchall()
			for x in range(0,len(result)):
				Button = self.findChildren(QtGui.QPushButton,"tb_DataMaster_DataProyek_Penjab_Find"+str(x))
				if len(Button)<1:
					Button = QtGui.QPushButton(self.scontent_DataMaster_DataProyek_Tambah_Penjab)
					local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
					Button.setObjectName(_fromUtf8("tb_DataMaster_DataProyek_Penjab_Find"+str(x)))
					Button.setText(local_name)
					self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0].addWidget(Button,(QtCore.Qt.AlignTop | QtCore.Qt.AlignTop))
					Button.clicked.connect(functools.partial(self.DataMaster_DataProyek_Tambah_Showlist_Selected,result[x]))
				else:
					Button = Button[0]
					local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
					Button.setText(local_name)
					self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0].addWidget(Button,(QtCore.Qt.AlignTop | QtCore.Qt.AlignTop))
					Button.clicked.disconnect()
					Button.clicked.connect(functools.partial(self.DataMaster_DataProyek_Tambah_Showlist_Selected,result[x]))
					Button.show()
			self.db.close()
		#~ self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.
	
	def DataMaster_DataProyek_Tambah_Showlist_Selected(self,data):
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setText(data[self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
		self.le_DataMaster_DataProyek_Tambah_KodePenanggungJawab.setText(data[self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")])
	

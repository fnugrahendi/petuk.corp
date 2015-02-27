from PyQt4 import QtCore
from PyQt4 import QtGui

class DataMasterStyling(object):
	def __init__(self,parent):
		self.si_om = parent
		
	def DataMaster_Styling_Apply(self):
		#-- set button text to empty for styling
		menus = self.si_om.fr_DataMaster_Menu.findChildren(QtGui.QPushButton)
		for button in menus:
			button.setText("") #-- clear text
			button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #-- set cursor
		self.si_om.tb_DataMaster_DataNamaAlamat.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/nama_alamat.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/nama_alamat1.png');
			}
			""")
			
		self.si_om.tb_DataMaster_DataProduk.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/produk.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/produk1.png');
			}
			""")
		self.si_om.tb_DataMaster_DataPajak.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/pajak.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/pajak1.png');
			}
			""")
		self.si_om.tb_DataMaster_DataProyek.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/proyek.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/proyek1.png');
			}
			""")
		self.si_om.tb_DataMaster_DataSatuanPengukuran.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/pengukuran.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/pengukuran1.png');
			}
			""")
		self.si_om.tb_DataMaster_DataRekening.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/rekening.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/rekening1.png');
			}
			""")
		self.si_om.tb_DataMaster_DataDepartemen.setStyleSheet(""" 
			QPushButton{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/departemen.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+self.si_om.BasePath+"""image/datamaster_menu/departemen1.png');
			}
			""")
		print "background-image: url('"+self.si_om.BasePath+"image/datamaster_menu/nama_alamat.png');"

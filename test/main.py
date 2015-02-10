import os,sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import functools
import itertools
import re
from subprocess import Popen 

from MainWindow import Ui_MainWindow

class MainGUI(QtGui.QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None):
		super(MainGUI,self).__init__(parent)
		self.setupUi(self)
		self.showFullScreen()
		
		self.fr_Logo.setStyleSheet("QFrame{background-image: url(:/Login/img/LogoMedium.png);}")
		
	#~ background-image: url(:/DataMaster/img/edit.png);
		self.tb_DataMaster_DataCommon_Edit = QtGui.QPushButton(self.centralwidget)
		self.tb_DataMaster_DataCommon_Edit.setMinimumSize(QtCore.QSize(30, 30))
		self.tb_DataMaster_DataCommon_Edit.setMaximumSize(QtCore.QSize(30, 16777215))
		self.tb_DataMaster_DataCommon_Edit.setStyleSheet("")
		self.tb_DataMaster_DataCommon_Edit.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/Login/img/LogoMedium.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
		self.tb_DataMaster_DataCommon_Edit.setIcon(icon)
		self.tb_DataMaster_DataCommon_Edit.setObjectName("tb_DataMaster_DataCommon_Edit")
		self.igr_centralwidget.addWidget(self.tb_DataMaster_DataCommon_Edit)
		self.GarvinGridTab(self.centralwidget,self.igr_centralwidget)
		self.GarvinGridTab(self.fr_Layouttest,self.ifl_Layouttest)

	def GarvinGridTab(self,widget,layout):
		if type(layout)==QtGui.QGridLayout or type(layout)==QtGui.QFormLayout:
			if type(layout)==QtGui.QGridLayout:
				kolom = layout.columnCount()
				baris = layout.rowCount()
				pilih = layout.itemAtPosition
			else:
				kolom = 2
				baris = layout.rowCount()
				pilih = layout.itemAt
				
			LineEdits = []
			for y in range(0,baris):
				for x in range(0,kolom):
					item = pilih(y,x)
					if (item!=None):
						if type(item.widget())==QtGui.QLineEdit:
							#~ print item.widget().objectName()
							LineEdits.append(item.widget())
			for x in range(1,len(LineEdits)):
				widget.setTabOrder(LineEdits[x-1],LineEdits[x])
    
	def Quit(self):
		exit()
	
	def GarvinDisconnect(self,stuff):
		"nyimpel2ke disconnect signal, cara manggil koyo self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked)"
		try:
			stuff.disconnect()
			return True
		except:
			return False

	
if __name__=="__main__":
	#-- data
	Path = str(__file__).replace("main.py","").replace("\\","/")
	DataPath = Path+"../data/"

	loginrcpath = Path+"../image/"+"Image_rc.py"
	resfile = open(loginrcpath)
	resource = resfile.read()
	resfile.close()
	resource = resource[:resource.find("def qInitResources")]
	exec(resource)
	QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

	app = QtGui.QApplication(sys.argv)
	w = MainGUI()
	sys.exit(app.exec_())

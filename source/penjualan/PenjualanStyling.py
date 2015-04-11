from PyQt4 import QtCore
from PyQt4 import QtGui

class PenjualanStyling(object):
	def __init__(self,parent):
		self.si_om = parent
	
	def Apply(self):
		P = self.si_om
		
		menus = P.fr_Penjualan_Menu.findChildren(QtGui.QPushButton)
		for button in menus:
			button.setText("") #-- clear text
			button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #-- set cursor
		
		P.tb_Penjualan_OrderPenjualan.setStyleSheet("""
			QPushButton{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/order.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/order1.png');
			}""")
		
		P.tb_Penjualan_Invoice.setStyleSheet("""
			QPushButton{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/invoice.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/invoice1.png');
			}""")
			
		P.tb_Penjualan_UangMuka.setStyleSheet("""
			QPushButton{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/uangmuka.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/uangmuka1.png');
			}""")
			
		P.tb_Penjualan_Piutang.setStyleSheet("""
			QPushButton{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/piutang.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/piutang1.png');
			}""")
			
		P.tb_Penjualan_JurnalMemorial.setStyleSheet("""
			QPushButton{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/memorial.png');
			background-repeat:no-repeat;
			width:160px;height:195px;
			}
			QPushButton::hover{
			background-image: url('"""+P.BasePath+"""image/penjualan_menu/memorial1.png');
			}""")



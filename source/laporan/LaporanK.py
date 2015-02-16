import MySQLdb
import xlsxwriter
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSvg
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sip 
import sys,os
import functools
import itertools
import re
from datetime import datetime

###--- from L_BukuBesar_DTJ import L_BukuBesar_DTJ, this one will be dumped, not be used
#~ from html import HTML
from ui_laporan import Ui_st_Laporan


class Laporan(object):
	def __init__(self,parent=None):
		super(Laporan,self).__init__(parent)
		pass #-- doesn't triggered
		
	def Laporan_init(self,si_om=None):
		self.st_Laporan = QtGui.QStackedWidget(self.tab_KasBank)
		self.LaporanUI = Ui_st_Laporan()
		self.LaporanUI.setupUi(self.st_Laporan)
		self.tab_Laporan.findChild(QtGui.QVBoxLayout).addWidget(self.st_Laporan)
		#-- after main init
		super(Laporan,self).__init__(si_om)
		
		self.INDEX_ST_LAPORAN = ["MENU", "LAPORAN KAS HARIAN", "LAPORAN LABA RUGI", "LAPORAN NERACA"]
		
		self.Laporan_Goto("LAPORAN LABA RUGI")
	
	def Laporan_Goto(self,namaroom):
		if (type(namaroom)==str):
			#-- do the find. which each page is no more than a widget (not to be confused with QStackedWidget with st_ name)
			idx = self.INDEX_ST_LAPORAN.index(namaroom.upper())
			if idx<0:
				return False
			self.st_Laporan.setCurrentIndex(idx)
		else:
			self.st_Laporan.setCurrentIndex(namaroom)
		return True
	
	def Laporan_Neraca(self, data):
		#--- CARA MASUK KE MENU:
		#--- 
		
		pass
		
	def Laporan_BuktiBankMasuk(self,data):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Bank Masuk '+data+'.xlsx')
		#~ workbook = xlsxwriter.Workbook(self.DataPath+"merge_rich_string.xlsx") #-- apike neng folder data kro
		
		worksheet = workbook.add_worksheet()

		# Set up some formats to use.
		#~ red = workbook.add_format({'color': 'red', 'bold' : 'true'})
		#~ blue = workbook.add_format({'color': 'blue'})
		#~ cell_format = workbook.add_format({'align': 'right',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 2,
										   #~ 'color':'blue',
										   #~ 'bold':'true'})
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatBeriTerima = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatBiasa = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTotal = workbook.add_format({'align': 'right',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'right':0,
										   'font_size':'12'})

		formatAngkaTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})

		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:H2', "BUKTI BANK", formatJudul)
		worksheet.write(1,8, 'Nomor', formatNoTgl)
		worksheet.write(2,8, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_bank_masuk` WHERE kodeTransaksi LIKE '"+data+"'"
		result = self.DatabaseRunQuery(sql)
		#durung digawe ben bisa pilihan
		kodeTransaksi = data;
		
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][2].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "BANK MASUK", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : ", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)

		# We then overwrite the first merged cell with a rich string. Note that we
		# must also pass the cell format used in the merged cells format at the end.
		#~ worksheet.set_column(0,0,45);
		#~ worksheet.write_formula('A'+str(ax+1),'=SUM('+'A'+str(awal)+':'+'A'+str(ax)+')')
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_bank_masuk` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_bank_masuk`.`noAkunDetail` WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][6], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][3], formatBiasa)
			total = total +  int(result[x][3])
		worksheet.merge_range('B'+str(index+1)+':H'+str(index+1), "TOTAL : ", formatTotal)
		worksheet.merge_range('I'+str(index+1)+':K'+str(index+1), "=SUM(I"+str(8)+":K"+str(index)+")", formatBiasa)
		
		worksheet.merge_range('B'+str(index+2)+':C'+str(index+2), "Terbilang", formatTerbilang)
		worksheet.merge_range('D'+str(index+2)+':K'+str(index+2), ": "+self.Terbilang(total), formatAngkaTerbilang)
		
		worksheet.merge_range('B'+str(index+3)+':C'+str(index+3), "Cheque/Giro", formatTerbilang)
		worksheet.merge_range('D'+str(index+3)+':K'+str(index+3), ":", formatAngkaTerbilang)
				
		worksheet.merge_range('B'+str(index+4)+':C'+str(index+4), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+4)+':E'+str(index+4), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+4)+':G'+str(index+4), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+4)+':K'+str(index+4), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index+5)+':C'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+5)+':E'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+5)+':G'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+5)+':I'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+5)+':K'+str(index+9), "", formatJudulTandaTangan)
		
		
		workbook.close()
		return

	def Laporan_BuktiKasMasuk(self,data):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Kas Masuk.xlsx')
		worksheet = workbook.add_worksheet()

		# Set up some formats to use.
		#~ red = workbook.add_format({'color': 'red', 'bold' : 'true'})
		#~ blue = workbook.add_format({'color': 'blue'})
		#~ cell_format = workbook.add_format({'align': 'right',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 2,
										   #~ 'color':'blue',
										   #~ 'bold':'true'})
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatBeriTerima = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatBiasa = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTotal = workbook.add_format({'align': 'right',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'right':0,
										   'font_size':'12'})

		formatAngkaTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})

		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:H2', "BUKTI KAS", formatJudul)
		worksheet.write(1,8, 'Nomor', formatNoTgl)
		worksheet.write(2,8, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_kas_masuk` "
		result = self.DatabaseRunQuery(sql)
		#durung digawe ben bisa pilihan
		kodeTransaksi = result[0][1];
		
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][2].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "KAS MASUK", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : ", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)

		# We then overwrite the first merged cell with a rich string. Note that we
		# must also pass the cell format used in the merged cells format at the end.
		#~ worksheet.set_column(0,0,45);
		#~ worksheet.write_formula('A'+str(ax+1),'=SUM('+'A'+str(awal)+':'+'A'+str(ax)+')')
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_kas_masuk` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_kas_masuk`.`noAkunDetail` WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][6], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][3], formatBiasa)
			total = total +  int(result[x][3])
		worksheet.merge_range('B'+str(index+1)+':H'+str(index+1), "TOTAL : ", formatTotal)
		worksheet.merge_range('I'+str(index+1)+':K'+str(index+1), "=SUM(I"+str(8)+":K"+str(index)+")", formatBiasa)
		
		worksheet.merge_range('B'+str(index+2)+':C'+str(index+2), "Terbilang", formatTerbilang)
		worksheet.merge_range('D'+str(index+2)+':K'+str(index+2), ": "+self.Terbilang(total), formatAngkaTerbilang)
		
		worksheet.merge_range('B'+str(index+3)+':C'+str(index+3), "Cheque/Giro", formatTerbilang)
		worksheet.merge_range('D'+str(index+3)+':K'+str(index+3), ":", formatAngkaTerbilang)
				
		worksheet.merge_range('B'+str(index+4)+':C'+str(index+4), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+4)+':E'+str(index+4), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+4)+':G'+str(index+4), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+4)+':K'+str(index+4), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index+5)+':C'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+5)+':E'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+5)+':G'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+5)+':I'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+5)+':K'+str(index+9), "", formatJudulTandaTangan)
		
		
		workbook.close()
		return

	def Laporan_BuktiBankKeluar(self,data):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Bank  Keluar.xlsx')
		worksheet = workbook.add_worksheet()

		# Set up some formats to use.
		#~ red = workbook.add_format({'color': 'red', 'bold' : 'true'})
		#~ blue = workbook.add_format({'color': 'blue'})
		#~ cell_format = workbook.add_format({'align': 'right',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 2,
										   #~ 'color':'blue',
										   #~ 'bold':'true'})
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatBeriTerima = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatBiasa = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTotal = workbook.add_format({'align': 'right',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'right':0,
										   'font_size':'12'})

		formatAngkaTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})

		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:H2', "BUKTI BANK", formatJudul)
		worksheet.write(1,8, 'Nomor', formatNoTgl)
		worksheet.write(2,8, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_bank_keluar` "
		result = self.DatabaseRunQuery(sql)
		#durung digawe ben bisa pilihan
		kodeTransaksi = result[0][1];
		
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][2].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "BANK KELUAR", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : ", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)

		# We then overwrite the first merged cell with a rich string. Note that we
		# must also pass the cell format used in the merged cells format at the end.
		#~ worksheet.set_column(0,0,45);
		#~ worksheet.write_formula('A'+str(ax+1),'=SUM('+'A'+str(awal)+':'+'A'+str(ax)+')')
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_bank_keluar` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_bank_keluar`.`noAkunDetail` WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][6], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][3], formatBiasa)
			total = total +  int(result[x][3])
		worksheet.merge_range('B'+str(index+1)+':H'+str(index+1), "TOTAL : ", formatTotal)
		worksheet.merge_range('I'+str(index+1)+':K'+str(index+1), "=SUM(I"+str(8)+":K"+str(index)+")", formatBiasa)
		
		worksheet.merge_range('B'+str(index+2)+':C'+str(index+2), "Terbilang", formatTerbilang)
		worksheet.merge_range('D'+str(index+2)+':K'+str(index+2), ": "+self.Terbilang(total), formatAngkaTerbilang)
		
		worksheet.merge_range('B'+str(index+3)+':C'+str(index+3), "Cheque/Giro", formatTerbilang)
		worksheet.merge_range('D'+str(index+3)+':K'+str(index+3), ":", formatAngkaTerbilang)
				
		worksheet.merge_range('B'+str(index+4)+':C'+str(index+4), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+4)+':E'+str(index+4), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+4)+':G'+str(index+4), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+4)+':K'+str(index+4), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index+5)+':C'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+5)+':E'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+5)+':G'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+5)+':I'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+5)+':K'+str(index+9), "", formatJudulTandaTangan)
		
		
		workbook.close()
		return

	def Laporan_BuktiKasKeluar(self,data):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Kas Keluar.xlsx')
		worksheet = workbook.add_worksheet()
		
		# Set up some formats to use.
		#~ red = workbook.add_format({'color': 'red', 'bold' : 'true'})
		#~ blue = workbook.add_format({'color': 'blue'})
		#~ cell_format = workbook.add_format({'align': 'right',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 2,
										   #~ 'color':'blue',
										   #~ 'bold':'true'})
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatBeriTerima = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatBiasa = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTotal = workbook.add_format({'align': 'right',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'right':0,
										   'font_size':'12'})

		formatAngkaTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})
		
		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:H2', "BUKTI KAS", formatJudul)
		worksheet.write(1,8, 'Nomor', formatNoTgl)
		worksheet.write(2,8, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_kas_keluar` "
		result = self.DatabaseRunQuery(sql)
		#durung digawe ben bisa pilihan
		kodeTransaksi = result[0][1];
		
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][2].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "KAS KELUAR", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : ", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)

		# We then overwrite the first merged cell with a rich string. Note that we
		# must also pass the cell format used in the merged cells format at the end.
		#~ worksheet.set_column(0,0,45);
		#~ worksheet.write_formula('A'+str(ax+1),'=SUM('+'A'+str(awal)+':'+'A'+str(ax)+')')
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_kas_keluar` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_kas_keluar`.`noAkunDetail` WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][6], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][3], formatBiasa)
			total = total +  int(result[x][3])
		worksheet.merge_range('B'+str(index+1)+':H'+str(index+1), "TOTAL : ", formatTotal)
		worksheet.merge_range('I'+str(index+1)+':K'+str(index+1), "=SUM(I"+str(8)+":K"+str(index)+")", formatBiasa)
		
		worksheet.merge_range('B'+str(index+2)+':C'+str(index+2), "Terbilang", formatTerbilang)
		worksheet.merge_range('D'+str(index+2)+':K'+str(index+2), ": "+self.Terbilang(total), formatAngkaTerbilang)
		
		worksheet.merge_range('B'+str(index+3)+':C'+str(index+3), "Cheque/Giro", formatTerbilang)
		worksheet.merge_range('D'+str(index+3)+':K'+str(index+3), ":", formatAngkaTerbilang)
				
		worksheet.merge_range('B'+str(index+4)+':C'+str(index+4), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+4)+':E'+str(index+4), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+4)+':G'+str(index+4), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+4)+':K'+str(index+4), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index+5)+':C'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+5)+':E'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+5)+':G'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+5)+':I'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+5)+':K'+str(index+9), "", formatJudulTandaTangan)
		
		
		workbook.close()
		return

	def Laporan_BuktiMemorial(self,data):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti memorial.xlsx')
		worksheet = workbook.add_worksheet()
		
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatBeriTerima = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatBiasa = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatKeterangan = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatKeteranganTitik = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'right':0,
										   'font_size':'12'})

		formatAngkaTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})
		
		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:H2', "BUKTI MEMORIAL", formatJudul)
		worksheet.write(1,8, 'Nomor', formatNoTgl)
		worksheet.write(2,8, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_jurnal_memorial` "
		result = self.DatabaseRunQuery(sql)
		#durung digawe ben bisa pilihan
		kodeTransaksi = result[0][1];
		
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][2].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('B5:K5', "DEBET : ", formatBeriTerima)

		worksheet.merge_range('B6:C6', "Perkiraan", formatBiasa)
		worksheet.merge_range('D6:H6', "Nama Perkiraan", formatBiasa)
		worksheet.merge_range('I6:K6', "Jumlah", formatBiasa)

		# We then overwrite the first merged cell with a rich string. Note that we
		# must also pass the cell format used in the merged cells format at the end.
		#~ worksheet.set_column(0,0,45);
		#~ worksheet.write_formula('A'+str(ax+1),'=SUM('+'A'+str(awal)+':'+'A'+str(ax)+')')
				
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_jurnal_memorial` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_jurnal_memorial`.`noAkunMemorial` WHERE noReferensi LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+6
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][5], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][10], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][4], formatBiasa)
		
		worksheet.merge_range('B'+str(index+1)+':C'+str(index+1),'Keterangan :',formatKeterangan);
		worksheet.merge_range('D'+str(index+1)+':K'+str(index+1),'........................................................................',formatKeteranganTitik);
		worksheet.merge_range('D'+str(index+2)+':K'+str(index+2),'........................................................................',formatKeteranganTitik);
		worksheet.merge_range('D'+str(index+3)+':K'+str(index+3),'........................................................................',formatKeteranganTitik);
		worksheet.merge_range('D'+str(index+4)+':K'+str(index+4),'........................................................................',formatKeteranganTitik);
				
		worksheet.merge_range('B'+str(index+5)+':K'+str(index+5), "KREDIT : ", formatBeriTerima)

		worksheet.merge_range('B'+str(index+6)+':C'+str(index+6), "Perkiraan", formatBiasa)
		worksheet.merge_range('D'+str(index+6)+':H'+str(index+6), "Nama Perkiraan", formatBiasa)
		worksheet.merge_range('I'+str(index+6)+':K'+str(index+6), "Jumlah", formatBiasa)
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_jurnal_memorial` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_jurnal_memorial`.`noAkunPiutang` WHERE noReferensi LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(sql)
		awal = index+7
		
		for x in range(0,len(result)):
			index1 = x+awal
			print index1
			worksheet.merge_range('B'+str(index1)+':C'+str(index1), result[x][6], formatBiasa)
			worksheet.merge_range('D'+str(index1)+':H'+str(index1), result[x][10], formatBiasa)
			worksheet.merge_range('I'+str(index1)+':K'+str(index1), result[x][4], formatBiasa)
				
		worksheet.merge_range('B'+str(index1+1)+':C'+str(index1+1), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index1+1)+':E'+str(index1+1), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index1+1)+':G'+str(index1+1), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index1+1)+':I'+str(index1+1), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index1+1)+':K'+str(index1+1), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index1+2)+':C'+str(index1+6), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index1+2)+':E'+str(index1+6), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index1+2)+':G'+str(index1+6), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index1+2)+':I'+str(index1+6), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index1+2)+':K'+str(index1+6), "", formatJudulTandaTangan)
				
		workbook.close()
		return

	def Laporan_BuktiInvoice(self,data):
		
		# Create an new Excel file and add a worksheet.
		#~ workbook = xlsxwriter.Workbook(self.DataPath+'BuktiInvoice.xlsx')
		
		#~ simpan = QtGui.QFileDialog()
		#~ namafilesimpan = str(simpan.getSaveFileName())
		#~ workbook = xlsxwriter.Workbook(namafilesimpan)
		workbook = xlsxwriter.Workbook('BuktiInvoice.xlsx')
		worksheet = workbook.add_worksheet()
		
		# Set up some formats to use.
		#~ red = workbook.add_format({'color': 'red', 'bold' : 'true'})
		#~ blue = workbook.add_format({'color': 'blue'})
		#~ cell_format = workbook.add_format({'align': 'right',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 2,
										   #~ 'color':'blue',
										   #~ 'bold':'true'})
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatBeriTerima = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatBeriTerimaKpd = workbook.add_format({'align': 'left',
										   'right':0,
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatBiasa = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTotal = workbook.add_format({'align': 'right',
										   'valign': 'vcenter',
										   'border': 1,
										   'font_size':'12'})

		formatTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'right':0,
										   'font_size':'12'})

		formatAngkaTerbilang = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 1,
										   'left':0,
										   'font_size':'12'})

		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})
		
		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:I2', "BUKTI INVOICE", formatJudul)
		worksheet.write(1,9, 'Nomor', formatNoTgl)
		worksheet.write(2,9, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_invoice_penjualan` JOIN gd_nama_alamat ON gd_nama_alamat.kodePelanggan LIKE gd_invoice_penjualan.kodePelanggan WHERE kodeTransaksi LIKE '"+data+"'"
		result = self.DatabaseRunQuery(sql)
		print sql
		
		kodeTransaksi = data
		
		worksheet.write(1,10, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,10, ': '+(result[0][4].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('E3:H3', "INVOICE", formatSubJudul)
		worksheet.merge_range('B5:D6', "Diberikan Kepada :", formatBeriTerimaKpd)
		worksheet.merge_range('E5:L6', result[0][10], formatBeriTerima)

		worksheet.merge_range('B7:C7', "Kode Produk", formatBiasa)
		worksheet.merge_range('D7:F7', "Keterangan", formatBiasa)
		worksheet.merge_range('G7:H7', "Qty", formatBiasa)
		worksheet.merge_range('I7:J7', "Harga", formatBiasa)
		worksheet.merge_range('K7:L7', "Total", formatBiasa)

		# We then overwrite the first merged cell with a rich string. Note that we
		# must also pass the cell format used in the merged cells format at the end.
		#~ worksheet.set_column(0,0,45);
		#~ worksheet.write_formula('A'+str(ax+1),'=SUM('+'A'+str(awal)+':'+'A'+str(ax)+')')
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_invoice_penjualan` JOIN gd_nama_alamat ON gd_nama_alamat.kodePelanggan LIKE gd_invoice_penjualan.kodePelanggan JOIN gd_order_penjualan ON gd_order_penjualan.kodeTransaksi LIKE gd_invoice_penjualan.kodeTransaksi WHERE gd_invoice_penjualan.kodeTransaksi LIKE '"+data+"'"
		
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][26], formatBiasa)
			worksheet.merge_range('D'+str(index)+':F'+str(index), result[x][5], formatBiasa)
			worksheet.merge_range('G'+str(index)+':H'+str(index), result[x][28], formatBiasa)
			worksheet.merge_range('I'+str(index)+':J'+str(index), result[x][29], formatBiasa)
			worksheet.merge_range('K'+str(index)+':L'+str(index), result[x][32], formatBiasa)
			total = total +  int(result[x][32])
		worksheet.merge_range('B'+str(index+1)+':J'+str(index+1), "TOTAL : ", formatTotal)
		worksheet.merge_range('K'+str(index+1)+':L'+str(index+1), "=SUM(K"+str(8)+":L"+str(index)+")", formatBiasa)
		
		worksheet.merge_range('B'+str(index+2)+':C'+str(index+2), "Terbilang", formatTerbilang)
		worksheet.merge_range('D'+str(index+2)+':L'+str(index+2), ": "+self.Terbilang(total), formatAngkaTerbilang)
		
		worksheet.merge_range('B'+str(index+3)+':C'+str(index+3), "Cheque/Giro", formatTerbilang)
		worksheet.merge_range('D'+str(index+3)+':L'+str(index+3), ":", formatAngkaTerbilang)
				
		worksheet.merge_range('B'+str(index+4)+':C'+str(index+4), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+4)+':E'+str(index+4), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+4)+':G'+str(index+4), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+4)+':L'+str(index+4), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index+5)+':C'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+5)+':E'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+5)+':G'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+5)+':I'+str(index+9), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+5)+':L'+str(index+9), "", formatJudulTandaTangan)
		
		
		workbook.close()
		return

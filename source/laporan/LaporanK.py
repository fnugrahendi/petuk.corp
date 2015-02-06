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

from L_BukuBesar_DTJ import L_BukuBesar_DTJ
from html import HTML


class Laporan(L_BukuBesar_DTJ):
	def __init__(self,parent=None):
		super(Laporan,self).__init__(parent)
		pass #-- doesn't triggered
		
	def Laporan_Init(self):
		super(L_BukuBesar_DTJ,self).__init__(parent)
		
		return
	
	def Laporan_Neraca(self, data):
		
		pass
		
	def Laporan_BuktiBankMasuk(self,data):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('merge_rich_string.xlsx')
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

		worksheet.set_column(1,9,10)
		worksheet.set_column(2,9,10)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_bank_masuk` "
		result = self.DatabaseRunQuery(sql)
		#durung digawe ben bisa pilihan
		kodeTransaksi = result[0][1];
		
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


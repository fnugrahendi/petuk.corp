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

		# We can only write simple types to merged ranges so we write a blank string.
		worksheet.merge_range('D2:H2', "BUKTI BANK", formatJudul)
		worksheet.write(1,8, 'Nomor', formatNoTgl)
		worksheet.write(2,8, 'Tanggal', formatNoTgl)

		worksheet.set_column(1,9,10)
		worksheet.set_column(2,9,10)

		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_bank_masuk` "
		result = self.DatabaseRunQuery(sql)
		kodeTransaksi = result[0][1];
		
		worksheet.write(1,9, ':'+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ':', formatNoTgl)

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
		print sql
		result = self.DatabaseRunQuery(sql)
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][6], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][3], formatBiasa)
			
		workbook.close()
		return


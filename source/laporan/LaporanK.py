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

__BELUM_LUNAS__ = '2'
__LUNAS__ = '1'
__SEMUA__ = '0'

def tabel_kode(data):
	if(data.find('KM')>=0):
		return "gd_kas_masuk"
	elif(data.find('KK')>=0):
		return "gd_kas_keluar"
	elif(data.find('BM')>=0):
		return "gd_bank_masuk"
	elif(data.find('BK')>=0):
		return "gd_bank_keluar"
	elif(data.find('INV')>=0):
		return "gd_invoice_penjualan"
	return

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
		
		self.INDEX_ST_LAPORAN = ["MENU", "LAPORAN KAS HARIAN", "LAPORAN LABA RUGI", "LAPORAN NERACA", "LAPORAN HUTANG PIUTANG", "LAPORAN JUAL BELI"]
		
		#-- signal connect NING KENE, Connect tombol seko room Menu ke fungsi Kontrol bersangkutan
		#~ self.LaporanUI.tb_Menu_Laporan_Neraca.clicked.connect(functools.partial(self.Laporan_Neraca,None))
		self.LaporanUI.tb_Menu_Laporan_KasHarian.clicked.connect(self.Laporan_RKasHarian)
		self.LaporanUI.tb_Menu_Laporan_LabaRugi.clicked.connect(self.Laporan_RLabaRugi)
		self.LaporanUI.tb_Menu_Laporan_Neraca.clicked.connect(self.Laporan_RNeraca)
		self.LaporanUI.tb_Menu_Laporan_HutangPiutangPerusahaan.clicked.connect(self.Laporan_RHutangPiutang)
		self.LaporanUI.tb_Menu_Laporan_JualBeliPerusahaan.clicked.connect(self.Laporan_RJualBeli)
		
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
	
	#~ def Laporan_Neraca(self, data):
		#~ #--- CARA MASUK KE MENU:
		#~ #--- 
		#~ self.Laporan_Goto("LAPORAN NERACA")
		#~ pass
	
	def Laporan_RMenu(self):		
		self.Laporan_Goto("MENU")
				
	def Laporan_BuktiBankMasuk(self,kodeTransaksi):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Bank  Masuk.xlsx')
		worksheet = workbook.add_worksheet()

		idxNilaiDetail = self.KasBank_DetailBankMasuk_Field.index("nilaiDetail")
		idxCatatan = self.KasBank_DetailBankMasuk_Field.index("catatan")
		idxNoAkunDetail = self.KasBank_DetailBankMasuk_Field.index("noAkunDetail")
		
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

		sql = "SELECT tanggal,aDB.kodePelanggan,namaPelanggan,catatan FROM `"+self.dbDatabase+"`.`gd_bank_masuk` as aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan  WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(sql)
		
		print result[0][0],result[0][1],result[0][2]
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][0].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "BANK KELUAR", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : "+result[0][2]+" ("+result[0][1]+")", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_bank_masuk` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_bank_masuk`.`noAkunDetail` JOIN `gd_bank_masuk` ON `gd_bank_masuk`.kodeTransaksi LIKE `gd_detail_bank_masuk`.kodeTransaksi WHERE `gd_detail_bank_masuk`.kodeTransaksi LIKE '"+kodeTransaksi+"'"
		print sql
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][idxNoAkunDetail], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][idxCatatan], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][idxNilaiDetail], formatBiasa)
			total = total +  int(result[x][idxNilaiDetail]) 
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

	def Laporan_BuktiKasMasuk(self,kodeTransaksi):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Kas  Masuk.xlsx')
		worksheet = workbook.add_worksheet()

		idxNilaiDetail = self.KasBank_DetailKasMasuk_Field.index("nilaiDetail")
		idxCatatan = self.KasBank_DetailKasMasuk_Field.index("catatan")
		idxNoAkunDetail = self.KasBank_DetailKasMasuk_Field.index("noAkunDetail")
		
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

		sql = "SELECT tanggal,aDB.kodePelanggan,namaPelanggan,catatan FROM `"+self.dbDatabase+"`.`gd_kas_masuk` as aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan  WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(sql)
		
		print result[0][0],result[0][1],result[0][2]
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][0].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "KAS KELUAR", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : "+result[0][2]+" ("+result[0][1]+")", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_kas_masuk` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_kas_masuk`.`noAkunDetail` JOIN `gd_kas_masuk` ON `gd_kas_masuk`.kodeTransaksi LIKE `gd_detail_kas_masuk`.kodeTransaksi WHERE `gd_detail_kas_masuk`.kodeTransaksi LIKE '"+kodeTransaksi+"'"
		print sql
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][idxNoAkunDetail], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][idxCatatan], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][idxNilaiDetail], formatBiasa)
			total = total +  int(result[x][idxNilaiDetail]) 
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

	def Laporan_BuktiBankKeluar(self,kodeTransaksi):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Bank  Keluar.xlsx')
		worksheet = workbook.add_worksheet()

		idxNilaiDetail = self.KasBank_DetailBankKeluar_Field.index("nilaiDetail")
		idxCatatan = self.KasBank_DetailBankKeluar_Field.index("catatan")
		idxNoAkunDetail = self.KasBank_DetailBankKeluar_Field.index("noAkunDetail")
		
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

		sql = "SELECT tanggal,aDB.kodePelanggan,namaPelanggan,catatan FROM `"+self.dbDatabase+"`.`gd_bank_keluar` as aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan  WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(sql)
		
		print result[0][0],result[0][1],result[0][2]
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][0].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "BANK KELUAR", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : "+result[0][2]+" ("+result[0][1]+")", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_bank_keluar` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_bank_keluar`.`noAkunDetail` JOIN `gd_bank_keluar` ON `gd_bank_keluar`.kodeTransaksi LIKE `gd_detail_bank_keluar`.kodeTransaksi WHERE `gd_detail_bank_keluar`.kodeTransaksi LIKE '"+kodeTransaksi+"'"
		print sql
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][idxNoAkunDetail], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][idxCatatan], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][idxNilaiDetail], formatBiasa)
			total = total +  int(result[x][idxNilaiDetail]) 
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

	def Laporan_BuktiKasKeluar(self,kodeTransaksi):
		
		# Create an new Excel file and add a worksheet.
		workbook = xlsxwriter.Workbook('Bukti Kas  Keluar.xlsx')
		worksheet = workbook.add_worksheet()

		idxNilaiDetail = self.KasBank_DetailKasKeluar_Field.index("nilaiDetail")
		idxCatatan = self.KasBank_DetailKasKeluar_Field.index("catatan")
		idxNoAkunDetail = self.KasBank_DetailKasKeluar_Field.index("noAkunDetail")
		
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

		sql = "SELECT tanggal,aDB.kodePelanggan,namaPelanggan,catatan FROM `"+self.dbDatabase+"`.`gd_kas_keluar` as aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan  WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(sql)
		
		print result[0][0],result[0][1],result[0][2]
		worksheet.write(1,9, ': '+kodeTransaksi, formatNoTgl)
		worksheet.write(2,9, ': '+(result[0][0].strftime("%d-%m-%Y")), formatNoTgl)

		worksheet.merge_range('D3:H3', "KAS KELUAR", formatSubJudul)
		worksheet.merge_range('B5:K6', "Diberikan Kepada : "+result[0][2]+" ("+result[0][1]+")", formatBeriTerima)

		worksheet.merge_range('B7:C7', "Perkiraan", formatBiasa)
		worksheet.merge_range('D7:H7', "Keterangan", formatBiasa)
		worksheet.merge_range('I7:K7', "Jumlah", formatBiasa)
		
		sql = "SELECT * FROM `"+self.dbDatabase+"`.`gd_detail_kas_keluar` JOIN `gd_rekening_jurnal` ON `gd_rekening_jurnal`.`noAkun` LIKE `gd_detail_kas_keluar`.`noAkunDetail` JOIN `gd_kas_keluar` ON `gd_kas_keluar`.kodeTransaksi LIKE `gd_detail_kas_keluar`.kodeTransaksi WHERE `gd_detail_kas_keluar`.kodeTransaksi LIKE '"+kodeTransaksi+"'"
		print sql
		result = self.DatabaseRunQuery(sql)
		total = 0;
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][idxNoAkunDetail], formatBiasa)
			worksheet.merge_range('D'+str(index)+':H'+str(index), result[x][idxCatatan], formatBiasa)
			worksheet.merge_range('I'+str(index)+':K'+str(index), result[x][idxNilaiDetail], formatBiasa)
			total = total +  int(result[x][idxNilaiDetail]) 
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

	def Laporan_RLabaRugi(self):
		"""Kontrol untuk RLabaRugi"""
		self.Laporan_Goto("LAPORAN LABA RUGI")
		#~ self.GarvinDisconnect(self.LaporanUI.tb_Laporan_LabaRugi_KodePelanggan.clicked)
		#~ self.LaporanUI.tb_Laporan_LabaRugi_KodePelanggan.clicked.connect(functools.partial(self.Popup_NamaAlamat,self.LaporanUI.tb_Laporan_LabaRugi_KodePelanggan))
		self.LaporanUI.tb_Laporan_LabaRugi_Cetak.clicked.connect(functools.partial(self.Laporan_LabaRugi))
		self.LaporanUI.tb_Laporan_LabaRugi_Kembali.clicked.connect(self.Laporan_RMenu)
		
	def Laporan_LabaRugi(self):
		tanggalAwal = str(self.LaporanUI.dte_Laporan_LabaRugi_Dari.dateTime().toString("yyyy-MM-dd"))
		tanggalAkhir = str(self.LaporanUI.dte_Laporan_LabaRugi_Sampai.dateTime().toString("yyyy-MM-dd"))
		
		workbook = xlsxwriter.Workbook('LaporanLabaRugi.xlsx')
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

		formatNoTgl = workbook.add_format({'align': 'center',
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

		formatBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatSubBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
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
		worksheet.merge_range('B2:I2', "LAPORAN", formatJudul)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		worksheet.merge_range('B3:I3', "LABA RUGI", formatSubJudul)
		worksheet.merge_range('B4:I4', "PERIODE "+datetime.strptime(tanggalAwal,"%Y-%m-%d").strftime("%d %B %Y")+" - "+datetime.strptime(tanggalAkhir,"%Y-%m-%d").strftime("%d %B %Y"), formatNoTgl)
		
		worksheet.write('B6', "Penjualan", formatBiasa)
		
		#~ //select penjualan
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '4100%' AND '4999%' AND month(tanggal) = 2 GROUP BY noAkun,month(tanggal)"
		
		result = self.DatabaseRunQuery(sql)
		
		worksheet.write('B7', "Penjualan Produk", formatSubBiasa)
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][6], formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa)
		
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H6:I"+str(index)+")", formatBiasa)
		else:	
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		idxPenjualan = 'H'+str(index+1)
			
		index=index+3	
		awal=index+2
		worksheet.write('B'+str(index), "Biaya atas Pendapatan", formatSubBiasa)
		
		#//select biaya Pendapatan
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '5100%' AND '5999%' AND tanggal BETWEEN '"+tanggalAwal+"' AND '"+tanggalAkhir+"' GROUP BY noAkun,month(tanggal)"
		print sql
		result = self.DatabaseRunQuery(sql)
		
		worksheet.write('B'+str(index+1), "Biaya Produksi", formatBiasa)
		for x in range(0,len(result)):
			index = x+awal
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][6], formatBiasa)
				
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H"+str(awal)+":I"+str(index)+")", formatBiasa)
		else:	
			index+=1
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa);
		idxProduksi = 'H'+str(index+1)
			
			
			
		index=index+3	
		awal=index+2
		worksheet.write('B'+str(index), "Pengeluaran Operasional", formatSubBiasa)
		
		#//select biaya operasional
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '6100%' AND '6599%' AND tanggal BETWEEN '"+tanggalAwal+"' AND '"+tanggalAkhir+"' GROUP BY noAkun,month(tanggal)"
		
		result = self.DatabaseRunQuery(sql)
		
		worksheet.write('B'+str(index+1), "Biaya Operasional", formatBiasa)
		for x in range(0,len(result)):
			index = x+awal
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][6], formatBiasa)
				
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H"+str(awal)+":I"+str(index)+")", formatBiasa)
		else:	
			index+=1
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa);
		idxOperasional = 'H'+str(index+1)
			
			
			
		index=index+3	
		awal=index+2
		worksheet.write('B'+str(index), "Pendapatan Lain", formatSubBiasa)
		
		#//select Pendapatan Lain2
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '7100%' AND '7599%' AND tanggal BETWEEN '"+tanggalAwal+"' AND '"+tanggalAkhir+"' GROUP BY noAkun,month(tanggal)"
		
		result = self.DatabaseRunQuery(sql)
		
		worksheet.write('B'+str(index+1), "Biaya Operasional", formatBiasa)
		for x in range(0,len(result)):
			index = x+awal
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][6], formatBiasa)
				
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H"+str(awal)+":I"+str(index)+")", formatBiasa)
		else:	
			index+=1
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa);
		idxPendapatanLain = 'H'+str(index+1)
			
			
		index=index+3	
		awal=index+2
		worksheet.write('B'+str(index), "Pengeluaran Lain", formatSubBiasa)
		
		#//select pengeluaran lain
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '7600%' AND '7999%' AND tanggal BETWEEN '"+tanggalAwal+"' AND '"+tanggalAkhir+"' GROUP BY noAkun,month(tanggal)"
		
		result = self.DatabaseRunQuery(sql)
		
		worksheet.write('B'+str(index+1), "Pengeluaran  Lain", formatBiasa)
		for x in range(0,len(result)):
			index = x+awal
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][6], formatBiasa)
				
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H"+str(awal)+":I"+str(index)+")", formatBiasa)
		else:	
			index+=1
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa);
		idxPengeluaranLain = 'H'+str(index+1)	
				
		worksheet.merge_range('B'+str(index+3)+':G'+str(index+3),"LABA RUGI KOTOR : ",formatBiasa);
		worksheet.merge_range('H'+str(index+3)+':I'+str(index+3),"="+idxPenjualan+"-"+idxProduksi,formatBiasa);
				
		worksheet.merge_range('B'+str(index+4)+':G'+str(index+4),"LABA RUGI OPERASIONAL : ",formatBiasa);
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4),"="+idxOperasional,formatBiasa);
				
		worksheet.merge_range('B'+str(index+5)+':G'+str(index+5),"LABA RUGI OPERASIONAL : ",formatBiasa);
		worksheet.merge_range('H'+str(index+5)+':I'+str(index+5),"=("+idxPenjualan+"+"+idxPendapatanLain+")-"+idxProduksi+"-"+idxPengeluaranLain,formatBiasa);
				
		workbook.close()
		return
		
	def Laporan_RNeraca(self):
		"""Kontrol untuk RNeraca"""
		self.Laporan_Goto("LAPORAN NERACA")
		#~ self.GarvinDisconnect(self.LaporanUI.tb_Laporan_Neraca_KodePelanggan.clicked)
		#~ self.LaporanUI.tb_Laporan_Neraca_KodePelanggan.clicked.connect(functools.partial(self.Popup_NamaAlamat,self.LaporanUI.tb_Laporan_Neraca_KodePelanggan))
		self.LaporanUI.tb_Laporan_Neraca_Cetak.clicked.connect(functools.partial(self.Laporan_Neraca))
		self.LaporanUI.tb_Laporan_Neraca_Kembali.clicked.connect(self.Laporan_RMenu)
		
	def Laporan_Neraca(self):
		tanggalAwal = str(self.LaporanUI.dte_Laporan_KasHarian_Dari.dateTime().toString("yyyy-MM-dd"))
		tanggalAkhir = str(self.LaporanUI.dte_Laporan_KasHarian_Sampai.dateTime().toString("yyyy-MM-dd"))
		
		workbook = xlsxwriter.Workbook('LaporanNeraca.xlsx')
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

		formatNoTgl = workbook.add_format({'align': 'center',
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

		formatBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatSubBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
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
		worksheet.merge_range('B2:I2', "LAPORAN", formatJudul)

		worksheet.set_column(1,9,8)
		worksheet.set_column(2,9,8)

		worksheet.merge_range('B3:I3', "NERACA STANDAR", formatSubJudul)
		worksheet.merge_range('B4:I4', "PERIODE "+datetime.strptime(tanggalAwal,"%Y-%m-%d").strftime("%d %B %Y")+" - "+datetime.strptime(tanggalAkhir,"%Y-%m-%d").strftime("%d %B %Y"), formatNoTgl)
		
		worksheet.write('B6', "Harta", formatSubBiasa)
		
		#~ //select Harta
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '1100%' AND '1999%' AND month(tanggal) = 2 GROUP BY noAkun,month(tanggal)"
		
		result = self.DatabaseRunQuery(sql)
		
		for x in range(0,len(result)):
			index = x+1+7
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][5]-result[x][6], formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa)
		
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H6:I"+str(index)+")", formatBiasa)
		else:	
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		idxHarta = 'H'+str(index+1)
			
			
		index=index+3	
		awal=index+2
		worksheet.write('B'+str(index), "Kewajiban", formatSubBiasa)
		
		#//select Kewajiban
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '2100%' AND '2999%' AND tanggal BETWEEN '"+tanggalAwal+"' AND '"+tanggalAkhir+"' GROUP BY noAkun,month(tanggal)"
		print sql
		result = self.DatabaseRunQuery(sql)
		
		for x in range(0,len(result)):
			index = x+awal
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][5]-result[x][6], formatBiasa)
				
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H"+str(awal)+":I"+str(index)+")", formatBiasa)
		else:	
			index+=1
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa);
		idxKewajiban = 'H'+str(index+1)
			
			
		index=index+3	
		awal=index+2
		worksheet.write('B'+str(index), "Modal", formatSubBiasa)
		
		#//select Modal
		sql = "SELECT year(tanggal) as tahun,month(tanggal) as bulan,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun BETWEEN '3100%' AND '3999%' AND tanggal BETWEEN '"+tanggalAwal+"' AND '"+tanggalAkhir+"' GROUP BY noAkun,month(tanggal)"
		print sql
		result = self.DatabaseRunQuery(sql)
		
		for x in range(0,len(result)):
			index = x+awal
			worksheet.merge_range('B'+str(index)+':C'+str(index), result[x][3], formatBiasa)
			worksheet.merge_range('D'+str(index)+':G'+str(index), result[x][2], formatBiasa)
			worksheet.merge_range('H'+str(index)+':I'+str(index), result[x][5]-result[x][6], formatBiasa)
				
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H"+str(awal)+":I"+str(index)+")", formatBiasa)
		else:	
			index+=1
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		worksheet.merge_range('B'+str(index+1)+':G'+str(index+1),"TOTAL : ",formatBiasa);
		idxModal = 'H'+str(index+1)
			
		worksheet.merge_range('B'+str(index+3)+':G'+str(index+3),"TOTAL HARTA : ",formatBiasa);
		worksheet.merge_range('H'+str(index+3)+':I'+str(index+3),"="+idxHarta,formatBiasa);
				
		worksheet.merge_range('B'+str(index+4)+':G'+str(index+4),"TOTAL KEWAJIBAN DAN MODAL : ",formatBiasa);
		worksheet.merge_range('H'+str(index+4)+':I'+str(index+4),"="+idxKewajiban+"+"+idxModal,formatBiasa);
							
		workbook.close()
		return
		
	
	def Laporan_RKasHarian(self):
		"""Kontrol untuk RKasHarian"""
		self.Laporan_Goto("LAPORAN KAS HARIAN")
		self.GarvinDisconnect(self.LaporanUI.tb_Laporan_KasHarian_noAkunKas.clicked) #-- fungsi RKasHarian bakalan dipanggil berkali2 pas program jalan, dadi kudu pastikan diskonek sikik
		self.LaporanUI.tb_Laporan_KasHarian_noAkunKas.clicked.connect(functools.partial(self.Popup_Rekening,self.LaporanUI.tb_Laporan_KasHarian_noAkunKas))
		self.LaporanUI.tb_Laporan_KasHarian_Cetak.clicked.connect(functools.partial(self.Laporan_KasHarian))
		self.LaporanUI.tb_Laporan_KasHarian_Kembali.clicked.connect(self.Laporan_RMenu)
		
	def Laporan_KasHarian(self):
		noAkun = str(self.LaporanUI.tb_Laporan_KasHarian_noAkunKas.text())		
		tanggalAwal = str(self.LaporanUI.dte_Laporan_KasHarian_Dari.dateTime().toString("yyyy-MM-dd"))
		tanggalAkhir = str(self.LaporanUI.dte_Laporan_KasHarian_Sampai.dateTime().toString("yyyy-MM-dd"))
		
		workbook = xlsxwriter.Workbook('LaporanKasHarian.xlsx')
		worksheet = workbook.add_worksheet()
		#~ print '--------------------------------',tanggalAwal,tanggalAkhir,'----------------------------------------'
		formatJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'17'})
										   
		formatSubJudul = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'15'})

		formatNoTgl = workbook.add_format({'align': 'center',
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

		formatBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})

		formatSubBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
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
		worksheet.merge_range('B2:J2', "LAPORAN KAS HARIAN", formatJudul)

		worksheet.set_column(1,1,4)
		worksheet.set_column(2,12,8)
		worksheet.set_column(4,4,25)

		worksheet.merge_range('B4:J4', "PERIODE "+datetime.strptime(tanggalAwal,"%Y-%m-%d").strftime("%d %B %Y")+" - "+datetime.strptime(tanggalAkhir,"%Y-%m-%d").strftime("%d %B %Y"), formatNoTgl)
		
		#~ //select akun kas
		sql = "SELECT tanggal,`"+self.dbDatabase+"`.gd_rekening_jurnal.namaAkun,`"+self.dbDatabase+"`.`gd_buku_besar`.noAkun,kodeTransaksi,SUM(debit) as debit,SUM(kredit) as kredit FROM `"+self.dbDatabase+"`.`gd_buku_besar` JOIN `"+self.dbDatabase+"`.gd_rekening_jurnal ON `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE `"+self.dbDatabase+"`.gd_rekening_jurnal.noAkun  WHERE `"+self.dbDatabase+"`.`gd_buku_besar`.noAkun LIKE "+noAkun
		
		result = self.DatabaseRunQuery(sql)
		worksheet.write("B7","No",formatBiasa);
		worksheet.write("C7","Tanggal",formatBiasa);
		worksheet.write("D7","No Referensi",formatBiasa);
		worksheet.write("E7","Keterangan",formatBiasa);
		worksheet.write("F7","No Akun Perk.",formatBiasa);
		worksheet.write("G7","Debit",formatBiasa);
		worksheet.write("H7","Kredit",formatBiasa);
		for x in range(0,len(result)):
			index = x+1+7
			
			if(x==0):
				worksheet.merge_range('B3:J3', result[x][2]+" - "+result[x][1], formatSubJudul)
			
			kode = result[x][3]
			if(kode.find('KM')>=0):
				cat = "SELECT catatan FROM `gd_kas_masuk` WHERE kodeTransaksi LIKE '"+result[x][3]+"'"
				print  cat
				resultCat = self.DatabaseRunQuery(cat)
				worksheet.write('E'+str(index),resultCat[0][0], formatBiasa)
				
			worksheet.write("B"+str(index),str(x+1),formatBiasa);
			worksheet.write("C"+str(index),result[x][0].strftime("%d-%m-%Y"),formatBiasa);
			worksheet.write('D'+str(index),result[x][3], formatBiasa)
			worksheet.write('F'+str(index),result[x][2], formatBiasa)
			worksheet.write('G'+str(index),result[x][4], formatBiasa)
			worksheet.write('H'+str(index),result[x][5], formatBiasa)
		
		if(len(result)>0):
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "=SUM(H6:I"+str(index)+")", formatBiasa)
		else:	
			worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "0", formatBiasa)
		idxHarta = 'H'+str(index+1)
										
		workbook.close()
		return
		
	def Laporan_RHutangPiutang(self):
		"""Kontrol untuk RHutangPiutang"""
		self.Laporan_Goto("LAPORAN HUTANG PIUTANG")
		self.GarvinDisconnect(self.LaporanUI.tb_Laporan_HutangPiutang_KodePelanggan.clicked)
		self.LaporanUI.tb_Laporan_HutangPiutang_KodePelanggan.clicked.connect(functools.partial(self.Popup_NamaAlamat,self.LaporanUI.tb_Laporan_HutangPiutang_KodePelanggan))
		self.LaporanUI.tb_Laporan_HutangPiutang_Cetak.clicked.connect(functools.partial(self.Laporan_HutangPiutang))
		self.LaporanUI.tb_Laporan_HutangPiutang_Kembali.clicked.connect(self.Laporan_RMenu)
		
	def Laporan_HutangPiutang(self):
		
		idNama = str(self.LaporanUI.tb_Laporan_HutangPiutang_KodePelanggan.text())
		ket = str(self.LaporanUI.cb_Laporan_HutangPiutang_Tampilkan.currentIndex())
		tanggalAwal =str(self.LaporanUI.dte_Laporan_HutangPiutang_Dari.dateTime().toString("yyyy-MM-dd"))
		tanggalAkhir =str(self.LaporanUI.dte_Laporan_HutangPiutang_Sampai.dateTime().toString("yyyy-MM-dd"))
		
		workbook = xlsxwriter.Workbook('LaporanHutangPiutang.xlsx')
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
										   
		formatBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})
										   
		formatTblHeader = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'12'})
		
		worksheet.set_column(1,1,3.14)								   		
		worksheet.set_column(2,2,12)
		worksheet.set_column(3,3,11)
		worksheet.set_column(4,4,35)
		worksheet.set_column(5,5,20)
		worksheet.set_column(6,6,20)
		worksheet.set_column(7,7,20)
										   		
		#~ #Select piutang
		if(idNama == '0'):
			sqlPiutang = "SELECT * FROM gd_invoice_penjualan AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan WHERE 1 ORDER BY tanggal, kodeTransaksi ASC "
			resultPiutang = self.DatabaseRunQuery(sqlPiutang)
			namaPelanggan = ""
		else:	
			sqlPiutang = "SELECT * FROM gd_invoice_penjualan AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan WHERE aDB.kodePelanggan LIKE '"+idNama+"' ORDER BY tanggal, kodeTransaksi ASC "
			resultPiutang = self.DatabaseRunQuery(sqlPiutang)
			if(len(resultPiutang)>0):
				namaPelanggan = resultPiutang[0][10]				
				worksheet.merge_range("B3:H3",namaPelanggan,formatJudul)
		
		#~ namaPelanggan = resultPiutang[0][10]
		
		worksheet.merge_range("B2:H2","BUKU PIUTANG HUTANG",formatJudul)
		
		worksheet.merge_range("B5:C5","Piutang Dagang",formatTblHeader);
		worksheet.write("B6","No",formatTblHeader);
		worksheet.write("C6","No Invoice",formatTblHeader);
		worksheet.write("D6","Tanggal",formatTblHeader);
		worksheet.write("E6","Customer",formatTblHeader);
		worksheet.write("F6","Jumlah Invoice",formatTblHeader);
		worksheet.write("G6","Jumlah Penerimaan",formatTblHeader);
		worksheet.write("H6","No Referensi",formatTblHeader);
		
		index1 = 0;
		noUrut=1;
		
		if(len(resultPiutang)>0):
			for x in range(0,len(resultPiutang)):
				kodeTransaksi = resultPiutang[x][1]
				index = index1+8

				sqlX = "SELECT SUM(jumlahPenerimaan) AS jml,jumlahTagihan AS nilai FROM gd_piutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultX = self.DatabaseRunQuery(sqlX)
				jmlPenerimaan = resultX[0][0]
				jmlTagihan = resultPiutang[x][6]
				
				if not(resultX[0][0]>0):
					jmlPenerimaan = 0
									
				sqlRef = "SELECT noReferensi FROM gd_piutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultRef = self.DatabaseRunQuery(sqlRef)
				
				#~ print kodeTransaksi," ",(jmlPenerimaan)," ",(jmlTagihan)," ",(jmlPenerimaan < jmlTagihan)
				if((jmlPenerimaan >= jmlTagihan)) and (ket==__LUNAS__): 
					worksheet.write("B"+str(index),str(noUrut),formatBiasa);
					worksheet.write("D"+str(index),resultPiutang[x][1],formatBiasa);
					worksheet.write("C"+str(index),resultPiutang[x][4].strftime("%d-%m-%Y"),formatBiasa);
					worksheet.write("E"+str(index),resultPiutang[x][10],formatBiasa);
					worksheet.write("F"+str(index),resultPiutang[x][6],formatBiasa);
					worksheet.write("G"+str(index),jmlPenerimaan,formatBiasa);
					noUrut+=1
					
					for xi in range(0,len(resultRef)):
						worksheet.write("H"+str(index),resultRef[xi][0],formatBiasa);
						index+=1
						index1+=1
						
				elif((jmlPenerimaan < jmlTagihan)) and (ket==__BELUM_LUNAS__):
					worksheet.write("B"+str(index),str(noUrut),formatBiasa);
					worksheet.write("D"+str(index),resultPiutang[x][1],formatBiasa);
					worksheet.write("C"+str(index),resultPiutang[x][4].strftime("%d-%m-%Y"),formatBiasa);
					worksheet.write("E"+str(index),resultPiutang[x][10],formatBiasa);
					worksheet.write("F"+str(index),resultPiutang[x][6],formatBiasa);
					worksheet.write("G"+str(index),jmlPenerimaan,formatBiasa);
					noUrut+=1
					
					if(jmlPenerimaan>0):
						for xi in range(0,len(resultRef)):
							worksheet.write("H"+str(index),resultRef[xi][0],formatBiasa);
							index+=1
							index1+=1
					else:
						worksheet.write("G"+str(index),0,formatBiasa);
						index1+=1		
						
				elif (ket==__SEMUA__):	
					print kodeTransaksi," ",(jmlPenerimaan)," ",(jmlTagihan)," ",(jmlPenerimaan < jmlTagihan)
					worksheet.write("B"+str(index),str(noUrut),formatBiasa);
					worksheet.write("D"+str(index),resultPiutang[x][1],formatBiasa);
					worksheet.write("C"+str(index),resultPiutang[x][4].strftime("%d-%m-%Y"),formatBiasa);
					worksheet.write("E"+str(index),resultPiutang[x][10],formatBiasa);
					worksheet.write("F"+str(index),resultPiutang[x][6],formatBiasa);
					worksheet.write("G"+str(index),jmlPenerimaan,formatBiasa);
					noUrut+=1
					
					if(jmlPenerimaan>0):
						for xi in range(0,len(resultRef)):
							worksheet.write("H"+str(index),resultRef[xi][0],formatBiasa);
							index+=1
							index1+=1
					else:
						worksheet.write("G"+str(index),0,formatBiasa);
						index1+=1
		else:
			index = 8		
		
		index = index+2	
										   		
		#~ #Select hutang
		if(idNama == 0):
			sqlHutang = "SELECT * FROM gd_invoice_penjualan AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan WHERE 1 ORDER BY tanggal, kodeTransaksi ASC "
			namaPelanggan = ""
			resultHutang = self.DatabaseRunQuery(sqlHutang)
		else:	
			#~ sqlHutang = "SELECT * FROM gd_invoice_penjualan AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan WHERE aDB.kodePelanggan LIKE '"+idNama+"' ORDER BY tanggal, kodeTransaksi ASC "
			sqlHutang = "SELECT * FROM gd_pembelian_barang AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodeVendor LIKE bDB.kodePelanggan JOIN gd_invoice_penjualan AS cDB ON cDB.kodeTransaksi LIKE aDB.noInvoice WHERE aDB.kodeVendor LIKE '"+idNama+"' ORDER BY tanggal, kodeTransaksi ASC"
			#~ SELECT * FROM gd_pembelian_barang AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodeVendor LIKE bDB.kodePelanggan JOIN gd_invoice_penjualan AS cDB ON cDB.kodeTransaksi LIKE aDB.noInvoice WHERE aDB.kodeVendor LIKE 'VENDOR.000004' ORDER BY tanggal, kodeTransaksi ASC
			resultHutang = self.DatabaseRunQuery(sqlHutang)
			if(len(resultHutang)>0):
				if not(len(resultPiutang)>0):
					namaPelanggan = resultHutang[0][11]
					worksheet.merge_range("B3:H3",namaPelanggan,formatJudul)
		
				
		worksheet.merge_range("B"+str(index)+":C"+str(index),"Hutang Dagang",formatTblHeader);
		index+=1
		worksheet.write("B"+str(index),"No",formatTblHeader);
		worksheet.write("C"+str(index),"No Invoice",formatTblHeader);
		worksheet.write("D"+str(index),"Tanggal",formatTblHeader);
		worksheet.write("E"+str(index),"Customer",formatTblHeader);
		worksheet.write("F"+str(index),"Jumlah Invoice",formatTblHeader);
		worksheet.write("G"+str(index),"Jumlah Penerimaan",formatTblHeader);
		worksheet.write("H"+str(index),"No Referensi",formatTblHeader);
		
		index1 = 0;
		noUrut=1;
		awal = index+1
		
		if(len(resultHutang)>0):
			for x in range(0,len(resultHutang)):
				kodeTransaksi = resultHutang[x][1]
				index = awal+index1+1

				sqlX = "SELECT SUM(jumlahPenerimaan) AS jml,jumlahTagihan AS nilai FROM gd_hutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultX = self.DatabaseRunQuery(sqlX)
				jmlPenerimaan = resultX[0][0]
				jmlTagihan = resultHutang[x][6]
				
				if not(resultX[0][0]>0):
					jmlPenerimaan = 0
									
				sqlRef = "SELECT noReferensi FROM gd_hutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultRef = self.DatabaseRunQuery(sqlRef)
				
				#~# print kodeTransaksi," ",(jmlPenerimaan)," ",(jmlTagihan)," ",(jmlPenerimaan < jmlTagihan)
				if((jmlPenerimaan >= jmlTagihan)) and (ket==__LUNAS__): 
					worksheet.write("B"+str(index),str(noUrut),formatBiasa);
					worksheet.write("C"+str(index),resultHutang[x][1],formatBiasa);
					worksheet.write("D"+str(index),resultHutang[x][27].strftime("%d-%m-%Y"),formatBiasa);
					worksheet.write("E"+str(index),resultHutang[x][11],formatBiasa);
					worksheet.write("F"+str(index),resultHutang[x][8],formatBiasa);
					worksheet.write("G"+str(index),jmlPenerimaan,formatBiasa);
					noUrut+=1
					
					for xi in range(0,len(resultRef)):
						worksheet.write("H"+str(index),resultRef[xi][0],formatBiasa);
						index+=1
						index1+=1
						
				elif((jmlPenerimaan < jmlTagihan)) and (ket==__BELUM_LUNAS__):
					worksheet.write("B"+str(index),str(noUrut),formatBiasa);
					worksheet.write("C"+str(index),resultHutang[x][1],formatBiasa);
					worksheet.write("D"+str(index),resultHutang[x][27].strftime("%d-%m-%Y"),formatBiasa);
					worksheet.write("E"+str(index),resultHutang[x][11],formatBiasa);
					worksheet.write("F"+str(index),resultHutang[x][8],formatBiasa);
					worksheet.write("G"+str(index),jmlPenerimaan,formatBiasa);
					noUrut+=1
					
					if(jmlPenerimaan>0):
						for xi in range(0,len(resultRef)):
							worksheet.write("H"+str(index),resultRef[xi][0],formatBiasa);
							index+=1
							index1+=1
					else:
						worksheet.write("G"+str(index),0,formatBiasa);
						index1+=1		
						
				elif (ket==__SEMUA__):	
					worksheet.write("B"+str(index),str(noUrut),formatBiasa);
					worksheet.write("C"+str(index),resultHutang[x][1],formatBiasa);
					worksheet.write("D"+str(index),resultHutang[x][27].strftime("%d-%m-%Y"),formatBiasa);
					worksheet.write("E"+str(index),resultHutang[x][11],formatBiasa);
					worksheet.write("F"+str(index),resultHutang[x][8],formatBiasa);
					worksheet.write("G"+str(index),jmlPenerimaan,formatBiasa);
					noUrut+=1
					
					if(jmlPenerimaan>0):
						for xi in range(0,len(resultRef)):
							worksheet.write("H"+str(index),resultRef[xi][0],formatBiasa);
							index+=1
							index1+=1
					else:
						worksheet.write("G"+str(index),0,formatBiasa);
						index1+=1
				
		workbook.close()
		return


	def Laporan_RJualBeli(self):
		"""Kontrol untuk RJualBeli"""
		self.Laporan_Goto("LAPORAN JUAL BELI")
		self.GarvinDisconnect(self.LaporanUI.tb_Laporan_JualBeli_KodePelanggan.clicked)
		self.LaporanUI.tb_Laporan_JualBeli_KodePelanggan.clicked.connect(functools.partial(self.Popup_NamaAlamat,self.LaporanUI.tb_Laporan_JualBeli_KodePelanggan))
		self.LaporanUI.tb_Laporan_JualBeli_Cetak.clicked.connect(functools.partial(self.Laporan_JualBeli))
		self.LaporanUI.tb_Laporan_JualBeli_Kembali.clicked.connect(self.Laporan_RMenu)

	def Laporan_JualBeli(self):
		idNama = str(self.LaporanUI.tb_Laporan_JualBeli_KodePelanggan.text())
		ket = self.LaporanUI.cb_Laporan_JualBeli_Tampilkan.currentIndex()
		tanggalAwal =str(self.LaporanUI.dte_Laporan_JualBeli_Dari.dateTime().toString("yyyy-MM-dd"))
		tanggalAkhir =str(self.LaporanUI.dte_Laporan_JualBeli_Sampai.dateTime().toString("yyyy-MM-dd"))
		
		print '--------------------','(',idNama,',',ket,',',tanggalAwal,',',tanggalAkhir,')','--------------------'
		workbook = xlsxwriter.Workbook('LaporanJualBeli.xlsx')
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
										   
		formatBiasa = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'font_size':'12'})
										   
		formatTblHeader = workbook.add_format({'align': 'left',
										   'valign': 'vcenter',
										   'border': 0,
										   'bold':'true',
										   'font_size':'12'})
										   		
		formatJudulTandaTangan = workbook.add_format({'align': 'center',
										   'valign': 'vcenter',
										   'border': 1,
										   'bold':'true',
										   'font_size':'12'})
									   									   
		worksheet.set_column(1,1,3.14)								   		
		worksheet.set_column(2,2,12)
		worksheet.set_column(3,3,12)
		worksheet.set_column(4,4,18)
		worksheet.set_column(5,5,18)
		worksheet.set_column(6,6,18)
		worksheet.set_column(7,7,18)
		worksheet.set_column(8,10,20)
		
		#~ #Select penjualan
		if(idNama == '0'):
			sqlPenjualan = "SELECT * FROM gd_invoice_penjualan AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan JOIN gd_order_penjualan AS cDB ON cDB.kodeTransaksi LIKE aDB.kodeTransaksi WHERE 1 ORDER BY aDB.tanggal, aDB.kodeTransaksi ASC"
			resultPenjualan = self.DatabaseRunQuery(sqlPenjualan)
		else:
			sqlPenjualan = "SELECT * FROM gd_invoice_penjualan AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodePelanggan LIKE bDB.kodePelanggan JOIN gd_order_penjualan AS cDB ON cDB.kodeTransaksi LIKE aDB.kodeTransaksi WHERE aDB.kodePelanggan LIKE '"+idNama+"' ORDER BY aDB.tanggal, aDB.kodeTransaksi ASC"
			resultPenjualan = self.DatabaseRunQuery(sqlPenjualan)
			
			if(len(resultPenjualan)>0):
				namaPelanggan = resultPenjualan[0][10]
				worksheet.merge_range("B3:K3",namaPelanggan,formatJudul)
		
		worksheet.merge_range("B2:K2","BUKU PENJUALAN PEMBELIAN",formatJudul)
		
		worksheet.merge_range("B5:K5","Penjualan",formatTblHeader);
		worksheet.write("B6","No",formatTblHeader);
		worksheet.write("C6","No Invoice",formatTblHeader);
		worksheet.write("D6","Tanggal",formatTblHeader);
		worksheet.merge_range("E6:F6","Customer",formatTblHeader);
		worksheet.merge_range("G6:H6","Produk",formatTblHeader);
		worksheet.write("I6","Jumlah Invoice",formatTblHeader);
		worksheet.write("J6","Jumlah Dibayar",formatTblHeader);
		worksheet.write("K6","Saldo Piutang",formatTblHeader);
		
		index1 = 0;
		noUrut=1;
		index = index1+8
		
		if(len(resultPenjualan)>0):
			for x in range(0,len(resultPenjualan)):
				kodeTransaksi = resultPenjualan[x][1]
				index = index1+8

				sqlX = "SELECT SUM(jumlahPenerimaan) AS jml,jumlahTagihan AS nilai FROM gd_piutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultX = self.DatabaseRunQuery(sqlX)
				jmlPenerimaan = resultX[0][0]
				jmlTagihan = resultPenjualan[x][6]
				
				if not(resultX[0][0]>0):
					jmlPenerimaan = 0
									
				sqlRef = "SELECT noReferensi FROM gd_piutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultRef = self.DatabaseRunQuery(sqlRef)
				
				#~ print kodeTransaksi," ",(jmlPenerimaan)," ",(jmlTagihan)," ",(jmlPenerimaan < jmlTagihan)
				worksheet.write("B"+str(index),str(noUrut),formatBiasa);
				worksheet.write("C"+str(index),resultPenjualan[x][4].strftime("%d-%m-%Y"),formatBiasa);
				worksheet.write("D"+str(index),resultPenjualan[x][1],formatBiasa);
				worksheet.merge_range("E"+str(index)+":F"+str(index),resultPenjualan[x][10],formatBiasa);
				worksheet.merge_range("G"+str(index)+":H"+str(index),resultPenjualan[x][26],formatBiasa);
				worksheet.write("I"+str(index),resultPenjualan[x][6],formatBiasa);
				worksheet.write("J"+str(index),jmlPenerimaan,formatBiasa);
				worksheet.write("K"+str(index),"=I"+str(index)+"-J"+str(index),formatBiasa);
				noUrut+=1
				index1+=1
							
		
		index = index+2
		index1 = index+3	
		
		#~ #Select pembelian
		if(idNama == '0'):
			sqlPembelian = "SELECT * FROM gd_pembelian_barang AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodeVendor LIKE bDB.kodePelanggan JOIN gd_invoice_penjualan AS cDB ON aDB.noInvoice LIKE cDB.kodeTransaksi WHERE 1 ORDER BY cDB.tanggal, cDB.kodeTransaksi ASC"
			resultPembelian = self.DatabaseRunQuery(sqlPembelian)			
		else:
			sqlPembelian = "SELECT * FROM gd_pembelian_barang AS aDB JOIN gd_nama_alamat AS bDB ON aDB.kodeVendor LIKE bDB.kodePelanggan JOIN gd_invoice_penjualan AS cDB ON aDB.noInvoice LIKE cDB.kodeTransaksi WHERE aDB.kodeVendor LIKE '"+idNama+"' ORDER BY cDB.tanggal, cDB.kodeTransaksi ASC"
			resultPembelian = self.DatabaseRunQuery(sqlPembelian)
						
			if not(len(resultPenjualan)>0):
				namaPelanggan = resultPembelian[0][10]
				worksheet.merge_range("B3:K3",resultPembelian[0][10]+" - "+resultPembelian[0][11],formatJudul)
		
		
		worksheet.merge_range("B"+str(index)+":C"+str(index),"Pembelian",formatTblHeader);
		index+=1
		worksheet.write("B"+str(index),"No",formatTblHeader);
		worksheet.write("C"+str(index),"No Invoice",formatTblHeader);
		worksheet.write("D"+str(index),"Tanggal",formatTblHeader);
		worksheet.merge_range("E"+str(index)+":F"+str(index),"Customer",formatTblHeader);
		worksheet.merge_range("G"+str(index)+":H"+str(index),"Produk",formatTblHeader);
		worksheet.write("I"+str(index),"Jumlah Invoice",formatTblHeader);
		worksheet.write("J"+str(index),"Jumlah Dibayar",formatTblHeader);
		worksheet.write("K"+str(index),"Hutang",formatTblHeader);
		
		noUrut=1;
		
		if(len(resultPembelian)>0):
			for x in range(0,len(resultPembelian)):
				kodeTransaksi = resultPembelian[x][1]
				index = index1

				sqlX = "SELECT SUM(jumlahPenerimaan) AS jml,jumlahTagihan AS nilai FROM gd_hutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultX = self.DatabaseRunQuery(sqlX)
				jmlPenerimaan = resultX[0][0]
				jmlTagihan = resultPembelian[x][6]
				
				if not(resultX[0][0]>0):
					jmlPenerimaan = 0
									
				sqlRef = "SELECT noReferensi FROM gd_hutang WHERE noInvoice LIKE '"+kodeTransaksi+"'"
				resultRef = self.DatabaseRunQuery(sqlRef)
				
				#~ print kodeTransaksi," ",(jmlPenerimaan)," ",(jmlTagihan)," ",(jmlPenerimaan < jmlTagihan)
				worksheet.write("B"+str(index),str(noUrut),formatBiasa);
				worksheet.write("D"+str(index),resultPembelian[x][1],formatBiasa);
				worksheet.write("C"+str(index),resultPembelian[x][27].strftime("%d-%m-%Y"),formatBiasa);
				worksheet.merge_range("E"+str(index)+":F"+str(index),resultPembelian[x][11],formatBiasa);
				worksheet.merge_range("G"+str(index)+":H"+str(index),resultPembelian[x][3]+" (@"+str(resultPembelian[x][5])+"x"+str(resultPembelian[x][6])+" "+(resultPembelian[x][7])+")",formatBiasa);
				worksheet.write("I"+str(index),resultPembelian[x][8],formatBiasa);
				worksheet.write("J"+str(index),jmlPenerimaan,formatBiasa);
				worksheet.write("K"+str(index),"=I"+str(index)+"-J"+str(index),formatBiasa);
				noUrut+=1
				index1+=1
		
		index+=3	
		worksheet.merge_range('B'+str(index+1)+':C'+str(index+1), "Pembukuan", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+1)+':E'+str(index+1), "Keuangan", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+1)+':G'+str(index+1), "Diketahui", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+1)+':I'+str(index+1), "Disetujui", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+1)+':K'+str(index+1), "Penerima", formatJudulTandaTangan)
				
		worksheet.merge_range('B'+str(index+2)+':C'+str(index+6), "", formatJudulTandaTangan)
		worksheet.merge_range('D'+str(index+2)+':E'+str(index+6), "", formatJudulTandaTangan)
		worksheet.merge_range('F'+str(index+2)+':G'+str(index+6), "", formatJudulTandaTangan)
		worksheet.merge_range('H'+str(index+2)+':I'+str(index+6), "", formatJudulTandaTangan)
		worksheet.merge_range('J'+str(index+2)+':K'+str(index+6), "", formatJudulTandaTangan)
		
		workbook.close()
		return

	#~ def Laporan_HutangPiutang(self,idNama,noAkun,tanggalAwal,tanggalAkhir):
		#~ 
		#~ workbook = xlsxwriter.Workbook('LaporanHutangPiutang.xlsx')
		#~ worksheet = workbook.add_worksheet()
		#~ 
		#~ formatJudul = workbook.add_format({'align': 'center',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 0,
										   #~ 'bold':'true',
										   #~ 'font_size':'17'})
										   #~ 
		#~ formatSubJudul = workbook.add_format({'align': 'center',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 0,
										   #~ 'font_size':'15'})
										   #~ 
		#~ formatBiasa = workbook.add_format({'align': 'left',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 0,
										   #~ 'font_size':'12'})
										   #~ 
		#~ formatTblHeader = workbook.add_format({'align': 'left',
										   #~ 'valign': 'vcenter',
										   #~ 'border': 0,
										   #~ 'bold':'true',
										   #~ 'font_size':'12'})
										   #~ 
		#//select noAkun hutang dan piutang
		#~ sql = "SELECT noAkunHutang,noAkunPiutang,namaPelanggan FROM `"+self.dbDatabase+"`.`gd_nama_alamat`WHERE kodePelanggan LIKE '"+idNama+"'"
		#~ result = self.DatabaseRunQuery(sql)
		#~ 
		#~ noAkunHutang = result[0][0]
		#~ noAkunPiutang = result[0][1]
		#~ namaPelanggan = result[0][2]
		#~ 
		#Select hutang		
		#~ sqlHutang = "SELECT * FROM `"+self.dbDatabase+"`.`gd_buku_besar` WHERE noAkun LIKE '"+noAkunHutang+"' ORDER BY tanggal,kodeTransaksi ASC"
		#~ resultHutang = self.DatabaseRunQuery(sqlHutang)
		#~ 
		#Select piutang
		#~ sqlPiutang = "SELECT * FROM `"+self.dbDatabase+"`.`gd_buku_besar` WHERE noAkun LIKE '"+noAkunPiutang+"' ORDER BY tanggal,kodeTransaksi ASC"
		#~ resultPiutang = self.DatabaseRunQuery(sqlPiutang)
		#~ 
		#~ worksheet.merge_range("B2:H2","BUKU PIUTANG HUTANG",formatJudul)
		#~ worksheet.merge_range("B3:H3",namaPelanggan,formatJudul)
		#~ 
		#~ worksheet.merge_range("B5:C5","Piutang Dagang",formatTblHeader);
		#~ worksheet.write("B6","No",formatTblHeader);
		#~ worksheet.write("C6","Tanggal",formatTblHeader);
		#~ worksheet.write("D6","No Referensi",formatTblHeader);
		#~ worksheet.write("E6","Deskripsi",formatTblHeader);
		#~ worksheet.write("F6","Debit",formatTblHeader);
		#~ worksheet.write("G6","Kredit",formatTblHeader);
		#~ worksheet.write("H6","Saldo Debit",formatTblHeader);
		#~ 
		#~ if(len(resultPiutang)>0):
			#~ for x in range(0,len(resultPiutang)):
				#~ index = x+8
				#~ kodeTransaksi = resultPiutang[x][1]
				#~ namaTabel = tabel_kode(kodeTransaksi)
				#~ 
				#Select deskripsi berdasar kodeTransaksi
				#~ sqlDesc = "SELECT catatan FROM `"+self.dbDatabase+"`.`"+namaTabel+"` WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
				#~ resultDesc = self.DatabaseRunQuery(sqlDesc)
				#~ 
				#print resultPiutang[x][2]," | ",resultPiutang[x][1]," | ",resultDesc[0][0]," | ",resultPiutang[x][4]," | ",resultPiutang[x][5]
				#~ 
				#~ worksheet.write("B"+str(index),str(x+1),formatBiasa);
				#~ worksheet.write("C"+str(index),resultPiutang[x][2].strftime("%d-%m-%Y"),formatBiasa);
				#~ worksheet.write("D"+str(index),resultPiutang[x][1],formatBiasa);
				#~ worksheet.write("E"+str(index),resultDesc[0][0],formatBiasa);
				#~ worksheet.write("F"+str(index),str(resultPiutang[x][4]),formatBiasa);
				#~ worksheet.write("G"+str(index),str(resultPiutang[x][5]),formatBiasa);
				#~ worksheet.write("H"+str(index),"=H"+str(index-1)+"+F"+str(index)+"-G"+str(index),formatBiasa);
		#~ 
		#~ index = index+2	
		#~ awal = index+1
		#~ 
		#~ worksheet.merge_range("B"+str(index)+":C"+str(index),"Hutang Dagang",formatTblHeader);
		#~ index+=1
		#~ worksheet.write("B"+str(index),"No",formatTblHeader);
		#~ worksheet.write("C"+str(index),"Tanggal",formatTblHeader);
		#~ worksheet.write("D"+str(index),"No Referensi",formatTblHeader);
		#~ worksheet.write("E"+str(index),"Deskripsi",formatTblHeader);
		#~ worksheet.write("F"+str(index),"Debit",formatTblHeader);
		#~ worksheet.write("G"+str(index),"Kredit",formatTblHeader);
		#~ worksheet.write("H"+str(index),"Saldo Debit",formatTblHeader);
		#~ 
		#~ if(len(resultHutang)>0):
			#~ for x in range(0,len(resultHutang)):
				#~ index = x+awal
				#~ kodeTransaksi = resultHutang[x][1]
				#~ namaTabel = tabel_kode(kodeTransaksi)
				#~ 
				#Select deskripsi berdasar kodeTransaksi
				#~ sqlDesc = "SELECT catatan FROM `"+self.dbDatabase+"`.`"+namaTabel+"` WHERE kodeTransaksi LIKE '"+kodeTransaksi+"'"
				#~ resultDesc = self.DatabaseRunQuery(sqlDesc)
				#~ 
				#~ print "no - ",index
				#print resultHutang[x][2]," | ",resultHutang[x][1]," | ",resultDesc[0][0]," | ",resultHutang[x][4]," | ",resultHutang[x][5]
				#~ 
				#~ worksheet.write("B"+str(index),str(x+1),formatBiasa);
				#~ worksheet.write("C"+str(index),resultHutang[x][2].strftime("%d-%m-%Y"),formatBiasa);
				#~ worksheet.write("D"+str(index),resultHutang[x][1],formatBiasa);
				#~ worksheet.write("E"+str(index),resultDesc[0][0],formatBiasa);
				#~ worksheet.write("F"+str(index),str(resultHutang[x][4]),formatBiasa);
				#~ worksheet.write("G"+str(index),str(resultHutang[x][5]),formatBiasa);
				#~ worksheet.write("H"+str(index),"=H"+str(index-1)+"+F"+str(index)+"-G"+str(index),formatBiasa);
			#~ 
		#~ workbook.close()
		#~ return
#~ 

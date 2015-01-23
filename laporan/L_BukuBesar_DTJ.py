import MySQLdb
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

from html import HTML

class L_BukuBesar_DTJ(object):
	def __init__(self, parent=None):
		pass
		
		
	def L_BukuBesar_DTJ_init(self):
		pass
	
	def L_BukuBesar_DTJ_Create(self,nama,data):
		fjurnal = self.BukuBesar_TransaksiJurnal_Field.index
		fdetail = self.BukuBesar_DetailTransaksiJurnal_Field.index
		h = HTML()
		h.text("<!doctype html>",escape=False)
		h_ = h.html()
		h_html = h_.body(style="font-family:Arial; font-size:10pt;")
		h_html_Judul = h_html.p("General Journal List")
		h_html_table = h_html.table(style="border:solid 1px gray;")
		tr_judul = h_html_table.tr(style="font-weight:bold;")
		tr_judul.td("Tanggal")
		tr_judul.td("Keterangan")
		tr_judul.td("Departemen")
		tr_judul.td("Debet")
		tr_judul.td("Kredit")
		#~ tr_judul.td("Proyek")
		for x_transaksi in range(0,len(data[1])):
			transaksi = data[0][x_transaksi]
			detail = data[1][x_transaksi]
			
			tr = h_html_table.tr(style="font-weight:bold;font-size:0.8em;")
			tr.td(str(re.findall("(.+)\s",str(detail[0][fdetail("tanggal")])	))[2:-2])
			tr.td("")
			tr.td("")
			tr.td("")
			tr.td("")
			for baris_detail in range(0,len(detail)):
				tr_detail = h_html_table.tr
				data_detail = detail[baris_detail]
				tr_detail.td(" "+str(data_detail[fdetail("kodeTransaksi")]),escape=False)
				
				nomorakun = str(data_detail[fdetail("noAkunJurnal")])
				try:namaakun = str(self.DatabaseFetchResult(self.dbDatabase,"gd_rekening_jurnal","noAkun",nomorakun)[0][self.DataMaster_DataRekening_Field.index("namaAkun")])
				except:namaakun = ""
				tr_detail.td(nomorakun+" "+namaakun,escape=False)
				
				kodedepartemen = str(data_detail[fdetail("kodeDepartemen")])
				try:namadepartemen = self.DatabaseFetchResult(self.dbDatabase,"gd_data_departemen","kodeDepartemen",kodedepartemen)[0][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")]
				except:namadepartemen = kodedepartemen
				tr_detail.td(namadepartemen,escape=False)
				tr_detail.td(str(data_detail[fdetail("debit")]),escape=False)
				tr_detail.td(str(data_detail[fdetail("kredit")]),escape=False)
				
				#~ for kolom_detail in range(1,len(detail[baris_detail])): #-- mulai dari 1 (skip field id)
					#~ print detail[baris_detail][kolom_detail]
					#~ td = h_html_table_tr.td(str(detail[baris_detail][kolom_detail]))
		print (str(h))
		f = open("./Laporan.html","w")
		f.write(str(h))
		f.close()

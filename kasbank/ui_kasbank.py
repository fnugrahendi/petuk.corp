# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kasbank/ui_kasbank.ui'
#
# Created: Wed Jan 21 22:05:22 2015
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_st_KasBank(object):
    def setupUi(self, st_KasBank):
        st_KasBank.setObjectName(_fromUtf8("st_KasBank"))
        st_KasBank.resize(777, 584)
        st_KasBank.setStyleSheet(_fromUtf8("QFrame{border:0px;}"))
        self.st_Menu = QtGui.QWidget()
        self.st_Menu.setObjectName(_fromUtf8("st_Menu"))
        self.igr_KasBank_Menu = QtGui.QGridLayout(self.st_Menu)
        self.igr_KasBank_Menu.setObjectName(_fromUtf8("igr_KasBank_Menu"))
        self.fr_Menu_Content = QtGui.QFrame(self.st_Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Menu_Content.sizePolicy().hasHeightForWidth())
        self.fr_Menu_Content.setSizePolicy(sizePolicy)
        self.fr_Menu_Content.setMinimumSize(QtCore.QSize(640, 480))
        self.fr_Menu_Content.setMaximumSize(QtCore.QSize(640, 480))
        self.fr_Menu_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Menu_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Menu_Content.setObjectName(_fromUtf8("fr_Menu_Content"))
        self.tb_Menu_KasMasuk = QtGui.QPushButton(self.fr_Menu_Content)
        self.tb_Menu_KasMasuk.setGeometry(QtCore.QRect(150, 160, 151, 161))
        self.tb_Menu_KasMasuk.setObjectName(_fromUtf8("tb_Menu_KasMasuk"))
        self.tb_Menu_KasKeluar = QtGui.QPushButton(self.fr_Menu_Content)
        self.tb_Menu_KasKeluar.setGeometry(QtCore.QRect(330, 160, 151, 161))
        self.tb_Menu_KasKeluar.setObjectName(_fromUtf8("tb_Menu_KasKeluar"))
        self.igr_KasBank_Menu.addWidget(self.fr_Menu_Content, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_KasBank_Menu.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_KasBank_Menu.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_KasBank_Menu.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_KasBank_Menu.addItem(spacerItem3, 1, 2, 1, 1)
        st_KasBank.addWidget(self.st_Menu)
        self.st_KasMasuk = QtGui.QWidget()
        self.st_KasMasuk.setObjectName(_fromUtf8("st_KasMasuk"))
        self.ivl_KasMasuk = QtGui.QVBoxLayout(self.st_KasMasuk)
        self.ivl_KasMasuk.setObjectName(_fromUtf8("ivl_KasMasuk"))
        self.fr_KasMasuk_t = QtGui.QFrame(self.st_KasMasuk)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_t.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_t.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_t.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasMasuk_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasMasuk_t.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_t.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_t.setObjectName(_fromUtf8("fr_KasMasuk_t"))
        self.ihl_KasMasuk_t = QtGui.QHBoxLayout(self.fr_KasMasuk_t)
        self.ihl_KasMasuk_t.setObjectName(_fromUtf8("ihl_KasMasuk_t"))
        self.lb_KasMasuk_Judul = QtGui.QLabel(self.fr_KasMasuk_t)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lb_KasMasuk_Judul.sizePolicy().hasHeightForWidth())
        self.lb_KasMasuk_Judul.setSizePolicy(sizePolicy)
        self.lb_KasMasuk_Judul.setMinimumSize(QtCore.QSize(300, 0))
        self.lb_KasMasuk_Judul.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_KasMasuk_Judul.setFont(font)
        self.lb_KasMasuk_Judul.setObjectName(_fromUtf8("lb_KasMasuk_Judul"))
        self.ihl_KasMasuk_t.addWidget(self.lb_KasMasuk_Judul)
        spacerItem4 = QtGui.QSpacerItem(226, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ihl_KasMasuk_t.addItem(spacerItem4)
        self.le_KasMasuk_Search = QtGui.QLineEdit(self.fr_KasMasuk_t)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.le_KasMasuk_Search.sizePolicy().hasHeightForWidth())
        self.le_KasMasuk_Search.setSizePolicy(sizePolicy)
        self.le_KasMasuk_Search.setMinimumSize(QtCore.QSize(200, 0))
        self.le_KasMasuk_Search.setMaximumSize(QtCore.QSize(200, 16777215))
        self.le_KasMasuk_Search.setObjectName(_fromUtf8("le_KasMasuk_Search"))
        self.ihl_KasMasuk_t.addWidget(self.le_KasMasuk_Search)
        self.ivl_KasMasuk.addWidget(self.fr_KasMasuk_t)
        self.fr_KasMasuk_Content = QtGui.QFrame(self.st_KasMasuk)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_Content.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_Content.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_Content.setObjectName(_fromUtf8("fr_KasMasuk_Content"))
        self.ivl_KasMasuk_Content = QtGui.QVBoxLayout(self.fr_KasMasuk_Content)
        self.ivl_KasMasuk_Content.setObjectName(_fromUtf8("ivl_KasMasuk_Content"))
        self.tbl_KasMasuk = QtGui.QTableWidget(self.fr_KasMasuk_Content)
        self.tbl_KasMasuk.setObjectName(_fromUtf8("tbl_KasMasuk"))
        self.tbl_KasMasuk.setColumnCount(5)
        self.tbl_KasMasuk.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasMasuk.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasMasuk.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasMasuk.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasMasuk.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasMasuk.setHorizontalHeaderItem(4, item)
        self.ivl_KasMasuk_Content.addWidget(self.tbl_KasMasuk)
        self.ivl_KasMasuk.addWidget(self.fr_KasMasuk_Content)
        self.fr_KasMasuk_b = QtGui.QFrame(self.st_KasMasuk)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_b.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_b.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_b.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasMasuk_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasMasuk_b.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_b.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_b.setObjectName(_fromUtf8("fr_KasMasuk_b"))
        self.ihl_KasMasuk_b = QtGui.QHBoxLayout(self.fr_KasMasuk_b)
        self.ihl_KasMasuk_b.setObjectName(_fromUtf8("ihl_KasMasuk_b"))
        self.tb_KasMasuk_Buka = QtGui.QPushButton(self.fr_KasMasuk_b)
        self.tb_KasMasuk_Buka.setObjectName(_fromUtf8("tb_KasMasuk_Buka"))
        self.ihl_KasMasuk_b.addWidget(self.tb_KasMasuk_Buka)
        self.tb_KasMasuk_Delete = QtGui.QPushButton(self.fr_KasMasuk_b)
        self.tb_KasMasuk_Delete.setObjectName(_fromUtf8("tb_KasMasuk_Delete"))
        self.ihl_KasMasuk_b.addWidget(self.tb_KasMasuk_Delete)
        spacerItem5 = QtGui.QSpacerItem(495, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ihl_KasMasuk_b.addItem(spacerItem5)
        self.tb_KasMasuk_Tutup = QtGui.QPushButton(self.fr_KasMasuk_b)
        self.tb_KasMasuk_Tutup.setObjectName(_fromUtf8("tb_KasMasuk_Tutup"))
        self.ihl_KasMasuk_b.addWidget(self.tb_KasMasuk_Tutup)
        self.ivl_KasMasuk.addWidget(self.fr_KasMasuk_b)
        st_KasBank.addWidget(self.st_KasMasuk)
        self.st_KasMasuk_Tambah = QtGui.QWidget()
        self.st_KasMasuk_Tambah.setObjectName(_fromUtf8("st_KasMasuk_Tambah"))
        self.ivl_KasMasuk_Tambah = QtGui.QVBoxLayout(self.st_KasMasuk_Tambah)
        self.ivl_KasMasuk_Tambah.setObjectName(_fromUtf8("ivl_KasMasuk_Tambah"))
        self.fr_KasMasuk_Tambah_T = QtGui.QFrame(self.st_KasMasuk_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_Tambah_T.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_Tambah_T.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_Tambah_T.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasMasuk_Tambah_T.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasMasuk_Tambah_T.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_Tambah_T.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_Tambah_T.setObjectName(_fromUtf8("fr_KasMasuk_Tambah_T"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fr_KasMasuk_Tambah_T)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lb_KasMasuk_Judul_2 = QtGui.QLabel(self.fr_KasMasuk_Tambah_T)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lb_KasMasuk_Judul_2.sizePolicy().hasHeightForWidth())
        self.lb_KasMasuk_Judul_2.setSizePolicy(sizePolicy)
        self.lb_KasMasuk_Judul_2.setMinimumSize(QtCore.QSize(300, 0))
        self.lb_KasMasuk_Judul_2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_KasMasuk_Judul_2.setFont(font)
        self.lb_KasMasuk_Judul_2.setObjectName(_fromUtf8("lb_KasMasuk_Judul_2"))
        self.horizontalLayout.addWidget(self.lb_KasMasuk_Judul_2)
        spacerItem6 = QtGui.QSpacerItem(432, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.ivl_KasMasuk_Tambah.addWidget(self.fr_KasMasuk_Tambah_T)
        self.fr_KasMasuk_Tambah_Form = QtGui.QFrame(self.st_KasMasuk_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_Tambah_Form.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_Tambah_Form.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_Tambah_Form.setMaximumSize(QtCore.QSize(16777215, 100))
        self.fr_KasMasuk_Tambah_Form.setStyleSheet(_fromUtf8("QLineEdit,QPushButton{border-style:inset;border-width:1px;border-radius:2px;border-color:rgb(156, 156, 156);background-color:#ffffff;min-height:23px;}"))
        self.fr_KasMasuk_Tambah_Form.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_Tambah_Form.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_Tambah_Form.setObjectName(_fromUtf8("fr_KasMasuk_Tambah_Form"))
        self.gridLayout = QtGui.QGridLayout(self.fr_KasMasuk_Tambah_Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lb_KasMasuk_Tambah_Form_Tanggal = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_Tanggal.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_Tanggal"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_Tanggal, 3, 0, 1, 1)
        self.tb_KasMasuk_Tambah_Form_Penyetor = QtGui.QPushButton(self.fr_KasMasuk_Tambah_Form)
        self.tb_KasMasuk_Tambah_Form_Penyetor.setMinimumSize(QtCore.QSize(150, 25))
        self.tb_KasMasuk_Tambah_Form_Penyetor.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tb_KasMasuk_Tambah_Form_Penyetor.setObjectName(_fromUtf8("tb_KasMasuk_Tambah_Form_Penyetor"))
        self.gridLayout.addWidget(self.tb_KasMasuk_Tambah_Form_Penyetor, 2, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 6, 1, 1)
        self.dte_KasMasuk_Tambah_Form_Tanggal = QtGui.QDateEdit(self.fr_KasMasuk_Tambah_Form)
        self.dte_KasMasuk_Tambah_Form_Tanggal.setMinimumSize(QtCore.QSize(150, 0))
        self.dte_KasMasuk_Tambah_Form_Tanggal.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dte_KasMasuk_Tambah_Form_Tanggal.setDate(QtCore.QDate(2015, 1, 1))
        self.dte_KasMasuk_Tambah_Form_Tanggal.setCalendarPopup(True)
        self.dte_KasMasuk_Tambah_Form_Tanggal.setObjectName(_fromUtf8("dte_KasMasuk_Tambah_Form_Tanggal"))
        self.gridLayout.addWidget(self.dte_KasMasuk_Tambah_Form_Tanggal, 3, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 6, 1, 1)
        self.tb_KasMasuk_Tambah_Form_NoAkun = QtGui.QPushButton(self.fr_KasMasuk_Tambah_Form)
        self.tb_KasMasuk_Tambah_Form_NoAkun.setMinimumSize(QtCore.QSize(150, 25))
        self.tb_KasMasuk_Tambah_Form_NoAkun.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tb_KasMasuk_Tambah_Form_NoAkun.setObjectName(_fromUtf8("tb_KasMasuk_Tambah_Form_NoAkun"))
        self.gridLayout.addWidget(self.tb_KasMasuk_Tambah_Form_NoAkun, 1, 2, 1, 1)
        self.le_KasMasuk_Tambah_Form_Catatan = QtGui.QLineEdit(self.fr_KasMasuk_Tambah_Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_KasMasuk_Tambah_Form_Catatan.sizePolicy().hasHeightForWidth())
        self.le_KasMasuk_Tambah_Form_Catatan.setSizePolicy(sizePolicy)
        self.le_KasMasuk_Tambah_Form_Catatan.setMaximumSize(QtCore.QSize(500, 16777215))
        self.le_KasMasuk_Tambah_Form_Catatan.setObjectName(_fromUtf8("le_KasMasuk_Tambah_Form_Catatan"))
        self.gridLayout.addWidget(self.le_KasMasuk_Tambah_Form_Catatan, 3, 5, 1, 2)
        self.lb_KasMasuk_Tambah_Form_NoAkun = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_NoAkun.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_NoAkun"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_NoAkun, 1, 0, 1, 1)
        self.lb_KasMasuk_Tambah_Form_Penyetor = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_Penyetor.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_Penyetor"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_Penyetor, 2, 0, 1, 1)
        self.lb_KasMasuk_Tambah_Form_Nilai = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_Nilai.setMinimumSize(QtCore.QSize(150, 0))
        self.lb_KasMasuk_Tambah_Form_Nilai.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lb_KasMasuk_Tambah_Form_Nilai.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_Nilai"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_Nilai, 2, 5, 1, 1)
        self.lb_KasMasuk_Tambah_Form_LabelNilai = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_LabelNilai.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_LabelNilai"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_LabelNilai, 2, 4, 1, 1)
        self.lb_KasMasuk_Tambah_Form_Catatan = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_Catatan.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_Catatan"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_Catatan, 3, 4, 1, 1)
        self.le_KasMasuk_Tambah_Form_Nomor = QtGui.QLineEdit(self.fr_KasMasuk_Tambah_Form)
        self.le_KasMasuk_Tambah_Form_Nomor.setMinimumSize(QtCore.QSize(150, 25))
        self.le_KasMasuk_Tambah_Form_Nomor.setMaximumSize(QtCore.QSize(150, 16777215))
        self.le_KasMasuk_Tambah_Form_Nomor.setObjectName(_fromUtf8("le_KasMasuk_Tambah_Form_Nomor"))
        self.gridLayout.addWidget(self.le_KasMasuk_Tambah_Form_Nomor, 1, 5, 1, 1)
        self.lb_KasMasuk_Tambah_Form_Nomor = QtGui.QLabel(self.fr_KasMasuk_Tambah_Form)
        self.lb_KasMasuk_Tambah_Form_Nomor.setObjectName(_fromUtf8("lb_KasMasuk_Tambah_Form_Nomor"))
        self.gridLayout.addWidget(self.lb_KasMasuk_Tambah_Form_Nomor, 1, 4, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 3, 1, 1)
        self.ivl_KasMasuk_Tambah.addWidget(self.fr_KasMasuk_Tambah_Form)
        self.fr_KasMasuk_Tambah_Content = QtGui.QFrame(self.st_KasMasuk_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_Tambah_Content.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_Tambah_Content.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_Tambah_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_Tambah_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_Tambah_Content.setObjectName(_fromUtf8("fr_KasMasuk_Tambah_Content"))
        self.ivl_KasMasuk_Tambah.addWidget(self.fr_KasMasuk_Tambah_Content)
        self.fr_KasMasuk_Tambah_B = QtGui.QFrame(self.st_KasMasuk_Tambah)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasMasuk_Tambah_B.sizePolicy().hasHeightForWidth())
        self.fr_KasMasuk_Tambah_B.setSizePolicy(sizePolicy)
        self.fr_KasMasuk_Tambah_B.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasMasuk_Tambah_B.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasMasuk_Tambah_B.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasMasuk_Tambah_B.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasMasuk_Tambah_B.setObjectName(_fromUtf8("fr_KasMasuk_Tambah_B"))
        self.ivl_KasMasuk_Tambah.addWidget(self.fr_KasMasuk_Tambah_B)
        st_KasBank.addWidget(self.st_KasMasuk_Tambah)
        self.st_KasKeluar = QtGui.QWidget()
        self.st_KasKeluar.setObjectName(_fromUtf8("st_KasKeluar"))
        self.ivl_KasKeluar = QtGui.QVBoxLayout(self.st_KasKeluar)
        self.ivl_KasKeluar.setObjectName(_fromUtf8("ivl_KasKeluar"))
        self.fr_KasKeluar_t = QtGui.QFrame(self.st_KasKeluar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasKeluar_t.sizePolicy().hasHeightForWidth())
        self.fr_KasKeluar_t.setSizePolicy(sizePolicy)
        self.fr_KasKeluar_t.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasKeluar_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasKeluar_t.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasKeluar_t.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasKeluar_t.setObjectName(_fromUtf8("fr_KasKeluar_t"))
        self.ihl_KasKeluar_t = QtGui.QHBoxLayout(self.fr_KasKeluar_t)
        self.ihl_KasKeluar_t.setObjectName(_fromUtf8("ihl_KasKeluar_t"))
        self.lb_KasKeluar_Judul = QtGui.QLabel(self.fr_KasKeluar_t)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lb_KasKeluar_Judul.sizePolicy().hasHeightForWidth())
        self.lb_KasKeluar_Judul.setSizePolicy(sizePolicy)
        self.lb_KasKeluar_Judul.setMinimumSize(QtCore.QSize(300, 0))
        self.lb_KasKeluar_Judul.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_KasKeluar_Judul.setFont(font)
        self.lb_KasKeluar_Judul.setObjectName(_fromUtf8("lb_KasKeluar_Judul"))
        self.ihl_KasKeluar_t.addWidget(self.lb_KasKeluar_Judul)
        spacerItem10 = QtGui.QSpacerItem(226, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ihl_KasKeluar_t.addItem(spacerItem10)
        self.le_KasKeluar_Search = QtGui.QLineEdit(self.fr_KasKeluar_t)
        self.le_KasKeluar_Search.setObjectName(_fromUtf8("le_KasKeluar_Search"))
        self.ihl_KasKeluar_t.addWidget(self.le_KasKeluar_Search)
        self.ivl_KasKeluar.addWidget(self.fr_KasKeluar_t)
        self.fr_KasKeluar_Content = QtGui.QFrame(self.st_KasKeluar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasKeluar_Content.sizePolicy().hasHeightForWidth())
        self.fr_KasKeluar_Content.setSizePolicy(sizePolicy)
        self.fr_KasKeluar_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasKeluar_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasKeluar_Content.setObjectName(_fromUtf8("fr_KasKeluar_Content"))
        self.ivl_KasKeluar_Content = QtGui.QVBoxLayout(self.fr_KasKeluar_Content)
        self.ivl_KasKeluar_Content.setObjectName(_fromUtf8("ivl_KasKeluar_Content"))
        self.tbl_KasKeluar = QtGui.QTableWidget(self.fr_KasKeluar_Content)
        self.tbl_KasKeluar.setObjectName(_fromUtf8("tbl_KasKeluar"))
        self.tbl_KasKeluar.setColumnCount(5)
        self.tbl_KasKeluar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasKeluar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasKeluar.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasKeluar.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasKeluar.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_KasKeluar.setHorizontalHeaderItem(4, item)
        self.ivl_KasKeluar_Content.addWidget(self.tbl_KasKeluar)
        self.ivl_KasKeluar.addWidget(self.fr_KasKeluar_Content)
        self.fr_KasKeluar_b = QtGui.QFrame(self.st_KasKeluar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasKeluar_b.sizePolicy().hasHeightForWidth())
        self.fr_KasKeluar_b.setSizePolicy(sizePolicy)
        self.fr_KasKeluar_b.setMinimumSize(QtCore.QSize(0, 50))
        self.fr_KasKeluar_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fr_KasKeluar_b.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasKeluar_b.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasKeluar_b.setObjectName(_fromUtf8("fr_KasKeluar_b"))
        self.ihl_KasKeluar_b = QtGui.QHBoxLayout(self.fr_KasKeluar_b)
        self.ihl_KasKeluar_b.setObjectName(_fromUtf8("ihl_KasKeluar_b"))
        self.tb_KasKeluar_Buka = QtGui.QPushButton(self.fr_KasKeluar_b)
        self.tb_KasKeluar_Buka.setObjectName(_fromUtf8("tb_KasKeluar_Buka"))
        self.ihl_KasKeluar_b.addWidget(self.tb_KasKeluar_Buka)
        self.tb_KasKeluar_Delete = QtGui.QPushButton(self.fr_KasKeluar_b)
        self.tb_KasKeluar_Delete.setObjectName(_fromUtf8("tb_KasKeluar_Delete"))
        self.ihl_KasKeluar_b.addWidget(self.tb_KasKeluar_Delete)
        spacerItem11 = QtGui.QSpacerItem(495, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ihl_KasKeluar_b.addItem(spacerItem11)
        self.tb_KasKeluar_Tutup = QtGui.QPushButton(self.fr_KasKeluar_b)
        self.tb_KasKeluar_Tutup.setObjectName(_fromUtf8("tb_KasKeluar_Tutup"))
        self.ihl_KasKeluar_b.addWidget(self.tb_KasKeluar_Tutup)
        self.ivl_KasKeluar.addWidget(self.fr_KasKeluar_b)
        st_KasBank.addWidget(self.st_KasKeluar)

        self.retranslateUi(st_KasBank)
        st_KasBank.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(st_KasBank)

    def retranslateUi(self, st_KasBank):
        st_KasBank.setWindowTitle(_translate("st_KasBank", "StackedWidget", None))
        self.tb_Menu_KasMasuk.setText(_translate("st_KasBank", "Kas Masuk", None))
        self.tb_Menu_KasKeluar.setText(_translate("st_KasBank", "Kas Keluar", None))
        self.lb_KasMasuk_Judul.setText(_translate("st_KasBank", "Kas Masuk", None))
        self.le_KasMasuk_Search.setPlaceholderText(_translate("st_KasBank", "Type to search...", None))
        item = self.tbl_KasMasuk.horizontalHeaderItem(0)
        item.setText(_translate("st_KasBank", "Tanggal", None))
        item = self.tbl_KasMasuk.horizontalHeaderItem(1)
        item.setText(_translate("st_KasBank", "Nomor Referensi", None))
        item = self.tbl_KasMasuk.horizontalHeaderItem(2)
        item.setText(_translate("st_KasBank", "Penerima", None))
        item = self.tbl_KasMasuk.horizontalHeaderItem(3)
        item.setText(_translate("st_KasBank", "Keterangan", None))
        item = self.tbl_KasMasuk.horizontalHeaderItem(4)
        item.setText(_translate("st_KasBank", "Nilai", None))
        self.tb_KasMasuk_Buka.setText(_translate("st_KasBank", "Buka", None))
        self.tb_KasMasuk_Delete.setText(_translate("st_KasBank", "Hapus", None))
        self.tb_KasMasuk_Tutup.setText(_translate("st_KasBank", "Tutup", None))
        self.lb_KasMasuk_Judul_2.setText(_translate("st_KasBank", "+Kas Masuk", None))
        self.lb_KasMasuk_Tambah_Form_Tanggal.setText(_translate("st_KasBank", "Tanggal :", None))
        self.tb_KasMasuk_Tambah_Form_Penyetor.setText(_translate("st_KasBank", "-", None))
        self.tb_KasMasuk_Tambah_Form_NoAkun.setText(_translate("st_KasBank", "-", None))
        self.lb_KasMasuk_Tambah_Form_NoAkun.setText(_translate("st_KasBank", "Akun Kas :", None))
        self.lb_KasMasuk_Tambah_Form_Penyetor.setText(_translate("st_KasBank", "Dari :", None))
        self.lb_KasMasuk_Tambah_Form_Nilai.setText(_translate("st_KasBank", "Rp 0", None))
        self.lb_KasMasuk_Tambah_Form_LabelNilai.setText(_translate("st_KasBank", "Besar Total :", None))
        self.lb_KasMasuk_Tambah_Form_Catatan.setText(_translate("st_KasBank", "Catatan :", None))
        self.lb_KasMasuk_Tambah_Form_Nomor.setText(_translate("st_KasBank", "Nomor Referensi :", None))
        self.lb_KasKeluar_Judul.setText(_translate("st_KasBank", "Kas Keluar", None))
        item = self.tbl_KasKeluar.horizontalHeaderItem(0)
        item.setText(_translate("st_KasBank", "Tanggal", None))
        item = self.tbl_KasKeluar.horizontalHeaderItem(1)
        item.setText(_translate("st_KasBank", "Nomor Referensi", None))
        item = self.tbl_KasKeluar.horizontalHeaderItem(2)
        item.setText(_translate("st_KasBank", "Penerima", None))
        item = self.tbl_KasKeluar.horizontalHeaderItem(3)
        item.setText(_translate("st_KasBank", "Keterangan", None))
        item = self.tbl_KasKeluar.horizontalHeaderItem(4)
        item.setText(_translate("st_KasBank", "Nilai", None))
        self.tb_KasKeluar_Buka.setText(_translate("st_KasBank", "Buka", None))
        self.tb_KasKeluar_Delete.setText(_translate("st_KasBank", "Hapus", None))
        self.tb_KasKeluar_Tutup.setText(_translate("st_KasBank", "Tutup", None))


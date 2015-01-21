# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kasbank/ui_kasbank.ui'
#
# Created: Wed Jan 21 07:02:27 2015
#      by: PyQt4 UI code generator 4.10.4
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
        self.st_KasBank_Menu = QtGui.QWidget()
        self.st_KasBank_Menu.setObjectName(_fromUtf8("st_KasBank_Menu"))
        self.igr_KasBank_Menu = QtGui.QGridLayout(self.st_KasBank_Menu)
        self.igr_KasBank_Menu.setObjectName(_fromUtf8("igr_KasBank_Menu"))
        self.fr_KasBank_Menu_Content = QtGui.QFrame(self.st_KasBank_Menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_KasBank_Menu_Content.sizePolicy().hasHeightForWidth())
        self.fr_KasBank_Menu_Content.setSizePolicy(sizePolicy)
        self.fr_KasBank_Menu_Content.setMinimumSize(QtCore.QSize(640, 480))
        self.fr_KasBank_Menu_Content.setMaximumSize(QtCore.QSize(640, 480))
        self.fr_KasBank_Menu_Content.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_KasBank_Menu_Content.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_KasBank_Menu_Content.setObjectName(_fromUtf8("fr_KasBank_Menu_Content"))
        self.tb_KasBank_Menu_KasMasuk = QtGui.QPushButton(self.fr_KasBank_Menu_Content)
        self.tb_KasBank_Menu_KasMasuk.setGeometry(QtCore.QRect(30, 60, 151, 161))
        self.tb_KasBank_Menu_KasMasuk.setObjectName(_fromUtf8("tb_KasBank_Menu_KasMasuk"))
        self.tb_KasBank_Menu_KasKeluar = QtGui.QPushButton(self.fr_KasBank_Menu_Content)
        self.tb_KasBank_Menu_KasKeluar.setGeometry(QtCore.QRect(190, 60, 151, 161))
        self.tb_KasBank_Menu_KasKeluar.setObjectName(_fromUtf8("tb_KasBank_Menu_KasKeluar"))
        self.igr_KasBank_Menu.addWidget(self.fr_KasBank_Menu_Content, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_KasBank_Menu.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_KasBank_Menu.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_KasBank_Menu.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_KasBank_Menu.addItem(spacerItem3, 1, 2, 1, 1)
        st_KasBank.addWidget(self.st_KasBank_Menu)

        self.retranslateUi(st_KasBank)
        QtCore.QMetaObject.connectSlotsByName(st_KasBank)

    def retranslateUi(self, st_KasBank):
        st_KasBank.setWindowTitle(_translate("st_KasBank", "StackedWidget", None))
        self.tb_KasBank_Menu_KasMasuk.setText(_translate("st_KasBank", "Kas Masuk", None))
        self.tb_KasBank_Menu_KasKeluar.setText(_translate("st_KasBank", "Kas Keluar", None))


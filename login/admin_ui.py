# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login/admin_ui.ui'
#
# Created: Mon Feb  2 14:22:47 2015
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

class Ui_fr_Admin(object):
    def setupUi(self, fr_Admin):
        fr_Admin.setObjectName(_fromUtf8("fr_Admin"))
        fr_Admin.resize(679, 571)
        fr_Admin.setStyleSheet(_fromUtf8("QFrame{\n"
"    border:0px;\n"
"}"))
        fr_Admin.setFrameShape(QtGui.QFrame.StyledPanel)
        fr_Admin.setFrameShadow(QtGui.QFrame.Raised)
        self.igr_Admin = QtGui.QGridLayout(fr_Admin)
        self.igr_Admin.setObjectName(_fromUtf8("igr_Admin"))
        self.st_Admin = QtGui.QStackedWidget(fr_Admin)
        self.st_Admin.setObjectName(_fromUtf8("st_Admin"))
        self.st_Menu = QtGui.QWidget()
        self.st_Menu.setObjectName(_fromUtf8("st_Menu"))
        self.igr_Menu = QtGui.QGridLayout(self.st_Menu)
        self.igr_Menu.setObjectName(_fromUtf8("igr_Menu"))
        self.tb_TutupAdmin = QtGui.QPushButton(self.st_Menu)
        self.tb_TutupAdmin.setMinimumSize(QtCore.QSize(40, 40))
        self.tb_TutupAdmin.setMaximumSize(QtCore.QSize(100, 40))
        self.tb_TutupAdmin.setObjectName(_fromUtf8("tb_TutupAdmin"))
        self.igr_Menu.addWidget(self.tb_TutupAdmin, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Menu.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Menu.addItem(spacerItem1, 1, 0, 1, 1)
        self.fr_Main = QtGui.QFrame(self.st_Menu)
        self.fr_Main.setMinimumSize(QtCore.QSize(320, 240))
        self.fr_Main.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Main.setObjectName(_fromUtf8("fr_Main"))
        self.tb_EditAdmin = QtGui.QPushButton(self.fr_Main)
        self.tb_EditAdmin.setGeometry(QtCore.QRect(70, 130, 191, 61))
        self.tb_EditAdmin.setObjectName(_fromUtf8("tb_EditAdmin"))
        self.tb_ListUser = QtGui.QPushButton(self.fr_Main)
        self.tb_ListUser.setGeometry(QtCore.QRect(70, 60, 191, 61))
        self.tb_ListUser.setObjectName(_fromUtf8("tb_ListUser"))
        self.igr_Menu.addWidget(self.fr_Main, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Menu.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Menu.addItem(spacerItem3, 0, 1, 1, 1)
        self.st_Admin.addWidget(self.st_Menu)
        self.st_Gaul = QtGui.QWidget()
        self.st_Gaul.setObjectName(_fromUtf8("st_Gaul"))
        self.verticalLayout = QtGui.QVBoxLayout(self.st_Gaul)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.st_Gaul)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tbl_ListUser_List = QtGui.QTableWidget(self.st_Gaul)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tbl_ListUser_List.sizePolicy().hasHeightForWidth())
        self.tbl_ListUser_List.setSizePolicy(sizePolicy)
        self.tbl_ListUser_List.setObjectName(_fromUtf8("tbl_ListUser_List"))
        self.tbl_ListUser_List.setColumnCount(2)
        self.tbl_ListUser_List.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tbl_ListUser_List.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbl_ListUser_List.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tbl_ListUser_List)
        self.frame = QtGui.QFrame(self.st_Gaul)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.st_Admin.addWidget(self.st_Gaul)
        self.igr_Admin.addWidget(self.st_Admin, 1, 0, 1, 1)

        self.retranslateUi(fr_Admin)
        self.st_Admin.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fr_Admin)

    def retranslateUi(self, fr_Admin):
        fr_Admin.setWindowTitle(_translate("fr_Admin", "Frame", None))
        self.tb_TutupAdmin.setText(_translate("fr_Admin", "Tutup Admin", None))
        self.tb_EditAdmin.setText(_translate("fr_Admin", "Edit Admin", None))
        self.tb_ListUser.setText(_translate("fr_Admin", "List User", None))
        self.label.setText(_translate("fr_Admin", "Users", None))
        item = self.tbl_ListUser_List.horizontalHeaderItem(0)
        item.setText(_translate("fr_Admin", "Username", None))
        item = self.tbl_ListUser_List.horizontalHeaderItem(1)
        item.setText(_translate("fr_Admin", "Kewenangan", None))


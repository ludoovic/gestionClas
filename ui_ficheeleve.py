# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/AELION/AppData/Local/Temp/ficheeleveXNPPRM.ui',
# licensing of 'C:/Users/AELION/AppData/Local/Temp/ficheeleveXNPPRM.ui' applies.
#
# Created: Mon Aug 19 15:09:44 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1036, 887)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nom = QtWidgets.QLabel(Dialog)
        self.nom.setObjectName("nom")
        self.gridLayout.addWidget(self.nom, 0, 3, 1, 1)
        self.labelp = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.labelp.setFont(font)
        self.labelp.setMargin(0)
        self.labelp.setObjectName("labelp")
        self.gridLayout.addWidget(self.labelp, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.labela = QtWidgets.QLabel(Dialog)
        self.labela.setObjectName("labela")
        self.gridLayout.addWidget(self.labela, 2, 1, 1, 1)
        self.prenom = QtWidgets.QLabel(Dialog)
        self.prenom.setObjectName("prenom")
        self.gridLayout.addWidget(self.prenom, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.NOM = QtWidgets.QLabel(Dialog)
        self.NOM.setObjectName("NOM")
        self.gridLayout.addWidget(self.NOM, 0, 1, 1, 1)
        self.adresse = QtWidgets.QLabel(Dialog)
        self.adresse.setObjectName("adresse")
        self.gridLayout.addWidget(self.adresse, 2, 3, 1, 1)
        self.photo = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo.sizePolicy().hasHeightForWidth())
        self.photo.setSizePolicy(sizePolicy)
        self.photo.setMinimumSize(QtCore.QSize(210, 270))
        self.photo.setMaximumSize(QtCore.QSize(100, 200))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("chattigre.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 1, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setShowGrid(True)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.radarchart = QtWidgets.QVBoxLayout()
        self.radarchart.setObjectName("radarchart")
        self.horizontalLayout.addLayout(self.radarchart)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.nom.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
        self.labelp.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">PRENOM</span></p></body></html>", None, -1))
        self.labela.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">ADRESSE</span></p></body></html>", None, -1))
        self.prenom.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))
        self.NOM.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">NOM</span></p></body></html>", None, -1))
        self.adresse.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))


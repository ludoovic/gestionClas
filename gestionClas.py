import sys, json
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QDialog, QTableWidgetItem)
from PySide2 import QtCore, QtUiTools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from ui_elevRechDesign import Ui_mainWindow
from ui_ficheeleve import Ui_Dialog


filename = "dataNotes.json"

def indexAcadSelec(acadSelec, dico):
    cpt = 0
    for academie in dico:
        if academie["nom"] == acadSelec:
            break
        else:
            cpt += 1
    return cpt

def indexEtabSelec(etabSelec, dico):
    cpt = 0
    for etablissement in dico:
        if etablissement["nom"] == etabSelec:
            break
        else:
            cpt += 1
    return cpt

def indexClassSelec(classSelec, dico):
    cpt = 0
    for classe in dico:
        if classe["nom"] == classSelec:
            break
        else:
            cpt += 1
    return cpt

def indexElevSelec(elevSelec, dico):
    cpt = 0
    for eleve in dico:
        if eleve["nom"] == elevSelec:
            break
        else:
            cpt += 1
    return cpt

class eleveRech(QMainWindow):
    def __init__(self):
        super(eleveRech, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesData = {}
        self.mesdata = self.lireJSON(filename)
        self.initAcademies()
        self.initEtablissements()
        self.initClasses()
        self.elevChanged()

        self.ui.cbAcad.currentIndexChanged.connect(self.acadChanged)
        self.ui.cbEtab.currentIndexChanged.connect(self.etabChanged)
        self.ui.cbClass.currentIndexChanged.connect(self.classChanged)
        self.ui.tableWidget.cellDoubleClicked.connect(self.affFichEl)

    def initAcademies(self):
        self.ui.cbAcad.clear()
        malisteAcad = []
        for a in self.mesdata["academies"]:
            malisteAcad.append(a["nom"])
        self.ui.cbAcad.addItems(malisteAcad)

    def initEtablissements(self):
        self.ui.cbEtab.clear()
        malisteEtab = []
        for e in self.mesdata["academies"][0]["etablissements"]:
            malisteEtab.append(e["nom"])
        self.ui.cbEtab.addItems(malisteEtab)

    def initClasses(self):
        self.ui.cbClass.clear()
        malisteClass = []
        for c in self.mesdata["academies"][0]["etablissements"][0]["classes"]:
            malisteClass.append(c["nom"])
        self.ui.cbClass.addItems(malisteClass)

###############################################################################################

    def acadChanged(self):
        indexAcad = indexAcadSelec(self.ui.cbAcad.currentText(), self.mesdata["academies"])
        self.ui.cbEtab.currentIndexChanged.disconnect(self.etabChanged)
        self.ui.cbEtab.clear()
        malisteEtab = []
        for e in self.mesdata["academies"][indexAcad]["etablissements"]:
            malisteEtab.append(e["nom"])
        self.ui.cbEtab.addItems(malisteEtab)
        self.etabChanged()
        self.ui.cbEtab.currentIndexChanged.connect(self.etabChanged)

    def etabChanged(self):
        indexAcad = indexAcadSelec(self.ui.cbAcad.currentText(), self.mesdata["academies"])
        indexEtab = indexEtabSelec(self.ui.cbEtab.currentText(), self.mesdata["academies"][indexAcad]["etablissements"])
        self.ui.cbClass.currentIndexChanged.disconnect(self.classChanged)
        self.ui.cbClass.clear()
        malisteClass = []
        print("indexEtab"+str(indexEtab))
        for c in self.mesdata["academies"][indexAcad]["etablissements"][indexEtab]["classes"]:
            malisteClass.append(c["nom"])
        self.ui.cbClass.addItems(malisteClass)
        self.classChanged()
        self.ui.cbClass.currentIndexChanged.connect(self.classChanged)

    def classChanged(self):
        indexAcad = indexAcadSelec(self.ui.cbAcad.currentText(), self.mesdata["academies"])
        indexEtab = indexEtabSelec(self.ui.cbEtab.currentText(), self.mesdata["academies"][indexAcad]["etablissements"])
        indexClass = indexClassSelec(self.ui.cbClass.currentText(), self.mesdata["academies"][indexAcad]["etablissements"][indexEtab]["classes"])
        malisteElev = []
        for elev in self.mesdata["academies"][indexAcad]["etablissements"][indexEtab]["classes"][indexClass]["eleves"]:
            malisteElev.append(elev["nom"])
        self.elevChanged()

    def elevChanged(self):
        indexAcad = indexAcadSelec(self.ui.cbAcad.currentText(), self.mesdata["academies"])
        indexEtab = indexEtabSelec(self.ui.cbEtab.currentText(), self.mesdata["academies"][indexAcad]["etablissements"])
        indexClass = indexClassSelec(self.ui.cbClass.currentText(),self.mesdata["academies"][indexAcad]["etablissements"][indexEtab]["classes"])
        listelev = self.mesdata["academies"][indexAcad]["etablissements"][indexEtab]["classes"][indexClass]["eleves"]

        self.ui.tableWidget.setRowCount(len(listelev))
        self.ui.tableWidget.setColumnCount(2)
        cpt = 0
        for elev in listelev:
            self.ui.tableWidget.setItem(cpt, 0, QTableWidgetItem(elev["nom"]))
            self.ui.tableWidget.setItem(cpt, 1, QTableWidgetItem(elev["prenom"]))
            cpt += 1

    def affFichEl(self):
        wAff = QDialog()
        uiAff = Ui_Dialog()
        uiAff.setupUi(wAff)

        freq = [np.random.randint(100, 200), np.random.randint(100, 200), np.random.randint(100, 200),
                np.random.randint(200, 300),
                np.random.randint(300, 400), np.random.randint(500, 600), np.random.randint(700, 800),
                np.random.randint(700, 800),
                np.random.randint(500, 600), np.random.randint(300, 400), np.random.randint(200, 300),
                np.random.randint(100, 200)]
        mois = range(1, 13)

        fig, ax = plt.subplots()
        ax.plot(mois, freq)

        plt.xticks(np.arange(min(mois), max(mois) + 1, 1.0))

        ax.set(xlabel='mois', ylabel='fréq.',
               title='Fréquentation du centre')
        ax.grid(True, linestyle='dotted')

        canvas = FigureCanvas(fig)
        uiAff.horizontalLayout.addWidget(canvas)
        self.setLayout(uiAff.horizontalLayout)

        wAff.exec_()

    def lireJSON(self, filename):
        with open(filename) as json_file:
            dico = json.load(json_file)
            return dico
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = eleveRech()
    window.show()

    sys.exit(app.exec_())
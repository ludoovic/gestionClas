import sys, json
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow)
from PySide2 import QtCore, QtUiTools

from ui_elevRechDesign import Ui_mainWindow

filename = "dataNotes.json"

def indexAcadSelec(acadSelec, dico):
    cpt = 0
    for academie in dico:
        if academie["nom"] == acadSelec:
            return cpt
            break
        else:
            cpt += 1

def indexEtabSelec(etabSelec, dico):
    cpt = 0
    for etablissement in dico:
        if etablissement["nom"] == etabSelec:
            return cpt
            break
        else:
            cpt += 1

def indexClassSelec(classSelec, dico):
    cpt = 0
    for classe in dico:
        if classe["nom"] == classSelec:
            return cpt
            break
        else:
            cpt += 1

def indexElevSelec(elevSelec, dico):
    cpt = 0
    for eleve in dico:
        if eleve["nom"] == elevSelec:
            return cpt
            break
        else:
            cpt += 1

def indexMatierSelec(matierSelec, dico):
    cpt = 0
    for matiere in dico:
        if matiere["nom"] == matierSelec:
            return cpt
            break
        else:
            cpt += 1

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
        self.initEleves()
        self.initMatieres()

        self.ui.cbAcad.currentIndexChanged.connect(self.acadChanged)
        self.ui.cbEtab.currentIndexChanged.connect(self.etabChanged)
        self.ui.cbClass.currentIndexChanged.connect(self.classChanged)
        self.ui.cbElev.currentIndexChanged.connect(self.elevChanged)
        self.ui.cbMatier.currentIndexChanged.connect(self.matierChanged)

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

    def initEleves(self):
        self.ui.cbElev.clear()
        malisteElev = []
        for elev in self.mesdata["academies"][0]["etablissements"][0]["classes"][0]["eleves"]:
            malisteElev.append(elev["nom"])
        self.ui.cbElev.addItems(malisteElev)

    def initMatieres(self):
        self.ui.cbMatier.clear()
        malisteMatier = []
        for m in self.mesdata["academies"][0]["etablissements"][0]["classes"][0]["eleves"][0]["matieres"]:
            malisteMatier.append(m["nom"])
        self.ui.cbMatier.addItems(malisteMatier)
###############################################################################################

    def acadChanged(self):
        indexAcad = indexAcadSelec(self.ui.cbAcad.currentText(), self.mesdata["academies"])
        self.ui.cbEtab.currentIndexChanged.disconnect(self.etabChanged)
        self.ui.cbEtab.clear()
        malisteEtab = []
        for e in self.mesdata["academies"][indexAcad]["etablissements"]:
            malisteEtab.append(e["nom"])
        self.ui.cbEtab.addItems(malisteEtab)
        self.etabChanged(indexAcad)
        self.ui.cbEtab.currentIndexChanged.connect(self.etabChanged)

    def etabChanged(self, aselect=0):
        indexEtab = indexEtabSelec(self.ui.cbEtab.currentText(), self.mesdata["academies"][aselect]["etablissements"])
        self.ui.cbClass.currentIndexChanged.disconnect(self.classChanged)
        self.ui.cbClass.clear()
        malisteClass = []
        for c in self.mesdata["academies"][aselect]["etablissements"][indexEtab]["classes"]:
            malisteClass.append(c["nom"])
        self.ui.cbClass.addItems(malisteClass)
        self.classChanged(aselect, indexEtab)
        self.ui.cbClass.currentIndexChanged.connect(self.classChanged)

    def classChanged(self, aselect=0, eselect=0):
        indexClass = indexClassSelec(self.ui.cbClass.currentText(), self.mesdata["academies"][aselect]["etablissements"][eselect]["classes"])
        self.ui.cbElev.currentIndexChanged.disconnect(self.elevChanged)
        self.ui.cbElev.clear()
        malisteElev = []
        for elev in self.mesdata["academies"][aselect]["etablissements"][eselect]["classes"][indexClass]["eleves"]:
            malisteElev.append(elev["nom"])
        self.ui.cbElev.addItems(malisteElev)
        self.elevChanged(aselect, eselect, indexClass)
        self.ui.cbElev.currentIndexChanged.connect(self.elevChanged)

    def elevChanged(self, aselect=0, eselect=0, elselect=0):
        # indexElev = indexElevSelec(self.ui.cbElev.currentText(), self.mesdata["eleves"])
        # self.ui.cbMatier = []
        # for m in self.mesdata["Eleves"][indexElev]["matieres"]:
        #     malisteElev.append(matier["nom"])
        # self.ui.cbMatier.addItems(malisteMatier)
        print(aselect, eselect, elselect)

    def matierChanged(self):
        print(self.ui.cbMatier.currentText())

    # def initSaisieEleve(self):
    #     cpt = 0
    #     self.ui.twNotes.clear()
    #     self.ui.twNotes.setColumnCount(2)
    #     mesdata = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"]
    #     for eleve in dicoClasse["eleves"]:
    #         for matiere in eleve["matieres"]:
    #             mat = self.ui.cbMatier.currentText()
    #             if matiere["nom"] == mat:
    #                 nomE = eleve["nom"]
    #                 self.ui.twNotes.setRowCount(cpt+1)
    #                 itemE = QTableWidgetItem(nomE)
    #                 self.ui.twNotes.setItem(cpt, 0, itemE)
    #                 spinB = QDoubleSpinBox()
    #                 spinB.setProperty("nom", nomE)
    #                 self.ui.twNotes;setCellWidget(cpt, 1, spinB)
    #                 cpt = cpt + 1
    #
    #     self.ui.twNotes.setHorizontalHeaderLabels(["Nom", "Note"])

    # self.ui.lecture.clicked.connect(self.lectureClicked)
    # self.mediaPlayer = QMediaPlayer()
    # self.mediaPlayer.setVideoOutput(self.ui.ecran)
    #
    # self.ui.pause.clicked.connect(self.pauseClicked)
    # self.ui.suivant.clicked.connect(self.suivantClicked)
    # self.ui.stop.clicked.connect(self.stopClicked)
    # self.ui.precedent.clicked.connect(self.precedentClicked)

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
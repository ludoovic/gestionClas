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

class eleveRech(QMainWindow):
    def __init__(self):
        super(eleveRech, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesData = {}
        self.mesdata = self.lireJSON(filename)
        self.updateAcademies()
        self.updateEtablissements()
        self.updateClasses()
        self.updateEleves()
        self.updateMatieres()

        self.ui.cbAcad.currentIndexChanged.connect(self.acadChanged)
        self.ui.cbEtab.currentIndexChanged.connect(self.etabChanged)
        self.ui.cbClass.currentIndexChanged.connect(self.classChanged)
        self.ui.cbElev.currentIndexChanged.connect(self.elevChanged)
        self.ui.cbMatier.currentIndexChanged.connect(self.matierChanged)


    def updateAcademies(self):
        self.ui.cbAcad.clear()
        malisteAcad = []
        for a in self.mesdata["academies"]:
            malisteAcad.append(a["nom"])
        self.ui.cbAcad.addItems(malisteAcad)

        print("l'index de l'academie de Toulouse est:")
        print(indexAcadSelec("Toulouse", self.mesdata["academies"]))

    def updateEtablissements(self):
        self.ui.cbEtab.clear()
        malisteEtab = []
        for e in self.mesdata["academies"][0]["etablissements"]:
            malisteEtab.append(e["nom"])
        self.ui.cbEtab.addItems(malisteEtab)

    def updateClasses(self):
        self.ui.cbClass.clear()
        malisteClass = []
        for c in self.mesdata["academies"][0]["etablissements"][0]["classes"]:
            malisteClass.append(c["nom"])
        self.ui.cbClass.addItems(malisteClass)

    def updateEleves(self):
        self.ui.cbElev.clear()
        malisteElev = []
        for elev in self.mesdata["academies"][0]["etablissements"][0]["classes"][0]["eleves"]:
            malisteElev.append(elev["nom"])
        self.ui.cbElev.addItems(malisteElev)

    def updateMatieres(self):
        self.ui.cbMatier.clear()
        malisteMatier = []
        for m in self.mesdata["academies"][0]["etablissements"][0]["classes"][0]["eleves"][0]["matieres"]:
            malisteMatier.append(m["nom"])
        self.ui.cbMatier.addItems(malisteMatier)

    def acadChanged(self):
        indexAcad = indexAcadSelec(self.ui.cbAcad.currentText(), self.mesdata["academies"])
        self.ui.cbEtab.clear()
        malisteEtab = []
        for e in self.mesdata["academies"][indexAcad]["etablissements"]:
            malisteEtab.append(e["nom"])
        self.ui.cbEtab.addItems(malisteEtab)

    def etabChanged(self):
        print(self.ui.cbEtab.currentText())

    def classChanged(self):
        print(self.ui.cbClass.currentText())

    def elevChanged(self):
        print(self.ui.cbElev.currentText())

    def matierChanged(self):
        print(self.ui.cbMatier.currentText())

    # def updateSaisieEleve(self):
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
import sys, json
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow)
from PySide2 import QtCore, QtUiTools

from ui_elevRechDesign import Ui_MainWindow

filename = "dataNotes.json"

class eleveRech(QMainWindow):
    def __init__(self):
        super(eleveRech, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesData = {}

        self.mesdata = self.lireJSON(filename)

        self.updateAcademies()


    def updateAcademies(self):
        self.ui.cbAcad.clear()
        maliste = []
        for a in self.mesdata["academies"]:
            maliste.append(a["nom"])
        # maliste.append("Paris")
        self.ui.cbAcad.addItems(maliste)

    def updateEtablissements(self):
        self.ui.cbEtab.clear()
        for e in self.mesdata["academies"][self.ui.cbAcad.currentIndex()]["etablissements"]:
            self.ui.cbEtab.addItem(e["nom"])
    #
    # def updateClasse(self):
    #     self.ui.cbClass.clear()
    #     for a in self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"]:
    #         self.ui.cbClass.addItem(a["nom"])
    #
    # def updateMatiere(self):
    #     self.ui.cbMatier.clear()
    #     dicoClasse = self.dico["academies"][self.ui.academie.currentIndex()]["etablissements"]:
    #     listeMatieres = []
    #     for eleve in dicoClasse["eleves"]:
    #         for matiere in eleve[matieres["nom"]]:
    #         listeMatieresUniques = np.unique(listeMatieres)
    #
    #
    # def updateSaisieEleve(self):
    #     cpt = 0
    #     self.ui.twNotes.clear()
    #     self.ui.twNotes.setColumnCount(2)
    #     dicoClasse = self.dico["academies"][self.ui.cbAcademie.currentIndex()]["etablissements"]
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
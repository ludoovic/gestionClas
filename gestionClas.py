import sys, json
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QDialog, QTableWidgetItem, QInputDialog, QDoubleSpinBox)
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

        self.wAff = QDialog()
        self.uiAff = Ui_Dialog()
        self.uiAff.setupUi(self.wAff)

        global filename
        self.mesData = {}
        self.mesdata = self.lireJSON(filename)

        self.ui.cbAcad.currentIndexChanged.connect(self.acadChanged)
        self.ui.cbEtab.currentIndexChanged.connect(self.etabChanged)
        self.ui.cbClass.currentIndexChanged.connect(self.classChanged)
        self.ui.cbMatier.currentIndexChanged.connect(self.elevChanged)

        self.ui.tableWidget.cellDoubleClicked.connect(self.affFichEl)

        self.initAcademies()

        #self.ui.cbElev.QInputDialog(self)

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
        indexClass = indexClassSelec(self.ui.cbClass.currentText(), self.mesdata["academies"][indexAcad][
            "etablissements"][indexEtab]["classes"])
        listelev = self.mesdata["academies"][indexAcad]["etablissements"][indexEtab]["classes"][indexClass]["eleves"]

        self.ui.tableWidget.setRowCount(len(listelev))
        self.ui.tableWidget.setColumnCount(2)
        cpt = 0
        for elev in listelev:
            self.ui.tableWidget.setItem(cpt, 0, QTableWidgetItem(elev["nom"]))
            self.ui.tableWidget.setItem(cpt, 1, QTableWidgetItem(elev["prenom"]))
            cpt += 1

            # dicoClasse = self.dico["academies"][self.ui.cbAcad.currentIndex()]["etablissements"][
            #     self.ui.cbEtab.currentIndex()]["classes"][self.ui.cbClass.currentIndex()]
            # for eleve in dicoClasse["eleves"]:
            for matiere in elev["matieres"]:
                mat = self.ui.cbMatier.currentText()
                if matiere["nom"] == mat:
                    nomE = elev["nom"]
                    self.ui.tableWidget.setRowCount(cpt + 1)
                    itemE = QTableWidgetItem(nomE)
                    self.ui.tableWidget.setItem(cpt, 0, itemE)
                    spinB = QDoubleSpinBox()
                    spinB.setProperty("nom", nomE)
                    self.ui.tableWidget.setCellWidget(cpt, 1, spinB)
                    cpt = cpt + 1

            self.ui.tableWidget.setHorizontalHeaderLabels(['Nom', 'Note'])

    def updateMatiere(self):
        dicoClasse = self.dico["academies"][self.ui.cbAcad.currentIndex()]["etablissements"][
            self.ui.cbEtab.currentIndex()]["classes"][self.ui.cbClass.currentIndex()]
        listeMatieres = []
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                listeMatieres.append(matiere["nom"])
                nomE = eleve["nom"]
                self.ui.tableWidget.setRowCount(cpt + 1)
                itemE = QTableWidgetItem(nomE)
                self.ui.tableWidget.setItem(cpt, 0, itemE)
                spinB = QDoubleSpinBox()
                spinB.setProperty("nom", nomE)
                self.ui.tableWidget.setCellWidget(cpt, 1, spinB)
                cpt = cpt + 1

            self.uiAff.tableView.setHorizontalHeaderLabels(['Nom', 'Note'])

        listeMatieresUniques = np.unique(listeMatieres)
        self.ui.cbMatier.addItems(listeMatieresUniques)


    def affFichEl(self):
        print(self.ui.tableWidget.currentItem().text())

        labels = []
        for a in self.mesdata["academies"]:
            for e in a["etablissements"]:
                for c in e["classes"]:
                    for elev in c["eleves"]:
                        if elev['nom']  == self.ui.tableWidget.currentItem().text():
                            print("Trouvé !")


        # freq = [np.random.randint(100, 200), np.random.randint(100, 200), np.random.randint(100, 200),
        #         np.random.randint(200, 300),
        #         np.random.randint(300, 400), np.random.randint(500, 600), np.random.randint(700, 800),
        #         np.random.randint(700, 800),
        #         np.random.randint(500, 600), np.random.randint(300, 400), np.random.randint(200, 300),
        #         np.random.randint(100, 200)]
        # mois = range(1, 13)
        #
        # fig, ax = plt.subplots()
        # ax.plot(mois, freq)
        #
        # plt.xticks(np.arange(min(mois), max(mois) + 1, 1.0))
        #
        # ax.set(xlabel='mois', ylabel='fréq.',
        #        title='Fréquentation du centre')
        # ax.grid(True, linestyle='dotted')
        #
        # canvas = FigureCanvas(fig)
        # uiAff.horizontalLayout.addWidget(canvas)
        # self.setLayout(uiAff.horizontalLayout)

        # angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
        # # close the plot
        # moyenneEleveR = np.concatenate((moysE, [moysE[0]]))
        # moyenneClasseR = np.concatenate((listMoyC, [listMoyC[0]]))
        # angles = np.concatenate((angles, [angles[0]]))
        #
        # self.fig = plt.figure()
        # ax = self.fig.add_subplot(111, polar=True)
        # ax.plot(angles, moyenneEleveR, 'o-', linewidth=2, label="Elève")
        # ax.fill(angles, moyenneEleveR, alpha=0.2)
        # ax.plot(angles, moyenneClasseR, 'o-', linewidth=2, label="Classe")
        # ax.fill(angles, moyenneClasseR, alpha=0.2)
        # ax.set_thetagrids(angles * 180 / np.pi, labels)
        # plt.yticks([2, 4, 6, 8, 10, 12, 14, 16, 18], color="grey", size=7)
        # plt.ylim(0, 20)
        #
        # ax.set_title(eleveR)
        # ax.grid(True)
        # plt.legend(loc='upper right')
        #
        # self.canvas = FigureCanvas(self.fig)  # the matplotlib canvas
        # self.ui.qRadar.addWidget(self.canvas)
        #
        # self.setLayout(self.ui.qRadar)
        # self.show()

        self.wAff.exec_()

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
from GUI.Steps import Ui_Form
from PyQt5 import QtWidgets, QtGui
from src.Pages.Page1 import Page1


class Page2(QtWidgets.QWizardPage, Ui_Form):
    constituents = []
    Ai = []

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setupUi(self)
        self.setTitle("Шаг 2.")
        self.setSubTitle(
            "Введите интересующий объем каждой составляющей.")
        self.group_box_right.setTitle("Интересующий объем составляющих:")
        self.layout_left = self.group_box_left.layout()
        self.layout_right = self.group_box_right.layout()

    def change_fields_num(self):
        """Change number of QLineEdit in each column"""
        if len(Page1.constituents) > len(Page2.constituents):
            print("add ", len(Page1.constituents) - len(Page2.constituents), "to 2nd page")
            for i in range(len(Page1.constituents) - len(Page2.constituents)):
                Page2.constituents.append(QtWidgets.QLabel(Page1.constituents[len(Page2.constituents)].text()))
                self.layout_left.addWidget(Page2.constituents[-1])

                Page2.Ai.append(QtWidgets.QLineEdit())
                self.registerField("Ai" + str(len(Page2.Ai) - 1) + "*", Page2.Ai[-1])
                Page2.Ai[-1].setValidator(QtGui.QDoubleValidator())
                self.layout_right.addWidget(Page2.Ai[-1])
        else:
            for i in range(len(Page2.constituents) - len(Page1.constituents)):
                Page2.constituents[-1].deleteLater()
                self.layout_left.removeWidget(Page2.constituents.pop())
                Page2.Ai[-1].deleteLater()
                self.layout_right.removeWidget(Page2.Ai.pop())
        self.check_changes()

    def check_changes(self):
        """Revalidation"""
        for i in range(len(Page2.constituents)):
            if Page2.constituents[i].text() != Page1.constituents[i].text():
                Page2.constituents[i].setText(Page1.constituents[i].text())

from GUI.Steps import Ui_Form
from PyQt5 import QtWidgets, QtGui
from src.Pages.Page1 import Page1


class Page3(QtWidgets.QWizardPage, Ui_Form):
    constituents = []
    nii = []

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setupUi(self)
        self.setTitle("Шаг 3.")
        self.setSubTitle(
            "Введите объемы понятий о каждой составляющей нововедения.")
        self.group_box_right.setTitle("Объем понятия о составляющей нововведения:")
        self.layout_left = self.group_box_left.layout()
        self.layout_right = self.group_box_right.layout()

    def change_fields_num(self):
        """Change number of QLineEdit in each column"""
        if len(Page1.constituents) > len(Page3.constituents):
            for i in range(len(Page1.constituents) - len(Page3.constituents)):
                Page3.constituents.append(QtWidgets.QLabel(Page1.constituents[len(Page3.constituents)].text()))
                self.layout_left.addWidget(Page3.constituents[-1])

                Page3.nii.append(QtWidgets.QLineEdit())
                self.registerField("nii" + str(len(Page3.nii) - 1) + "*", Page3.nii[-1])
                Page3.nii[-1].setValidator(QtGui.QDoubleValidator())
                self.layout_right.addWidget(Page3.nii[-1])
        else:
            for i in range(len(Page3.constituents) - len(Page1.constituents)):
                Page3.constituents[-1].deleteLater()
                self.layout_left.removeWidget(Page3.constituents.pop())
                Page3.nii[-1].deleteLater()
                self.layout_right.removeWidget(Page3.nii.pop())
        self.check_changes()

    def check_changes(self):
        """Revalidation"""
        for i in range(len(Page3.constituents)):
            if Page3.constituents[i].text() != Page1.constituents[i].text():
                Page3.constituents[i].setText(Page1.constituents[i].text())
from GUI.Steps import Ui_Form
from PyQt5 import QtWidgets, QtGui
from src.Pages.Page1 import Page1


class Page4(QtWidgets.QWizardPage, Ui_Form):

    def __init__(self, cross_id, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setupUi(self)
        self.group_box_right.setTitle("Приращение понятия:")
        self.layout_left = self.group_box_left.layout()
        self.layout_right = self.group_box_right.layout()
        self.constituents = []
        self.dnij = []
        self.cross_id = cross_id
        print("page_id = ", self.cross_id)

    def set_title(self, step_number):
        self.setTitle(f"Шаг {step_number}.")
        self.setSubTitle(
            f"Введите приращение понятия о составляющей {Page1.constituents[self.cross_id].text()} при наличии соответствующих составляющих:")

    def change_fields_num(self):
        """Change number of QLineEdit in each column"""
        if len(Page1.constituents) > len(self.constituents) + 1:
            for i in range(len(Page1.constituents) - len(self.constituents)):
                if i != self.cross_id:
                    self.constituents.append(QtWidgets.QLabel(Page1.constituents[i].text()))
                    self.layout_left.addWidget(self.constituents[-1])
                    self.dnij.append(QtWidgets.QLineEdit())
                    # self.registerField("dnij" + str(len(self.dnij) - 1) + "*", self.dnij[-1])
                    self.dnij[-1].setValidator(QtGui.QDoubleValidator())
                    self.layout_right.addWidget(self.dnij[-1])
        else:
            for i in range(len(self.constituents) - len(Page1.constituents) + 1):
                self.constituents[-1].deleteLater()
                self.layout_left.removeWidget(self.constituents.pop())
                self.dnij[-1].deleteLater()
                self.layout_right.removeWidget(self.dnij.pop())
        self.check_changes()

    def check_changes(self):
        """Revalidation"""
        j = 0
        for i in range(len(self.constituents)):
            if j == self.cross_id:
                j += 1
            print(i, " and ", j, " cross id = ", self.cross_id)
            if self.constituents[i].text() != Page1.constituents[j].text():
                self.constituents[i].setText(Page1.constituents[j].text())
            j += 1

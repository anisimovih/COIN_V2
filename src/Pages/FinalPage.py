import csv
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from src.Pages.Page1 import Page1
from src.Pages.Page2 import Page2
from src.Pages.Page3 import Page3



def str_to_float(string):
    return float(string.replace(',', '.'))


class Page5(QtWidgets.QWizardPage):

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Результаты.")
        self.box = QtWidgets.QVBoxLayout()
        self.lables = []
        self.h = []
        self.hvz = []

    def calculate_results(self, pages):
        """Calculate final results"""
        for i in range(len(Page1.constituents)):
            j = str_to_float(Page2.Ai[i].text()) / str_to_float(Page1.Ai_num[i].text())
            h = j / str_to_float(Page3.nii[i].text())
            hvz = 0

            for index in range(len(Page3.nii)):
                ji = str_to_float(Page2.Ai[index].text()) / str_to_float(Page1.Ai_num[index].text())
                if index == 0:
                    hvz += ji / str_to_float(Page3.nii[i].text())
                else:
                    hvz += ji / str_to_float(pages[i].dnij[index - 1].text())
            result = ("Значимость составляющей %s равна %.3g, а с учетом взаимного влияния %.3g" % (Page1.constituents[i].text(), h, hvz))
            self.hvz.append(int(hvz))
            self.h.append(int(h))
            self.lables.append(QtWidgets.QLabel(result))
            self.box.addWidget(self.lables[i])

        self.setLayout(self.box)

    def save_data(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print("\n\n\n", fname[0])
        with open(fname[0], mode='w') as csv_file:
            employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(["Название составляющей", "Значимость составляющей", "Значимость составляющей с учетом взаимного влияния"])
            for i in range(len(Page1.constituents)):
                employee_writer.writerow([Page1.constituents[i].text(), self.h[i], self.hvz[i]])

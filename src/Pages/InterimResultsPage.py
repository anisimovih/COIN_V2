from PyQt5 import QtWidgets
from src.Pages.Page1 import Page1
from src.Pages.Page2 import Page2
from src.Pages.Page3 import Page3


def str_to_float(string):
    return float(string.replace(',', '.'))


class InterimResultsPage(QtWidgets.QWizardPage):

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Промежуточные результаты:")
        self.box = QtWidgets.QVBoxLayout()
        self.lables = []
        self.h = []

    def calculate_interim_results(self):
        """Calculate second interim results"""
        last_lable = 0
        for i in range(len(Page1.constituents)):
            j = str_to_float(Page2.Ai[i].text()) / str_to_float(Page1.Ai_num[i].text())
            h = j / str_to_float(Page3.nii[i].text())
            result = ("Значимость составляющей %s равна %.3g" % (Page1.constituents[i].text(), h))
            self.h.append(int(h))
            self.lables.append(QtWidgets.QLabel(result))
            self.box.addWidget(self.lables[i])
            last_lable = i

        '''result = "Если вас устраивают промежуточне резльтаты, то можно продолжить, и начать вычисление значимости составляющих с учетом взаимного влияния. В противном случае можно изменить ранее введенные данные."
        self.lables.append(QtWidgets.QLabel(result))
        self.box.addWidget(self.lables[last_lable + 1])'''
        self.setLayout(self.box)

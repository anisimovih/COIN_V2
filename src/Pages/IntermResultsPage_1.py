from PyQt5 import QtWidgets
from src.Pages.Page1 import Page1
from src.Pages.Page2 import Page2


def str_to_float(string):
    return float(string.replace(',', '.'))


class InterimResultsPage1(QtWidgets.QWizardPage):

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Промежуточные результаты:")
        self.box = QtWidgets.QVBoxLayout()
        self.lables = []
        self.j = []

    def calculate_interim_results(self):
        """Calculate first interim results"""
        last_lable = 0
        last = ""
        for i in range(len(Page1.Ai_num)):
            j = str_to_float(Page1.Ai_num[i].text()) / str_to_float(Page2.Ai[i].text())
            result = (f'Интересующий объем составляющей "{Page1.constituents[i].text()}"  равен %.3g' % j)
            self.j.append(j)
            #last += result
            self.lables.append(QtWidgets.QLabel(result))
            self.box.addWidget(self.lables[i])
            last_lable = i
        #self.setSubTitle(last)

        '''result = "Если вас устраивают промежуточне резльтаты, то можно продолжить, и начать вычисление значимости составляющих с учетом взаимного влияния. В противном случае можно изменить ранее введенные данные."
        self.lables.append(QtWidgets.QLabel(result))
        self.box.addWidget(self.lables[last_lable + 1])'''
        self.setLayout(self.box)
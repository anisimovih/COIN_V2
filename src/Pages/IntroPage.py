from GUI.Intro import Ui_Form as Ui_Form_2
from PyQt5 import QtWidgets


class Page0(QtWidgets.QWizardPage, Ui_Form_2):
    constituents = []
    Ai_num = []

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setupUi(self)
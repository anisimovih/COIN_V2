from GUI.Steps import Ui_Form
from PyQt5 import QtWidgets, QtGui


class Page1(QtWidgets.QWizardPage, Ui_Form):
    constituents = []
    Ai_num = []

    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setupUi(self)
        self.spin_box = QtWidgets.QSpinBox()
        filler = QtWidgets.QLabel()

        self.layout_left = self.group_box_left.layout()
        self.layout_right = self.group_box_right.layout()

        self.layout_right.addWidget(filler)
        self.group_box_right.setTitle("Единицы измерения составляющих:")
        self.setTitle("Шаг 1.")
        self.setSubTitle(
            "Выберите колличество элементов, дайте им названия и определите единицы измерени каждой составляющей.")
        self.num = 0
        self.add_spin_box()

        self.change_fields_num(2)

    def add_spin_box(self):
        """Add spin_box to chose number of QLineEdit in each column"""
        self.layout_left.addWidget(self.spin_box)

        self.spin_box.setMinimum(2)
        self.spin_box.valueChanged.connect(lambda: self.change_fields_num(self.spin_box.value()))

    def change_fields_num(self, num):
        '''if num < 2:
            num = 2'''
        if num > self.num:
            for i in range(num - self.num):
                Page1.constituents.append(QtWidgets.QLineEdit())
                self.registerField("constituents" + str(len(Page1.constituents) - 1) + "*", Page1.constituents[-1])
                self.layout_left.addWidget(Page1.constituents[-1])

                Page1.Ai_num.append(QtWidgets.QLineEdit())
                self.registerField("Ai_num" + str(len(Page1.Ai_num) - 1) + "*", Page1.Ai_num[-1])
                Page1.Ai_num[-1].setValidator(QtGui.QDoubleValidator())
                self.layout_right.addWidget(Page1.Ai_num[-1])
        else:
            for i in range(self.num - num):
                Page1.constituents[-1].deleteLater()
                self.layout_left.removeWidget(Page1.constituents.pop())
                Page1.Ai_num[-1].deleteLater()
                self.layout_right.removeWidget(Page1.Ai_num.pop())
        self.num = num
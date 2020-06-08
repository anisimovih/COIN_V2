import sys
from src.Pages.IntroPage import Page0
from src.Pages.Page1 import Page1
from src.Pages.Page2 import Page2
from src.Pages.Page3 import Page3
from src.Pages.InterimResultsPage import InterimResultsPage
from src.Pages.IntermResultsPage_1 import InterimResultsPage1
from src.Pages.CrossPages import Page4
from src.Pages.FinalPage import Page5
from PyQt5 import QtWidgets


class Wizard(QtWidgets.QWizard):
    def __init__(self, parent=None, ):
        QtWidgets.QWizard.__init__(self, parent)
        self.setWindowTitle("Co-In_V2")
        self.setButtonText(0, "предыдущий шаг")
        self.setButtonText(1, "следующий шаг")
        self.setButtonText(6, "сохранить результаты")
        self.setOption(QtWidgets.QWizard.NoCancelButton)
        self.options()
        self.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
        self.page0 = Page0()
        self.page1 = Page1()
        self.page2 = Page2()
        self.interim_results_page_1 = InterimResultsPage1()
        self.page3 = Page3()
        self.interim_results_page = InterimResultsPage()
        self.page4 = []
        self.page5 = Page5()
        self.addPage(self.page0)
        self.addPage(self.page1)
        self.addPage(self.page2)
        self.addPage(self.interim_results_page_1)
        self.addPage(self.page3)
        self.addPage(self.interim_results_page)
        self.result_page = self.addPage(self.page5)
        self.button(self.NextButton).clicked.connect(lambda: self.next_button())
        self.button(QtWidgets.QWizard.CustomButton1).clicked.connect(lambda: self.save_data())

    def next_button(self):
        """Next button logic"""
        print(self.currentId())
        if self.currentId() == 5:
            self.interim_results_page.calculate_interim_results()
        elif self.currentId() == 3:
            self.interim_results_page_1.calculate_interim_results()
        if self.currentId() == 2:
            self.change_pages_num()

        if self.currentId() == self.pageIds()[-1]:
            self.page5.calculate_results(self.page4)
            self.setOption(self.HaveCustomButton1, True)
        elif self.currentId() != 1:
            if self.currentId() >= 5:
                self.page4[self.currentId() - 6].change_fields_num()
            elif self.currentId() != 5 and self.currentId() != 3:
                self.page(self.currentId()).change_fields_num()

    def change_pages_num(self):
        """Calculate and change number of cross pages"""
        self.removePage(self.result_page)
        if len(self.page4) < len(Page1.constituents):
            for i in range(len(Page1.constituents) - len(self.page4)):
                self.page4.append(Page4(len(self.page4)))
                self.addPage(self.page4[-1])
                self.page4[-1].set_title(4 + i)
        # ToDo: не удаляю лишние страницы при уменьшении числа
        self.result_page = self.addPage(self.page5)

    def save_data(self):
        self.page5.save_data()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Wizard()
    mainWin.show()
    sys.exit(app.exec_())

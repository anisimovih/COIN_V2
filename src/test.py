import sys
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from src.main import Wizard
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import qApp

app = QtWidgets.QApplication(sys.argv)


class WizardTest(unittest.TestCase):
    """Test the margarita mixer GUI"""

    def setUp(self) -> None:
        """setUp the GUI"""
        self.app = QtWidgets.QApplication(sys.argv)
        self.form = Wizard()
        self.form.show()
        print("start")

    def tearDown(self) -> None:
        """Close the GUI and clear all data"""
        self.form.close()
        self.app = None
        qApp.quit()
        qApp.exit()

    def test_1_correct_data(self) -> None:
        """Test the GUI in its default state"""
        # Go to 1 step
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)
        print("id: ", self.form.currentId())

        self.form.page1.spin_box.setValue(4)
        for i in range(4):
            self.form.page1.constituents[i].setText("test_" + str(i))
        # Try to go to 2 step
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        # Test_wrong_data_enter
        self.assertEqual(len(self.form.page2.constituents), 0)

        for i in range(4):
            self.form.page1.Ai_num[i].setText("1")
        # Go to 2 step
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        # Test_wrong_data_enter
        self.assertEqual(len(self.form.page3.constituents), 0)

        for i in range(4):
            self.form.page2.Ai[i].setText("1")

        # Go to InterimResultsPage_1
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        # Test final results
        self.assertEqual(self.form.interim_results_page_1.j, [1, 1, 1, 1])

        # Go to 3 step
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        for i in range(4):
            self.form.page3.nii[i].setText("0," + str(i + 1))

        # Go to InterimResultsPage
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        # Test final results
        self.assertEqual(self.form.interim_results_page.h, [10, 5, 3, 2])

        # Go to CrossPages_1
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        self.form.page4[0].dnij[0].setText("0,1")
        self.form.page4[0].dnij[1].setText("0,2")
        self.form.page4[0].dnij[2].setText("0,1")

        # Go to CrossPages_2
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        self.form.page4[1].dnij[0].setText("0,1")
        self.form.page4[1].dnij[1].setText("0,2")
        self.form.page4[1].dnij[2].setText("0,2")

        # Go to CrossPages_3
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        self.form.page4[2].dnij[0].setText("0,2")
        self.form.page4[2].dnij[1].setText("0,2")
        self.form.page4[2].dnij[2].setText("0,3")

        # Go to CrossPages_4
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        self.form.page4[3].dnij[0].setText("0,3")
        self.form.page4[3].dnij[1].setText("0,2")
        self.form.page4[3].dnij[2].setText("0,1")

        # Go to FinalPage
        QTest.mouseClick(self.form.button(1), Qt.LeftButton)

        # Test final results
        self.assertEqual(self.form.page5.hvz, [35, 25, 16, 20])


if __name__ == "__main__":
    unittest.main()

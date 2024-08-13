
from qtpy import QtWidgets
import sys
from qt_interface.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def beenden(self):
        print("ende")
        pass

    def _add(self):

        self.ui.lineEdit_add_firstname.text()
        self.ui.lineEdit_add_secondname.text()
        self.ui.lineEdit_add_number.text()
        self.ui.lineEdit_add_note.text()

def main():
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


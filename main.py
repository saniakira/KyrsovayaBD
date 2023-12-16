from PyQt5 import QtWidgets
from icecream import ic

from modules.old.app import App

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

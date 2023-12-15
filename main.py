from PyQt5 import QtWidgets

from modules.app import App

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

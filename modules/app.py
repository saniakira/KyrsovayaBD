from old.main_window_old import Ui_MainWindow
class App(Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        super().setupUi()
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 578)
        MainWindow.setMaximumSize(QtCore.QSize(99999, 99999))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".button {\n"
"  font-family: \'Helvetica\', Arial, sans-serif;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  text-transform: uppercase;\n"
"  letter-spacing: 1px;\n"
"  padding: 10px 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  cursor: pointer;\n"
"  border: 2px solid #3498db;\n"
"  border-radius: 5px;\n"
"  color: #ffffff;\n"
"  background-color: #3498db;\n"
"  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"\n"
".button:hover {\n"
"  background-color: #ffffff;\n"
"  color: #3498db;\n"
"  border-color: #3498db;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 581))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.layoutWidget = QtWidgets.QWidget(self.Login)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 330, 1001, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.LoginLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setObjectName("LoginLabel")
        self.horizontalLayout_15.addWidget(self.LoginLabel)
        self.LoginEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LoginEdit.setFont(font)
        self.LoginEdit.setObjectName("LoginEdit")
        self.horizontalLayout_15.addWidget(self.LoginEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.PasswordLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.horizontalLayout_16.addWidget(self.PasswordLabel)
        self.PasswordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PasswordEdit.setFont(font)
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.horizontalLayout_16.addWidget(self.PasswordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.LoginButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet(".button {\n"
"  display: inline-block;\n"
"  padding: 10px 20px;\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  cursor: pointer;\n"
"  border: 2px solid #3498db;\n"
"  border-radius: 5px;\n"
"  color: #ffffff;\n"
"  background-color: #3498db;\n"
"  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"\n"
".button:hover {\n"
"  background-color: #ffffff;\n"
"  color: #3498db;\n"
"  border-color: #3498db;\n"
"}\n"
"")
        self.LoginButton.setObjectName("LoginButton")
        self.verticalLayout.addWidget(self.LoginButton)
        self.tabWidget.addTab(self.Login, "")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.layoutWidget1 = QtWidgets.QWidget(self.Add)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.listWidgetLocations = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidgetLocations.setObjectName("listWidgetLocations")
        self.verticalLayout_12.addWidget(self.listWidgetLocations)
        self.horizontalLayout_17.addLayout(self.verticalLayout_12)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16)
        self.listWidgetReleases = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidgetReleases.setObjectName("listWidgetReleases")
        self.verticalLayout_16.addWidget(self.listWidgetReleases)
        self.horizontalLayout_17.addLayout(self.verticalLayout_16)
        self.verticalLayout_13.addLayout(self.horizontalLayout_17)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LastNameLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.LastNameLabel.setFont(font)
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.horizontalLayout.addWidget(self.LastNameLabel)
        self.LastNamelineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LastNamelineEdit.setFont(font)
        self.LastNamelineEdit.setObjectName("LastNamelineEdit")
        self.horizontalLayout.addWidget(self.LastNamelineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FirstNameLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.FirstNameLabel.setFont(font)
        self.FirstNameLabel.setObjectName("FirstNameLabel")
        self.horizontalLayout_2.addWidget(self.FirstNameLabel)
        self.FirstNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FirstNameLineEdit.setFont(font)
        self.FirstNameLineEdit.setObjectName("FirstNameLineEdit")
        self.horizontalLayout_2.addWidget(self.FirstNameLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SectionLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.SectionLabel.setFont(font)
        self.SectionLabel.setObjectName("SectionLabel")
        self.horizontalLayout_3.addWidget(self.SectionLabel)
        self.SectionLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SectionLineEdit.setFont(font)
        self.SectionLineEdit.setObjectName("SectionLineEdit")
        self.horizontalLayout_3.addWidget(self.SectionLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_6.addWidget(self.label_17)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.dateEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_13.addLayout(self.verticalLayout_2)
        self.AddReceiptButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.AddReceiptButton.setFont(font)
        self.AddReceiptButton.setObjectName("AddReceiptButton")
        self.verticalLayout_13.addWidget(self.AddReceiptButton)
        self.tabWidget.addTab(self.Add, "")
        self.viewresults = QtWidgets.QWidget()
        self.viewresults.setObjectName("viewresults")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.viewresults)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 1031, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 1011, 321))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.viewLocationsForRequest = QtWidgets.QListWidget(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.viewLocationsForRequest.setFont(font)
        self.viewLocationsForRequest.setObjectName("viewLocationsForRequest")
        self.verticalLayout_15.addWidget(self.viewLocationsForRequest)
        self.radioButtonFioPostman = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.radioButtonFioPostman.setFont(font)
        self.radioButtonFioPostman.setObjectName("radioButtonFioPostman")
        self.verticalLayout_15.addWidget(self.radioButtonFioPostman)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 1021, 341))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.listWidgetFioSubscriber = QtWidgets.QListWidget(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.listWidgetFioSubscriber.setFont(font)
        self.listWidgetFioSubscriber.setObjectName("listWidgetFioSubscriber")
        self.verticalLayout_18.addWidget(self.listWidgetFioSubscriber)
        self.radioButtonMagazines = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.radioButtonMagazines.setFont(font)
        self.radioButtonMagazines.setObjectName("radioButtonMagazines")
        self.verticalLayout_18.addWidget(self.radioButtonMagazines)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.radioButtonCountPostman = QtWidgets.QRadioButton(self.tab_5)
        self.radioButtonCountPostman.setGeometry(QtCore.QRect(0, 310, 651, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.radioButtonCountPostman.setFont(font)
        self.radioButtonCountPostman.setObjectName("radioButtonCountPostman")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.radioButtonMax = QtWidgets.QRadioButton(self.tab_6)
        self.radioButtonMax.setGeometry(QtCore.QRect(0, 310, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.radioButtonMax.setFont(font)
        self.radioButtonMax.setObjectName("radioButtonMax")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.radioButtonAverage = QtWidgets.QRadioButton(self.tab_7)
        self.radioButtonAverage.setGeometry(QtCore.QRect(0, 310, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.radioButtonAverage.setFont(font)
        self.radioButtonAverage.setObjectName("radioButtonAverage")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.layoutWidget4 = QtWidgets.QWidget(self.viewresults)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 370, 1031, 181))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.labelResultForRequest = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.labelResultForRequest.setFont(font)
        self.labelResultForRequest.setText("")
        self.labelResultForRequest.setObjectName("labelResultForRequest")
        self.verticalLayout_3.addWidget(self.labelResultForRequest)
        self.verticalLayout_14.addLayout(self.verticalLayout_3)
        self.pushButtonForRequest = QtWidgets.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonForRequest.setFont(font)
        self.pushButtonForRequest.setObjectName("pushButtonForRequest")
        self.verticalLayout_14.addWidget(self.pushButtonForRequest)
        self.tabWidget.addTab(self.viewresults, "")
        self.Subscribers = QtWidgets.QWidget()
        self.Subscribers.setObjectName("Subscribers")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Subscribers)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageReceipts = QtWidgets.QWidget()
        self.pageReceipts.setObjectName("pageReceipts")
        self.layoutWidget5 = QtWidgets.QWidget(self.pageReceipts)
        self.layoutWidget5.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButtonTabPostmen_3 = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabPostmen_3.setFont(font)
        self.pushButtonTabPostmen_3.setObjectName("pushButtonTabPostmen_3")
        self.horizontalLayout_12.addWidget(self.pushButtonTabPostmen_3)
        self.pushButtonTabSubscribers_3 = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabSubscribers_3.setFont(font)
        self.pushButtonTabSubscribers_3.setObjectName("pushButtonTabSubscribers_3")
        self.horizontalLayout_12.addWidget(self.pushButtonTabSubscribers_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.listWidgetTabReceipts = QtWidgets.QListWidget(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidgetTabReceipts.setFont(font)
        self.listWidgetTabReceipts.setObjectName("listWidgetTabReceipts")
        self.verticalLayout_5.addWidget(self.listWidgetTabReceipts)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.pageReceipts)
        self.pageSubscribers = QtWidgets.QWidget()
        self.pageSubscribers.setObjectName("pageSubscribers")
        self.layoutWidget6 = QtWidgets.QWidget(self.pageSubscribers)
        self.layoutWidget6.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButtonTabReceipts_2 = QtWidgets.QPushButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabReceipts_2.setFont(font)
        self.pushButtonTabReceipts_2.setObjectName("pushButtonTabReceipts_2")
        self.horizontalLayout_13.addWidget(self.pushButtonTabReceipts_2)
        self.pushButtonTabReleases_2 = QtWidgets.QPushButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabReleases_2.setFont(font)
        self.pushButtonTabReleases_2.setObjectName("pushButtonTabReleases_2")
        self.horizontalLayout_13.addWidget(self.pushButtonTabReleases_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.Subscribers_view = QtWidgets.QListWidget(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Subscribers_view.setFont(font)
        self.Subscribers_view.setObjectName("Subscribers_view")
        self.verticalLayout_4.addWidget(self.Subscribers_view)
        self.verticalLayout_10.addLayout(self.verticalLayout_4)
        self.stackedWidget.addWidget(self.pageSubscribers)
        self.pageReleases = QtWidgets.QWidget()
        self.pageReleases.setObjectName("pageReleases")
        self.layoutWidget7 = QtWidgets.QWidget(self.pageReleases)
        self.layoutWidget7.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButtonTabSubscribers = QtWidgets.QPushButton(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabSubscribers.setFont(font)
        self.pushButtonTabSubscribers.setObjectName("pushButtonTabSubscribers")
        self.horizontalLayout_14.addWidget(self.pushButtonTabSubscribers)
        self.pushButtonTabPostmen = QtWidgets.QPushButton(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabPostmen.setFont(font)
        self.pushButtonTabPostmen.setObjectName("pushButtonTabPostmen")
        self.horizontalLayout_14.addWidget(self.pushButtonTabPostmen)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.listWidgetTabReleases = QtWidgets.QListWidget(self.layoutWidget7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.listWidgetTabReleases.setFont(font)
        self.listWidgetTabReleases.setObjectName("listWidgetTabReleases")
        self.verticalLayout_6.addWidget(self.listWidgetTabReleases)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.pageReleases)
        self.pagePostmen = QtWidgets.QWidget()
        self.pagePostmen.setObjectName("pagePostmen")
        self.layoutWidget8 = QtWidgets.QWidget(self.pagePostmen)
        self.layoutWidget8.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButtonTabReleases = QtWidgets.QPushButton(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonTabReleases.setFont(font)
        self.pushButtonTabReleases.setObjectName("pushButtonTabReleases")
        self.horizontalLayout_11.addWidget(self.pushButtonTabReleases)
        self.pushButtonTabReceipts = QtWidgets.QPushButton(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.pushButtonTabReceipts.setFont(font)
        self.pushButtonTabReceipts.setObjectName("pushButtonTabReceipts")
        self.horizontalLayout_11.addWidget(self.pushButtonTabReceipts)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.listWidget_TabPostmen = QtWidgets.QListWidget(self.layoutWidget8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.listWidget_TabPostmen.setFont(font)
        self.listWidget_TabPostmen.setObjectName("listWidget_TabPostmen")
        self.verticalLayout_7.addWidget(self.listWidget_TabPostmen)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.pagePostmen)
        self.tabWidget.addTab(self.Subscribers, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget9 = QtWidgets.QWidget(self.tab)
        self.layoutWidget9.setGeometry(QtCore.QRect(0, 0, 1031, 551))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.lineEditReleaseIndex = QtWidgets.QLineEdit(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditReleaseIndex.setFont(font)
        self.lineEditReleaseIndex.setObjectName("lineEditReleaseIndex")
        self.horizontalLayout_7.addWidget(self.lineEditReleaseIndex)
        self.verticalLayout_17.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.lineEditReleaseName = QtWidgets.QLineEdit(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditReleaseName.setFont(font)
        self.lineEditReleaseName.setObjectName("lineEditReleaseName")
        self.horizontalLayout_8.addWidget(self.lineEditReleaseName)
        self.verticalLayout_17.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.lineEditReleasePrice = QtWidgets.QLineEdit(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        self.lineEditReleasePrice.setFont(font)
        self.lineEditReleasePrice.setObjectName("lineEditReleasePrice")
        self.horizontalLayout_9.addWidget(self.lineEditReleasePrice)
        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.lineEditReleaseCount = QtWidgets.QLineEdit(self.layoutWidget9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        self.lineEditReleaseCount.setFont(font)
        self.lineEditReleaseCount.setObjectName("lineEditReleaseCount")
        self.horizontalLayout_10.addWidget(self.lineEditReleaseCount)
        self.verticalLayout_17.addLayout(self.horizontalLayout_10)
        self.pushButtonAddRelease = QtWidgets.QPushButton(self.layoutWidget9)
        self.pushButtonAddRelease.setEnabled(True)
        self.pushButtonAddRelease.setMaximumSize(QtCore.QSize(1029, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.pushButtonAddRelease.setFont(font)
        self.pushButtonAddRelease.setObjectName("pushButtonAddRelease")
        self.verticalLayout_17.addWidget(self.pushButtonAddRelease)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget10 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget10.setGeometry(QtCore.QRect(10, 10, 1011, 541))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.listWidgetReport = QtWidgets.QListWidget(self.layoutWidget10)
        self.listWidgetReport.setObjectName("listWidgetReport")
        self.verticalLayout_19.addWidget(self.listWidgetReport)
        self.pushButtonReport = QtWidgets.QPushButton(self.layoutWidget10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReport.setFont(font)
        self.pushButtonReport.setObjectName("pushButtonReport")
        self.verticalLayout_19.addWidget(self.pushButtonReport)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(4)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB_App"))
        self.label_5.setText(_translate("MainWindow", "Авторизация"))
        self.LoginLabel.setText(_translate("MainWindow", "Логин"))
        self.LoginEdit.setText(_translate("MainWindow", "login"))
        self.PasswordLabel.setText(_translate("MainWindow", "Пароль"))
        self.PasswordEdit.setText(_translate("MainWindow", "123456"))
        self.LoginButton.setText(_translate("MainWindow", "Залогиниться"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Login), _translate("MainWindow", "Подключение"))
        self.label_6.setText(_translate("MainWindow", "Выбор участков"))
        self.label_16.setText(_translate("MainWindow", "Выбор доступных изданий"))
        self.label_13.setText(_translate("MainWindow", "Заполнение данных о подписчике"))
        self.LastNameLabel.setText(_translate("MainWindow", "Фамилия"))
        self.FirstNameLabel.setText(_translate("MainWindow", "Имя"))
        self.SectionLabel.setText(_translate("MainWindow", "Отчество"))
        self.label_14.setText(_translate("MainWindow", "Адрес"))
        self.label_17.setText(_translate("MainWindow", "Время подписки(месяцы)"))
        self.label_15.setText(_translate("MainWindow", "Дата начала подписки"))
        self.AddReceiptButton.setText(_translate("MainWindow", "Добавить запись"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add), _translate("MainWindow", "Заполнить квитанцию"))
        self.radioButtonFioPostman.setText(_translate("MainWindow", "Выбери для получения результата"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Фамилия почтальона"))
        self.radioButtonMagazines.setText(_translate("MainWindow", "Выбери для получения результата"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Газеты"))
        self.radioButtonCountPostman.setText(_translate("MainWindow", "Выбери для получения результата"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Сколько почтальонов работает"))
        self.radioButtonMax.setText(_translate("MainWindow", "Выбери для получения результата"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Количество экземпляров изданий максимально "))
        self.radioButtonAverage.setText(_translate("MainWindow", "Выбери для получения результата"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Средний срок подписки"))
        self.label_7.setText(_translate("MainWindow", "Результат:"))
        self.pushButtonForRequest.setText(_translate("MainWindow", "Найти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewresults), _translate("MainWindow", "Получить информацию"))
        self.pushButtonTabPostmen_3.setText(_translate("MainWindow", "Почтальоны"))
        self.pushButtonTabSubscribers_3.setText(_translate("MainWindow", "Подписчики"))
        self.label_2.setText(_translate("MainWindow", "Квитанции"))
        self.pushButtonTabReceipts_2.setText(_translate("MainWindow", "Квитанции"))
        self.pushButtonTabReleases_2.setText(_translate("MainWindow", "Издания"))
        self.label.setText(_translate("MainWindow", "Подписчики"))
        self.pushButtonTabSubscribers.setText(_translate("MainWindow", "Подписчики"))
        self.pushButtonTabPostmen.setText(_translate("MainWindow", "Почтальоны"))
        self.label_3.setText(_translate("MainWindow", "Издания"))
        self.pushButtonTabReleases.setText(_translate("MainWindow", "Издания"))
        self.pushButtonTabReceipts.setText(_translate("MainWindow", "Квитанции"))
        self.label_4.setText(_translate("MainWindow", "Почтальоны"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Subscribers), _translate("MainWindow", "Списки"))
        self.label_18.setText(_translate("MainWindow", "Индекс"))
        self.label_19.setText(_translate("MainWindow", "Название"))
        self.label_20.setText(_translate("MainWindow", "Цена"))
        self.label_21.setText(_translate("MainWindow", "Количество"))
        self.pushButtonAddRelease.setText(_translate("MainWindow", "Добавить издание"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Добавить новое издание"))
        self.pushButtonReport.setText(_translate("MainWindow", "Создать отчет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Отчет"))

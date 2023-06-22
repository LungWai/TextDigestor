from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.select_input_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_input_button.setGeometry(QtCore.QRect(50, 50, 200, 50))
        self.select_input_button.setObjectName("select_input_button")

        self.select_output_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_output_button.setGeometry(QtCore.QRect(550, 50, 200, 50))
        self.select_output_button.setObjectName("select_output_button")

        self.input_file_path = QtWidgets.QLabel(self.centralwidget)
        self.input_file_path.setGeometry(QtCore.QRect(50, 110, 700, 20))
        self.input_file_path.setObjectName("input_file_path")

        self.output_folder_path = QtWidgets.QLabel(self.centralwidget)
        self.output_folder_path.setGeometry(QtCore.QRect(50, 140, 700, 20))
        self.output_folder_path.setObjectName("output_folder_path")

        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(50, 200, 150, 50))
        self.convert_button.setObjectName("convert_button")

        self.summarize_button = QtWidgets.QPushButton(self.centralwidget)
        self.summarize_button.setGeometry(QtCore.QRect(220, 200, 150, 50))
        self.summarize_button.setObjectName("summarize_button")

        self.extract_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_button.setGeometry(QtCore.QRect(390, 200, 150, 50))
        self.extract_button.setObjectName("extract_button")

        self.ticker_button = QtWidgets.QPushButton(self.centralwidget)
        self.ticker_button.setGeometry(QtCore.QRect(560, 200, 150, 50))
        self.ticker_button.setObjectName("ticker_button")

        self.leave_button = QtWidgets.QPushButton(self.centralwidget)
        self.leave_button.setGeometry(QtCore.QRect(50, 500, 700, 50))
        self.leave_button.setObjectName("leave_button")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_input_button.setText(_translate("MainWindow", "Select Input File"))
        self.select_output_button.setText(_translate("MainWindow", "Select Output Folder"))
        self.input_file_path.setText(_translate("MainWindow", "Input File Path:"))
        self.output_folder_path.setText(_translate("MainWindow", "Output Folder Path:"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))
        self.summarize_button.setText(_translate("MainWindow", "Summarize"))
        self.extract_button.setText(_translate("MainWindow", "Extract"))
        self.ticker_button.setText(_translate("MainWindow", "Ticker"))
        self.leave_button.setText(_translate("MainWindow", "Leave"))

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QVBoxLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 960)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("font-size: 15pt; font-family: Times New Roman;")

        self.select_input_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_input_button.setObjectName("select_input_button")

        self.select_output_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_output_button.setObjectName("select_output_button")

        self.input_file_path = QtWidgets.QLabel(self.centralwidget)
        self.input_file_path.setObjectName("input_file_path")

        self.output_folder_path = QtWidgets.QLabel(self.centralwidget)
        self.output_folder_path.setObjectName("output_folder_path")

        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setObjectName("convert_button")

        self.summarize_button = QtWidgets.QPushButton(self.centralwidget)
        self.summarize_button.setObjectName("summarize_button")

        self.extract_button = QtWidgets.QPushButton(self.centralwidget)
        self.extract_button.setObjectName("extract_button")

        self.ticker_button = QtWidgets.QPushButton(self.centralwidget)
        self.ticker_button.setObjectName("ticker_button")

        self.leave_button = QtWidgets.QPushButton(self.centralwidget)
        self.leave_button.setObjectName("leave_button")


        # youtube downloader ui
        self.youtube_url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.youtube_url_input.setObjectName("youtube_url_input")

        self.select_output_folder_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_output_folder_button.setObjectName("select_output_folder_button")

        self.ytoutput_folder_path = QtWidgets.QLabel(self.centralwidget)
        self.ytoutput_folder_path.setObjectName("YT output_folder_path")

        self.download_video_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_video_button.setObjectName("download_video_button")

        self.download_audio_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_audio_button.setObjectName("download_audio_button")

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.addWidget(self.select_input_button)
        self.layout.addWidget(self.select_output_button)
        self.layout.addWidget(self.input_file_path)
        self.layout.addWidget(self.output_folder_path)
        self.layout.addWidget(self.convert_button)
        self.layout.addWidget(self.summarize_button)
        self.layout.addWidget(self.extract_button)
        self.layout.addWidget(self.ticker_button)
        self.layout.addWidget(self.leave_button)
        self.centralwidget.setLayout(self.layout)  # Set the layout on the centralwidget


        self.layout.addWidget(self.youtube_url_input)
        self.layout.addWidget(self.select_output_folder_button)
        self.layout.addWidget(self.ytoutput_folder_path)
        self.layout.addWidget(self.download_video_button)
        self.layout.addWidget(self.download_audio_button)


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

        self.youtube_url_input.setPlaceholderText(_translate("MainWindow", "Enter YouTube URL"))
        self.select_output_folder_button.setText(_translate("MainWindow", "Select Output Folder"))
        self.ytoutput_folder_path.setText(_translate("MainWindow", "YT Output Folder Path:"))
        self.download_video_button.setText(_translate("MainWindow", "Download Video"))
        self.download_audio_button.setText(_translate("MainWindow", "Download Audio"))


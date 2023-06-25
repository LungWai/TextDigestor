import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from ui import Ui_MainWindow
from converter import Converter
from summarizer import Summarizer
from extractor import Extractor
from ticker_finder import TickerFinder
from cleaner import Cleaner
from ytdl import YTDL

class MainApp(Ui_MainWindow):
    def __init__(self, window):
        super().__init__()
        self.setupUi(window)
        self.window = window
        self.input_file_label = window.findChild(QtWidgets.QLabel, "input_file_path")
        self.output_folder_label = window.findChild(QtWidgets.QLabel, "output_folder_path")
        self.output_yt_folder_label = window.findChild(QtWidgets.QLabel, "ytoutput_folder_path")
        self.outfile_path = ""
        self.connect_buttons()

    def connect_buttons(self):
        self.select_input_button.clicked.connect(self.select_input_file)
        self.select_output_button.clicked.connect(self.select_output_folder)
        self.convert_button.clicked.connect(self.convert_file)
        self.summarize_button.clicked.connect(self.summarize_text)
        self.extract_button.clicked.connect(self.extract_focus)
        self.ticker_button.clicked.connect(self.find_ticker)
        self.leave_button.clicked.connect(self.exit_app)

        self.select_output_folder_button.clicked.connect(self.select_output_ytfolder)
        self.download_video_button.clicked.connect(self.download_video)
        self.download_audio_button.clicked.connect(self.download_audio)

    def select_input_file(self):
        # Implement file selection dialog and display selected file path
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self.window, "Select Input File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.input_file_path = file_name
            self.input_file_label.setText(file_name)

    def select_output_folder(self):
        # Implement folder selection dialog and display selected folder path
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self.window, "Select Output Folder", "", options=options)
        if folder_path:
            self.output_folder_path = folder_path
            self.output_folder_label.setText(folder_path)

    def convert_file(self):
        converter = Converter(self.input_file_path, self.output_folder_path)
        converter.convert()
        self.outfile_path = converter.output_file
        self.show_save_dialog(converter.output_file)

    def summarize_text(self):
        print("output file path: ", self.outfile_path)
        cleaner = Cleaner(self.outfile_path)
        cleaned_text = cleaner.clean_text()
        summarizer = Summarizer(self.outfile_path, self.output_folder_path)
        summarizer.summarize()
        self.outfile_path = summarizer.output_file
        self.show_save_dialog(summarizer.output_file)

    def extract_focus(self):
        extractor = Extractor(self.outfile_path, self.output_folder_path)
        extractor.extract()
        self.outfile_path = extractor.output_file
        self.show_save_dialog(extractor.output_file)

    def find_ticker(self):
        ticker_finder = TickerFinder(self.outfile_path)
        ticker_finder.find_ticker()
        self.outfile_path = ticker_finder.output_file
        self.show_save_dialog(ticker_finder.output_file)

    def show_save_dialog(self, file_path):
        # Implement a dialog to show the saved file path
        msg_box = QMessageBox()
        msg_box.setWindowTitle("File Saved")
        msg_box.setText(f"The file has been saved to:\n{file_path}")
        msg_box.exec_()


    def select_output_ytfolder(self):
        # Implement folder selection dialog and display selected folder path
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self.window, "Select YT Output Folder", "", options=options)
        if folder_path:
            self.ytoutput_folder_path = folder_path
            self.output_yt_folder_label.setText(folder_path)

    def download_video(self):
        url = self.youtube_url_input.text()
        output_path = self.ytoutput_folder_path.text()
        downloader = YTDL(url, output_path)
        downloader.download_video()

    def download_audio(self):
        url = self.youtube_url_input.text()
        output_path = self.ytoutput_folder_path.text()
        downloader = YTDL(url, output_path)
        downloader.download_audio()

    def exit_app(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

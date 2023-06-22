import re

class Cleaner:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def clean_text(self):
        with open(self.input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        cleaned_text = self.remove_wrong_encoding(text)

        with open(self.input_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(cleaned_text)

    def remove_wrong_encoding(self, text):
        return re.sub(r'[^\x00-\x7F]+', ' ', text)


import os
from datetime import datetime
from transformers import pipeline

class Summarizer:
    def __init__(self, input_file_path, output_folder_path):
        self.input_file_path = input_file_path
        self.output_folder_path = output_folder_path
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.output_file = os.path.join(self.output_folder_path, f"{self.timestamp}_summary.txt")

    def summarize(self):
        with open(self.input_file_path, "r") as input_file:
            text = input_file.read()

        summarization_pipeline = pipeline("summarization")
        summary = summarization_pipeline(text, max_length=150, min_length=30, do_sample=False)


        # summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        # summary = summarization_pipeline(text, max_length=150, min_length=30, do_sample=False)

        with open(self.output_file, "w") as output:
            output.write(summary[0]['summary_text'])


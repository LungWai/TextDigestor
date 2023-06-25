import os
from datetime import datetime
from transformers import pipeline

class Extractor:
    def __init__(self, input_file_path, output_folder_path):
        self.input_file_path = input_file_path
        self.output_folder_path = output_folder_path
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.output_file = os.path.join(self.output_folder_path, f"{self.timestamp}_extract.txt")

    def extract(self):
        with open(self.input_file_path, "r") as input_file:
            text = input_file.read()

        extraction_pipeline = pipeline("text-classification", model="distilbert-base-uncased", tokenizer="distilbert-base-uncased", num_labels=5)
        extracted_topics = extraction_pipeline(text)

        with open(self.output_file, "w") as output_file:
            for topic in extracted_topics:
                output_file.write(f"{topic['label']}: {topic['score']}\n")

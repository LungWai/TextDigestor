import os
import torch
from datetime import datetime
from transformers import pipeline
from textsum.summarize import Summarizer as SZ

class Summarizer:
    def __init__(self, input_file_path, output_folder_path):
        self.input_file_path = input_file_path
        self.output_folder_path = output_folder_path
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.output_file = os.path.join(self.output_folder_path, f"{self.timestamp}_summary.txt")


    def summarize(self):
        with open(self.input_file_path, "r") as input_file:
            text = input_file.read()
        if len(text) < 1000:
            self.summarize_short(text)
        else:
             self.summarize_long()

    def summarize_short(self, text):
        summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarization_pipeline(text, max_length=130, min_length=30, do_sample=False,
                                            device=0 if torch.cuda.is_available() else -1)

        with open(self.output_file, "w") as output:
            output.write(summary[0]['summary_text'])

    def summarize_long(self): # Pending environment setup
        # summarizer = Summarizer(model_name_or_path='pszemraj/long-t5-tglobal-xl-16384-book-summary')
        summarizer = SZ(model_name_or_path=
                                'D:\\Models\\textSummarizer\\long-t5-tglobal-xl-16384-book-summary',
                                token_batch_length=1024,
                                load_in_8bit=True)
        summarizer.set_inference_params
        summarizer.summarize_file(self.input_file_path, self.output_file)

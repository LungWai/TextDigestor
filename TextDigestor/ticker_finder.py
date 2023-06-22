import os
import json
import re
from transformers import pipeline

class TickerFinder:
    def __init__(self, output_folder_path):
        self.output_folder_path = output_folder_path
        self.input_file = os.path.join(output_folder_path, "output.txt")
        self.output_file = os.path.join(output_folder_path, f"{self.get_timestamp()}_ticker.json")
        self.ticker_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def find_ticker(self):
        with open(self.input_file, "r") as f:
            text = f.read()

        ticker_data = self.ticker_pipeline(text)
        ticker_info = self.extract_ticker_info(ticker_data)

        with open(self.output_file, "w") as f:
            json.dump(ticker_info, f, indent=2)

    def extract_ticker_info(self, ticker_data):
        ticker = ""
        price = {
            "Supply": 0,
            "Demand": 0,
            "Entry": 0,
            "Add": 0,
            "First Target": 0,
            "Second Target": 0,
            "Stop Loss": 0
        }

        for item in ticker_data:
            if item["entity"] == "I-ORG" and item["score"] > 0.5:
                ticker = item["word"].upper()

            if item["entity"] == "I-MISC" and item["score"] > 0.5:
                value = float(re.findall(r'\d+', item["word"])[0])
                key = item["word"].split()[0]

                if key in price:
                    price[key] = value

        return {
            "ticker": ticker,
            "price": price
        }


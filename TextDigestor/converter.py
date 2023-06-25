import os
from datetime import datetime
from pathlib import Path
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import textract

class Converter:
    def __init__(self, input_file_path, output_folder_path):
        self.input_file_path = input_file_path
        self.output_folder_path = output_folder_path
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.output_file = os.path.join(self.output_folder_path, f"{self.timestamp}_output.json")

    def convert(self):
        file_extension = Path(self.input_file_path).suffix.lower()

        if file_extension in ['.pdf', '.epub', '.docx']:
            self.convert_document_to_text()
        elif file_extension in ['.mp4', '.mp3']:
            self.convert_audio_to_text()

    def convert_document_to_text(self):
        text = textract.process(self.input_file_path).decode("utf-8")
        with open(self.output_file, "w", encoding="utf-8") as output:
            output.write(text)

    def convert_audio_to_text(self):
        if Path(self.input_file_path).suffix.lower() == '.mp4':
            video = VideoFileClip(self.input_file_path)
            audio = video.audio
            audio.export("temp_audio.wav", format="wav")
        else:
            audio = AudioSegment.from_mp3(self.input_file_path)
            audio.export("temp_audio.wav", format="wav")

        processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60")
        model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60")

        audio_input = processor("temp_audio.wav", return_tensors="pt", sampling_rate=16000).input_values
        logits = model(audio_input).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.decode(predicted_ids[0])

        with open(self.output_file, "w", encoding="utf-8") as output:
            output.write(transcription)

        os.remove("temp_audio.wav")

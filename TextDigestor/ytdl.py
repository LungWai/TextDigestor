from pytube import YouTube

class YTDL:
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def download_video(self):
        yt = YouTube(self.url)
        stream = yt.streams.get_highest_resolution()
        stream.download(self.output_path)

    def download_audio(self):
        yt = YouTube(self.url)
        stream = yt.streams.get_audio_only()
        stream.download(self.output_path)
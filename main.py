import yt_dlp
import whisper
import os

url = "LINK HERE"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

print("Downloading vk video")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
except Exception as e:
    print(f"Error: {e}")
    exit()

print("Downloading whisper model")
model = whisper.load_model("small")

print("Processing")
result = model.transcribe("audio.mp3", language="ru")

with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Done! check transcription.txt")
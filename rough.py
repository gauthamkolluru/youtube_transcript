import speech_recognition as sr
from pydub import AudioSegment
import os

for f in os.listdir():
    if '.mp4' in f:
        f_name = f.split('.')[0]+".wav"
        # print(f_name)
        abc = AudioSegment.from_file(f).export(f_name, format="wav")
        # abc_wav = AudioSegment.from_mp3("YouTube.mp3").export(f_name, format="wav")
        r = sr.Recognizer()
        with sr.AudioFile(f_name) as source:
            audio = r.record(source)
        print(r.recognize_google(audio, language="en"))
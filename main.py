import os
import sys
from pytube import YouTube
from pydub import AudioSegment
# import speech_recognition as sr


def dld_au(url=''):
    yt = YouTube(url)
    return yt.streams.get_audio_only().download(filename=yt.title)


def a_con(oldFilePath='', newFilePath=''):
    return AudioSegment.from_file(oldFilePath).export(newFilePath, format=newFilePath.split('.')[-1]).close()


def recon(filepath=''):
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
        audio = r.record(source)
    return r.recognize_google(audio)


def main(url='', audio_format='wav'):
    dld_path = dld_au(url)
    nw_dld_path = dld_path.split('.')[0] + '.' + audio_format
    print(nw_dld_path)
    x = a_con(oldFilePath=dld_path, newFilePath=nw_dld_path)
    # return print(recon(nw_dld_path))
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(arg)
            main(url=arg, audio_format='mp3')
    else:
        arg = "https://www.youtube.com/watch?v=CSCnZdSLoA4"
        main(url=arg)

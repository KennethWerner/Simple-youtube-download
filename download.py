from __future__ import unicode_literals
import yt_dlp
import ffmpeg

mp4_opts = {
    'format' : 'bestvideo+bestaudio/best',
    }

finished = False

mp3_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }

urltodownload = input('Url to download : ')
while finished == False:
    formatchooser = input('Choose format \n1. Mp3 \n2. mp4\n : ')
    while formatchooser != '1' and formatchooser != '2':
        formatchooser = input("please enter 1 or 2 : ")
    if formatchooser == '1':
        with yt_dlp.YoutubeDL(mp3_opts) as ydl:
            ydl.download([urltodownload])
            finished = True
    if formatchooser == '2':
        with yt_dlp.YoutubeDL(mp4_opts) as ydl:
            ydl.download([urltodownload])
            finished = True
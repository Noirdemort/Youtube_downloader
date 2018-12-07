import os
import sys
from pytube import YouTube
from pathlib import Path

url = sys.argv[1]
contType = sys.argv[2]
yt = YouTube(url)

try:
    title = yt.title
    red = title.split(' ')
    red = "_".join(red)
    add = '.mp4'
    stream = yt.streams.filter(file_extension='mp4', res='360p').first()
    stream.download('{}/Desktop/'.format(Path.home()), filename=red)
    if contType == 'audio':
        os.system(
            './ffmpeg -i {}/Desktop/{}.mp4  {}/Desktop/{}.mp3'.format(Path.home(), red, Path.home, red))
        os.system('rm {}/Desktop/{}.mp4'.format(Path.home(), red))
        add = '.aac'
    title = "Your file has been downloaded on desktop with name {}{}".format(
        title, add)
except Exception as e:
    title = 'An error occured.'
    title = e
print(title)
sys.stdout.flush()

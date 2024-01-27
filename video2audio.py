import os
from moviepy.editor import *


for i in range(0, 19):
    try:
        video = VideoFileClip(f"./data/prodigy/prodigy_{i}.mp4")
        video.audio.write_audiofile(f"./data/prodigy_mp3/prodigy_{i}.mp3")
    except:
        pass


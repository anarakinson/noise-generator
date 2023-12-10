import os
from moviepy.editor import *


for i in range(0, 19):
    try:
        video = VideoFileClip(f"./data/phonk/phonk_{i}.mp4")
        video.audio.write_audiofile(f"./data/phonk_mp3/phonk_{i}.mp3")
    except:
        pass

"metalcore_mp3"
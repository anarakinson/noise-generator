import os
from moviepy.editor import *


for i in range(1, 19):
    try:
        video = VideoFileClip(f"./data/trancemetal/trance_metal_{i}.mp4")
        video.audio.write_audiofile(f"./data/trancemetal_mp3/trance_metal_{i}.mp3")
    except:
        pass

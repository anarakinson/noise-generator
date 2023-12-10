import os
import sys
import time
import glob
import numpy as np
from pygame import mixer  # Load the popular external library
from mutagen.mp3 import MP3
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-tz", "--timezone", help="", default="Europe/Moscow")
    parser.add_argument("-d", "--datapath", help="", default="./data/trancemetal_mp3/")
    args = parser.parse_args()
    return args


def play_music(music_path):
    # year = time.strftime('%Y')
    # month = time.strftime('%m')
    day = int(time.strftime('%d'))
    hour = int(time.strftime('%H'))
    if os.name == 'nt':
        hour += 3
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))

    random_minute = np.random.randint(10, 30)

    filenames = glob.glob(f"{music_path}/*.mp3")
    n = np.random.randint(len(filenames))
    # print(n)
    filename = filenames[n]


    if (
        (((hour >= 7 and minute >= np.random.randint(15)) or hour >= 8) and hour < 13) or              # 7-13  (7 +- 15)
        (((hour == 14 and minute >= 45 + np.random.randint(3, 12)) or hour >= 15) and hour <= 23) or   # 15-23 (15 +- 12)
        (hour >= 1 and hour < 2 and minute >= random_minute and minute <= random_minute + 9) or        # nighttime
        (hour >= 3 and hour < 4 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 5 and hour < 6 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 6 and hour < 7 and minute >= random_minute and minute <= random_minute + 9)
    ):
        mixer.music.load(filename)
        mixer.music.play()

    audio_lenght = MP3(filename).info.length
    print(audio_lenght / 60)
    time.sleep(audio_lenght + np.random.randint(3, 8) * 60)


def main():
    args = parse_args()

    mixer.init()
    os.environ["TZ"] = args.timezone
    if os.name != 'nt':
        time.tzset()  

    curr = time.time()
    print(time.strftime("%H:%M:%S"))

    while True:
        play_music(args.datapath)



if __name__ == "__main__":
    main()

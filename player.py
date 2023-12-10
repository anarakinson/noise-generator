import os
import sys
import time
import glob
import numpy as np
from pygame import mixer
from mutagen.mp3 import MP3
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-tz", "--timezone", help="timezone in full format like 'Europe/London'", default="Europe/Moscow")
    parser.add_argument("-d", "--datapath", help="path to audiofiles", default="./data/trancemetal_mp3/")
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
        (((hour >= 7 and minute >= np.random.randint(15)) or hour >= 8) and hour < 13) or              # from (7 +- 15) till 13
        (((hour == 14 and minute >= 45 + np.random.randint(5, 14)) or hour >= 15) and hour < 23) or   # from (15 +- 15) till 23
        (hour >= 1 and hour < 2 and minute >= random_minute and minute <= random_minute + 9) or        # from dusk till dawn 
        (hour >= 3 and hour < 4 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 5 and hour < 6 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 6 and hour < 7 and minute >= random_minute and minute <= random_minute + 9)
    ):
        print(os.path.basename(filename), end=" - ")
        mixer.music.load(filename)
        mixer.music.play()

    audio_lenght = MP3(filename).info.length   # get audio lenght
    print(f"{audio_lenght / 60 : .2f} min")
    
    time.sleep(audio_lenght + np.random.randint(7, 13) * 60)  # wait for 10-15 minuts after audio end


def main():
    args = parse_args()

    mixer.init()

    os.environ["TZ"] = args.timezone
    if os.name != 'nt':
        time.tzset()  

    print(time.strftime("%H:%M:%S"))

    while True:
        play_music(args.datapath)



if __name__ == "__main__":
    main()

import os
import sys
import time
import glob
import numpy as np
from pygame import mixer
from mutagen.mp3 import MP3
import argparse


# global variables changed once in few hours
RANDOM_MINUTE = 30
ALLOWED = True


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
        hour += -12
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))

    global RANDOM_MINUTE
    global ALLOWED
    night_delay = 4
    if (hour % 2 == 0 and minute >= 1 and minute < 10):
        RANDOM_MINUTE = np.random.randint(10, 30)   # at start of hour set random minute when schedule starts
        ALLOWED = np.random.uniform() < 0.5        # in thirty percent of cases schedule will work at nighttime

    filenames = glob.glob(f"{music_path}/*.mp3")
    if hour > 19 or hour <= 8:
        filenames = [f for f in filenames if ("cyberpunk4" in f or "phonk" in f)]
    n = np.random.randint(len(filenames))
    # print(n)
    filename = filenames[n]


    if (
        # from 7 till 13
        (((hour >= 7 and minute >= np.random.randint(5, 20)) or hour >= 8) and hour < 13) or 
        # from 15 till 22:30
        (hour == 14 and minute >= 45 + np.random.randint(5, 14)) or 
        (hour >= 15 and hour < 22) or  
        (hour == 22  and minute < 30) or    
        # from dusk till dawn 
        # (hour >= 1 and hour < 2 and minute >= RANDOM_MINUTE and minute < RANDOM_MINUTE + night_delay and ALLOWED) or 
        (hour >= 3 and hour < 4 and minute >= RANDOM_MINUTE and minute < RANDOM_MINUTE + night_delay and ALLOWED) or
        (hour >= 5 and hour < 6 and minute >= RANDOM_MINUTE and minute < RANDOM_MINUTE + night_delay and ALLOWED) 
    ):
        #play track
        print(os.path.basename(filename), end=" - ")
        mixer.music.load(filename)
        mixer.music.play() 

        # set delay after track
        delay_min = np.random.randint(7, 17)
        # get audio lenght
        audio_lenght = MP3(filename).info.length   
        print(f"{hour}:{minute}, {audio_lenght / 60 : .2f} min, delay:", delay_min, RANDOM_MINUTE)


        if (hour >= 23 or hour < 7):
            # play only 5 minutes and stop
            time.sleep((night_delay + 1) * 60)
            mixer.music.stop()
            return
        else:
            # wait for 10-15 minuts after audio end
            time.sleep(audio_lenght + delay_min * 60)  
            return


def main():
    args = parse_args()

    mixer.init()

    os.environ["TZ"] = args.timezone
    if os.name != 'nt':
        time.tzset()  

    print(time.strftime("%H:%M:%S"), int(time.strftime('%H')) + -12)

    while True:
        play_music(args.datapath)



if __name__ == "__main__":
    main()

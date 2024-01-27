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
    parser.add_argument("-d", "--datapath", help="path to audiofiles", default="./data/")
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
    
    filenames = glob.glob(f"{music_path}/*.mp3")
    n = np.random.randint(len(filenames))
    # print(n)
    filename = filenames[n]


    #play track
    print(os.path.basename(filename), end=" - ")
    mixer.music.load(filename)
    mixer.music.play() 

    # set delay after track
    delay_min = np.random.randint(7, 17)
    # get audio lenght
    audio_lenght = MP3(filename).info.length   
    print(f"{hour}:{minute}, {audio_lenght / 60 : .2f} min, delay:", delay_min)


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

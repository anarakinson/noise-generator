# import playsound
import os
import sys
import time
import glob
import numpy as np
from pygame import mixer  # Load the popular external library
import pygame

mixer.init()

os.environ["TZ"] = "Europe/Moscow"

if os.name != 'nt':
    time.tzset()  

curr = time.time()

print(time.strftime("%H:%M:%S"))

def play_music():
    # year = time.strftime('%Y')
    # month = time.strftime('%m')
    day = int(time.strftime('%d'))
    hour = int(time.strftime('%H'))
    if os.name != 'nt':
        hour += 3
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))

    random_minute = np.random.randint(10, 30)

    filenames = glob.glob("./data/trancemetal_mp3/*.mp3")
    n = np.random.randint(len(filenames))
    # print(n)
    filename = filenames[n]


    if (
        (hour >= 7 and hour < 13) or 
        (((hour > 14 and minute >= 45) or (hour > 15)) and hour <= 23) or 
        (hour >= 1 and hour < 2 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 3 and hour < 4 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 5 and hour < 6 and minute >= random_minute and minute <= random_minute + 9) or
        (hour >= 6 and hour < 7 and minute >= random_minute and minute <= random_minute + 9)
    ):
        # playsound.playsound(filename, True)
        mixer.music.load(filename)
        mixer.music.play()

    time.sleep(10 * 60 + np.random.randint(2, 7) * 60)


if __name__ == "__main__":
    while True:
        play_music()


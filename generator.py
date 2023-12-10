import numpy as np
import pygame
import matplotlib.pyplot as plt

sampleRate = 44100
freq = 56

# pygame.mixer.init(44100,-16,2,512)
pygame.mixer.init()


def make_sinus():
    arr = np.array([4096 * np.sin(2.0 * np.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(np.int16)
    arr2 = np.c_[arr,arr]
    return arr2


arr2 = make_sinus()
sound = pygame.sndarray.make_sound(arr2)
sound.play(-1)
pygame.time.delay(1000 * 1000)
sound.stop()

# import pysine
# pysine.sine(frequency=56.0, duration=10.0 * 60) 

import sys
import time
import os
from playsound import playsound

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def scroll(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)

def pause():
  scroll('\nPress enter.')
  pause = input('')

def about():
  cls()
  scroll('Playing informational Audio')
  playsound('FitTheFirst.mp3')
  pause()

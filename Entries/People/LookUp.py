import sqlite3
import sys
import time
import os
book = sqlite3.connect("People.db")
cursor = book.cursor()

def scroll(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    scroll('\nPress enter.')
    pause = input('')

def displayEntries1():
  cls()
# TABLE NAMES
# EntryNumber
# EntryName 
# Enrty
  for row in cursor.execute("SELECT EntryNumber, EntryName FROM People WHERE EntryNumber BETWEEN 0 AND 7"):
    print(row)
  choice = int(input('Select 1-7, or 9 to move to the next page.\n'))
  if choice == 1:
    cls()
    for row in cursor.execute("SELECT Enrty FROM People WHERE EntryNumber BETWEEN 1 AND 1"):
      scroll(str(row))
  #elif choice == 9:
    #displayEntries2()
      #Will need to make when needed lmao
  else:
    scroll('Invalid choice.')
    displayEntries1()
  pause()
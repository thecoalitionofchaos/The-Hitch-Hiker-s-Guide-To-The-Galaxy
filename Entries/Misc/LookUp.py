import sqlite3
import sys
import time
import os
book = sqlite3.connect("Misc.db")
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
  for row in cursor.execute("SELECT EntryNumber, EntryName FROM Misc WHERE EntryNumber BETWEEN 0 AND 7"):
    print(row)
  choice = int(input('Select 1-7, or 9 to move to the next page.\n'))
  if choice == 1:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 1 AND 1"):
      scroll(str(row))
  elif choice == 2:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 2 AND 2"):
      scroll(str(row))
  elif choice == 3:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 3 AND 3"):
      scroll(str(row))
  elif choice == 4:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 4 AND 4"):
      scroll(str(row))
  elif choice == 5:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 5 AND 5"):
      scroll(str(row))
  elif choice == 6:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 6 AND 6"):
      scroll(str(row))
  elif choice == 7:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 7 AND 7"):
      scroll(str(row))
  elif choice == 9:
    displayEntries2()
      #Will need to make when needed lmao
  else:
    scroll('Invalid choice.')
    displayEntries1()
  pause()

def displayEntries2():
  cls()
# TABLE NAMES
# EntryNumber
# EntryName 
# Enrty
  for row in cursor.execute("SELECT EntryNumber, EntryName FROM Misc WHERE EntryNumber BETWEEN 8 AND 14"):
    print(row)
  choice = int(input('Select 1-7, 9 to move to the next page, and 0 to move back.\n'))
  if choice == 1:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 8 AND 8"):
      scroll(str(row))
  elif choice == 2:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 9 AND 9"):
      scroll(str(row))
  elif choice == 3:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 10 AND 10"):
      scroll(str(row))
  elif choice == 4:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 11 AND 11"):
      scroll(str(row))
  elif choice == 5:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 12 AND 12"):
      scroll(str(row))
  elif choice == 6:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 13 AND 13"):
      scroll(str(row))
  elif choice == 7:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 14 AND 14"):
      scroll(str(row))
  elif choice == 0:
    displayEntries1()
  elif choice == 9:
    displayEntries3()
      #Will need to make when needed lmao
  else:
    scroll('Invalid choice.')
    displayEntries2()
  pause()

def displayEntries3():
  cls()
# TABLE NAMES
# EntryNumber
# EntryName 
# Enrty
  for row in cursor.execute("SELECT EntryNumber, EntryName FROM Misc WHERE EntryNumber BETWEEN 15 AND 21"):
    print(row)
  choice = int(input('Select 1-7, or 9 to move to the next page.\n'))
  if choice == 1:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 15 AND 15"):
      scroll(str(row))
  elif choice == 2:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 16 AND 16"):
      scroll(str(row))
  elif choice == 3:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 17 AND 17"):
      scroll(str(row))
  elif choice == 4:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 18 AND 18"):
      scroll(str(row))
  elif choice == 5:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 19 AND 19"):
      scroll(str(row))
  elif choice == 6:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 20 AND 20"):
      scroll(str(row))
  elif choice == 7:
    cls()
    for row in cursor.execute("SELECT Enrty FROM Misc WHERE EntryNumber BETWEEN 21 AND 21"):
      scroll(str(row))
  elif choice == 0:
    displayEntries2()
  #elif choice == 9:
    #displayEntries2()
      #Will need to make when needed lmao
  else:
    scroll('Invalid choice.')
    displayEntries3()
  pause()
import time
import sys
import os
#from Entries.About.About import about
from Entries.Misc.NewEntry import MiscEntry
from Entries.Misc.LookUp import displayEntries1
from Entries.People.LookUp import displayEntries1 as PEentry
from Entries.People.NewEntry import PeopleEntry
from Entries.Places.LookUp import displayEntries1 as PLentry
from Entries.Places.NewEntry import PlacesEntry
from Entries.Planets.LookUp import displayEntries1 as Pentry
from Entries.Planets.NewEntry import PlanetsEntry
from Entries.Species.LookUp import displayEntries1 as Sentry
from Entries.Species.NewEntry import SpeciesEntry

debug = 0


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


  
def mainLoop():
    cls()
    scroll('1. People\n')
    scroll('2. Places\n')
    scroll('3. Planets\n')
    scroll('4. Species\n')
    scroll('5. Misc\n')
    #scroll('6. About the guide\n')
    choice = input('')
    if choice == '1':
        PEentry()
    elif choice == '2':
        PLentry()
    elif choice == '3':
        Pentry()
    elif choice == '4':
        Sentry()
    elif choice == '5':
        displayEntries1()
    #elif choice == '6':
        #about()
    else:
        cls()
        scroll('Invalid Option. Please select 1-6')
        pause()
    mainLoop()



  
def EntryAdd():
    cls()
    scroll('1. People\n')
    scroll('2. Places\n')
    scroll('3. Planets\n')
    scroll('4. Species\n')
    scroll('5. Misc\n')
    choice = input('')
    if choice == '1':
        # Current Entries: 1
        PeopleEntry()
    elif choice == '2':
        # Current Entries: 0
        PlacesEntry()
    elif choice == '3':
        # Current Entries: 1
        PlanetsEntry()
    elif choice == '4':
        # Current Entries: 0
        SpeciesEntry()
    elif choice == '5':
        # Current Entries: 10
        MiscEntry()
    else:
        cls()
        scroll('Invalid Option. Please select 1-6')
        pause()
    EntryAdd()


if debug == 1:
    EntryAdd()
else:
    mainLoop()

import sqlite3
# Current Entries: 0
def PlanetsEntry():
  book = sqlite3.connect('Planets.db')
  cursor = book.cursor()
  myRec = []
  entryNo = input('Input entry number\n')
  while entryNo != "XXX":
    Name = str(input('Input Entry Name\n'))
    Entry = str(input('Input Entry\n'))
    myRec.append(int(entryNo))
    myRec.append(Name)
    myRec.append(Entry)
    cursor.execute("INSERT INTO Planets VALUES (?,?,?)", myRec)
    book.commit()
    myRec = []
    entryNo = input('Input entry number, XXX to end\n')
  book.close()
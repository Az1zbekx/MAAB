import sqlite3


conn = sqlite3.connect('roster.db')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS Roster')
cur.execute('''
    CREATE TABLE Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')


data = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]
cur.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', data)


cur.execute('UPDATE Roster SET Name = ? WHERE Name = ?', ('Ezri Dax', 'Jadzia Dax'))


print("Bajoran characters (Name, Age):")
for row in cur.execute('SELECT Name, Age FROM Roster WHERE Species = ?', ('Bajoran',)):
    print(row)


cur.execute('DELETE FROM Roster WHERE Age > 100')


cur.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')

ranks = {
    'Benjamin Sisko': 'Captain',
    'Ezri Dax': 'Lieutenant',
    'Kira Nerys': 'Major'
}
for name, rank in ranks.items():
    cur.execute('UPDATE Roster SET Rank = ? WHERE Name = ?', (rank, name))


print("\nCharacters sorted by Age (descending):")
for row in cur.execute('SELECT * FROM Roster ORDER BY Age DESC'):
    print(row)


conn.commit()
conn.close()

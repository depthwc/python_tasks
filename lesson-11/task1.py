import sqlite3


conn = sqlite3.connect('roster.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

characters = [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]

cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', characters)


cursor.execute('UPDATE Roster SET Name = ? WHERE Name = ?', ('Ezri Dax', 'Jadzia Dax'))


print("Bajoran Characters:")
cursor.execute('SELECT Name, Age FROM Roster WHERE Species = ?', ('Bajoran',))
for row in cursor.fetchall():
    print(row)


cursor.execute('DELETE FROM Roster WHERE Age > 100')


cursor.execute('ALTER TABLE Roster ADD COLUMN Rank TEXT')


rank_data = {
    'Benjamin Sisko': 'Captain',
    'Ezri Dax': 'Lieutenant',
    'Kira Nerys': 'Major'
}

for name, rank in rank_data.items():
    cursor.execute('UPDATE Roster SET Rank = ? WHERE Name = ?', (rank, name))


print("\nCharacters sorted by Age (descending):")
cursor.execute('SELECT * FROM Roster ORDER BY Age DESC')
for row in cursor.fetchall():
    print(row)


conn.commit()
conn.close()
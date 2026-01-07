import sqlite3


conn = sqlite3.connect('library.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
''')

books = [
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
]
cursor.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', books)

cursor.execute('UPDATE Books SET Year_Published = ? WHERE Title = ?', (1950, '1984'))


print("Dystopian Books:")
cursor.execute('SELECT Title, Author FROM Books WHERE Genre = ?', ('Dystopian',))
for row in cursor.fetchall():
    print(row)


cursor.execute('DELETE FROM Books WHERE Year_Published < 1950')


cursor.execute('ALTER TABLE Books ADD COLUMN Rating REAL')


ratings = {
    'To Kill a Mockingbird': 4.8,
    '1984': 4.7,
    'The Great Gatsby': 4.5
}


for title, rating in ratings.items():
    cursor.execute('UPDATE Books SET Rating = ? WHERE Title = ?', (rating, title))


print("\nBooks sorted by Year Published (ascending):")
cursor.execute('SELECT * FROM Books ORDER BY Year_Published ASC')
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
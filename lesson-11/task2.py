import sqlite3


conn = sqlite3.connect('library.db')
cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS Books')
cur.execute('''
    CREATE TABLE Books (
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
cur.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', books)


cur.execute('UPDATE Books SET Year_Published = ? WHERE Title = ?', (1950, '1984'))


print("Dystopian books (Title, Author):")
for row in cur.execute('SELECT Title, Author FROM Books WHERE Genre = ?', ('Dystopian',)):
    print(row)


cur.execute('DELETE FROM Books WHERE Year_Published < 1950')


cur.execute('ALTER TABLE Books ADD COLUMN Rating REAL')

ratings = {
    'To Kill a Mockingbird': 4.8,
    '1984': 4.7,
    'The Great Gatsby': 4.5
}
for title, rating in ratings.items():
    cur.execute('UPDATE Books SET Rating = ? WHERE Title = ?', (rating, title))


print("\nBooks sorted by Year_Published (ascending):")
for row in cur.execute('SELECT * FROM Books ORDER BY Year_Published ASC'):
    print(row)


conn.commit()
conn.close()

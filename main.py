import sqlite3

conn = sqlite3.connect("bookbuddy.db")

cur = conn.cursor()

# Tabellen Erstellung

book_table = """CREATE TABLE books (
    isbn VARCHAR(17) PRIMARY KEY, 
    title VARCHAR(30), 
    year INT, 
    genre VARCHAR(50), 
    status INT
    )
    """
cur.execute(book_table)


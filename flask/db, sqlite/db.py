import sqlite3


conn = sqlite3.connect("books.sqlite")

cursor = conn.cursor()
sql_query = """ Create TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    lanaguage text NOT NULL,
    title text NOT NULL
)"""
cursor.execute(sql_query)
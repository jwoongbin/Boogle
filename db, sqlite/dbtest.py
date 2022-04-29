import flask
import sqlite3

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS table2 \
    (id integer PRIMARY KEY, name text, birthday text)")

c.execute("INSERT INTO table2(id, name, birthday) \
    VALUES(?,?,?)", \
    (7, 'qwe', '1993-00-00'))

c.execute("Select * from table2")

print(c.fetchall())

print()

c.execute("Select * from table2")
for row in c.fetchall():
    print(row)
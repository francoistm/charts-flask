#!/usr/bin/env python
import sqlite3 as sql
import os

# data base creation/connection
conn = sql.connect("ferme_3_chenes.sqlite")
cursor = conn.cursor()

# lecture de la base de donnée
with open("schema.sql", "r") as file:
    cursor.executescript(file.read())

for file in os.listdir():
    try:
        if file.endswith(".sql") and not file == "schema.sql":
            with open(file, "r") as sql_query:
                sql_string = sql_query.read()
            cursor.executescript(sql_string)
    except Exception as e:
        print(e)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()

conn.close()

# create_db.py

import sqlite3

connection = sqlite3.connect("data/game.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0
)
""")


"""REMEMBER: DOCUMENTS TABLE AND RELATIONS"""

connection.commit()
connection.close()
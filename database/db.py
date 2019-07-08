#!/usr/bin/env python3

"""
 This module has the following purposes:
    1. creates a Sqlite3 database, with the specified;
    2. creates a table in the database;

Example:
    $ cd challenge/
    $ source venv/bin/activate
    $ python3 database/db.py

Exception:
    If Sqlite3 operation error appears.

"""

import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE USERS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         USERNAME       TEXT    NOT NULL,
         DATE_OF_BIRTH  TEXT    NOT NULL);''')
    print("Database successfully created")
except sqlite3.Error as error:
    print(error)

cursor.close()

#!/usr/bin/env python3

import sqlite3
import logging

conn = sqlite3.connect('challenge_db.sqlite')

cursor = conn.cursor()

logging.info("Opened database successfully")

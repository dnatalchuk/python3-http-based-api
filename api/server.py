#!/usr/bin/env python3
"""
  This module has the following purposes:
    1. creates API with the Flask framework used;
    2. GET and POST (only application/json content type)
       methods are supported;
    3. API makes calls to Sqlite3 database for updating
       and fetching data;
    4. endpoint exposed /hello/<username> with dynamic
       lookup value for username in request data;
    5. Implemented logic for updating values in DB if the username exists
       and create a new one - if missing;
    6. Username should be a unique value;
    7. The logic for birthday delta calculation is
       applied and respective messages displayed;

Example:
    $ cd challenge/
    $ source venv/bin/activate
    $ cd api/
    $ ./server.py
"""

import logging
import sys
import flask
from flask import request, jsonify
import sqlite3
import datetime
from datetime import date

root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

app = flask.Flask(__name__)

@app.route('/hello/<username>', methods=['GET'])
def get_user(username):
    user = "{}".format(username)
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    query = cur.execute("SELECT DATE_OF_BIRTH FROM USERS WHERE\
    USERNAME=?", (user,))
    logging.info("Query has been executed")
    dateOfBirth = cur.fetchone()
    if dateOfBirth is None:
        logging.warning(" Not existing username")
        return jsonify("message: User not found, please add new one")
    date_split = dateOfBirth[0].split('-')
    y, m, d = date_split
    today = datetime.date.today()
    year = date.today().year
    birthday = date(int(year), int(m), int(d))
    if today > birthday:
        year += 1
        birthday = date(int(year), int(m), int(d))
        delta = abs((today - birthday).days)
    elif today == birthday:
        return jsonify("message: Hello, {}! Happy birthday".format(username))
    else:
        birthday = date(int(year), int(m), int(d))
        delta = (birthday - today).days

    return jsonify("message: Hello, {}! Your birthday in {} day(s)".format(username, delta))

@app.route('/hello/<username>', methods=['POST'])
def post_data(username):
    req_data = request.get_json()
    dateOfBirth = req_data['dateOfBirth']
    with sqlite3.connect('users.db') as conn:
        user = "{}".format(username)
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        query = cur.execute("SELECT DATE_OF_BIRTH FROM USERS WHERE\
        USERNAME=?", (user,))
        result = query.fetchall()
        if len(result) == 0:
            conn.execute('INSERT INTO USERS (USERNAME,DATE_OF_BIRTH)\
                VALUES (?,?)', (username, dateOfBirth))
            conn.commit()
            return jsonify("Record for {} and date of birth {} successfully\
                ADDED".format(username, dateOfBirth))
        else:
            conn.execute('UPDATE USERS SET DATE_OF_BIRTH=? WHERE \
            USERNAME=?', (dateOfBirth, username))
            conn.commit()
            return jsonify("Record for {} has been UPDATED with date of \
                            birth {}".format(username, dateOfBirth))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

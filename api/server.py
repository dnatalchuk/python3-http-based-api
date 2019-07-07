#!/usr/bin/env python3

import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error
from sqlalchemy import create_engine

app = flask.Flask(__name__)


# @app.route('/hello', methods=['GET'])
# def api_get():
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     query = c.execute('SELECT * FROM Users;')
#     result = query.fetchall()
#     return jsonify(result)


@app.route('/hello/<username>', methods=['GET', 'POST'])
def api_put(username):
    if request.method == 'GET':
        user = "{}".format(username)
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        query = cur.execute("SELECT DATE_OF_BIRTH FROM USERS WHERE USERNAME=?", (user,))
        dateOfBirth = query.fetchall()
        return jsonify("message: Hello, {}! Your birthday at {}".format(username, dateOfBirth))


    if request.method == 'POST':
        req_data = request.get_json()
        dateOfBirth = req_data['dateOfBirth']
        with sqlite3.connect('users.db') as conn:
            user = "{}".format(username)
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            query = cur.execute("SELECT DATE_OF_BIRTH FROM USERS WHERE USERNAME=?", (user,))
            result = query.fetchall()
            if len(result)==0:
                conn.execute('INSERT INTO USERS (USERNAME,DATE_OF_BIRTH) VALUES (?,?)', (username, dateOfBirth))
                conn.commit()
                return jsonify("Record for {} and date of birth {} successfully ADDED".format(username, dateOfBirth))
            else:
                conn.execute('UPDATE USERS SET DATE_OF_BIRTH=? WHERE USERNAME=?', (dateOfBirth, username))
                conn.commit()
                return jsonify("Record for {} has been UPDATED with date of birth {}".format(username, dateOfBirth))


if __name__ == '__main__':
    app.run(debug=True)

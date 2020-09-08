from flask import Flask, jsonify
import backend as backend
import json
import sqlite3
import schedule
import time

app = Flask(__name__)

counter_one = 0
counter_two = 0

def reset():
    global counter_one
    global counter_two
    counter_one = 0
    counter_two = 0

schedule.every(60).minutes.do(reset) 

@app.route("/")
def home():
    return "hello world"

@app.route("/films", methods=['GET'])
def first():
    global counter_one
    conn = sqlite3.connect('starwars.db')
    cur = conn.cursor()
    counter_one += 1
    if counter_one == 1:
        cur.execute('CREATE TABLE IF NOT EXISTS films ( data json)')
        for i in backend.film_names():
            cur.execute('insert into films values ( ?)',[json.dumps(i)])
        conn.commit()
        conn.close()
        return jsonify(backend.film_names())
    else:
        conn = sqlite3.connect('starwars.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM films")
        rows = cur.fetchall()
        return rows

@app.route("/characters", methods=['GET'])
def second():
    global counter_two
    counter_two += 1
    conn = sqlite3.connect('starwars.db')
    cur = conn.cursor()
    if counter_two == 1:
        cur.execute('CREATE TABLE IF NOT EXISTS characters ( data json)')
        for i in backend.join():
            cur.execute('insert into characters values ( ?)',[json.dumps(i)])
        conn.commit()
        conn.close()
        return jsonify(backend.join())
    else:
        conn = sqlite3.connect('starwars.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM characters")
        rows = cur.fetchall()
        return rows

if __name__ == "__main__":
    app.run( debug=True)
    while 1:
        schedule.run_pending()
        time.sleep(1)
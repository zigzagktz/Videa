from flask import Flask, jsonify
import backend as backend
import json
import sqlite3
import schedule
import time

app = Flask(__name__)

counter_one = 0     # to keep counter of films_api
counter_two = 0     # to keep counter of characters_api

def reset():
    """
    in order to reset the counter, this function runs every 1 hour
    once the counters are reset, the cached value will be deleted
    and fresh data will be fetched.
    """
    global counter_one
    global counter_two
    counter_one = 0
    counter_two = 0
schedule.every(60).minutes.do(reset) 

@app.route('/')
def home():
    return jsonify("for films go to -> localhost:8080/films and for characters go to -> localhost:8080/characters")


@app.route("/films", methods=['GET'])
def film_api():
    """ 
This function calls the backend funciton film_names()
and then creates a small database which stores the value in json format
to table films.
    """
    global counter_one
    conn = sqlite3.connect('starwars.db')
    cur = conn.cursor()
    counter_one += 1
    if counter_one == 1:
        cur.execute('drop table if exists films')
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
        dt = []
        for i in rows:
            dt.append(eval(i[0]))
        return jsonify(dt)

@app.route("/characters", methods=['GET'])
def characters_api():
    """
This function calls the backend function join()
and stores the value inside the table called characters
    """
    global counter_two
    counter_two += 1
    conn = sqlite3.connect('starwars.db')
    cur = conn.cursor()
    if counter_two == 1:
        cur.execute('drop table if exists characters')
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
        dt = []
        for i in rows:
            dt.append(eval(i[0]))
        return jsonify(dt)

if __name__ == "__main__":
    app.run( host="0.0.0.0", port = 8080, debug=True)

    while True:
        schedule.run_pending()
        time.sleep(1)
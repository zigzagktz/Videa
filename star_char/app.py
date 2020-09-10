from flask import Flask, jsonify
import backend as backend
import json
import sqlite3
import schedule
import time

app = Flask(__name__)

FlagForFilm_isCache = 0         
FlagForCharacter_isCache = 0    
timeProgramStarts = time.time()   # setting a timer

def reset():
    global FlagForCharacter_isCache
    global FlagForFilm_isCache
    FlagForFilm_isCache = 0
    FlagForCharacter_isCache = 0

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
    global FlagForFilm_isCache
    global timeProgramStarts
    conn = sqlite3.connect('starwars.db')
    cur = conn.cursor()
    if time.time() - timeProgramStarts > 3600:
        timeProgramStarts = time.time()   # setting the current time
        reset()                    # reset flags if 1 hr have passed
    else:
        pass
    if FlagForFilm_isCache == 0:
        FlagForFilm_isCache = 1   # set flag on
        cur.execute('drop table if exists films')
        cur.execute('CREATE TABLE IF NOT EXISTS films ( data json)')
        for i in backend.film_names():
            cur.execute('insert into films values ( ?)',[json.dumps(i)])
        conn.commit()
        conn.close()
        return jsonify(backend.film_names())
    else:
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
    global FlagForCharacter_isCache
    global timeProgramStarts
    conn = sqlite3.connect('starwars.db')
    cur = conn.cursor()
    if time.time() - timeProgramStarts > 3600:
        timeProgramStarts = time.time()   # setting the current time 
        reset()                    # reset flags if 1 hr have passed
    else:
        pass
    if FlagForCharacter_isCache == 0:
        FlagForCharacter_isCache = 1    # set flag on
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
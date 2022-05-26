# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
import sqlite3


def connect_to_db():
    conn = sqlite3.connect('D:/SqlLite/chinook/chinook.db')
    return conn


def get_artists():
    artists = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM artists")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            artist = {"artistId": i["ArtistId"], "name": i["Name"]}
            artists.append(artist)

    except:
        artists = []

    return artists


app = Flask(__name__)


@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_artists())


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app




from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.cypee1r.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/trip", methods=["POST"])
def trip_post():
    name_receive = request.form['name_give']
    place_receive = request.form['place_give']
    comment_receive = request.form['comment_give']
    star_receive=request.form['star_give']
    icon_receive=request.form['icon_give']

    doc = {
        'name':name_receive,
        'place' :place_receive,
        'comment':comment_receive,
        'icon':icon_receive,
        'star':star_receive
    }

    db.trip.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/trip", methods=["GET"])
def trip_get():
    all_trips = list(db.trip.find({},{'_id':False}))
    return jsonify({'result':all_trips})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
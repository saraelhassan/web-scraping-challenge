from flask import flask, render_template,request,redirect,url_for #flask implementation
import pymongo
app = Flask(__name__)
conn ='mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mission_to_mars_db
db.mars.drop()


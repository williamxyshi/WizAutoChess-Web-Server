from flask import Flask
from flask_pymongo import pymongo
from application import application
CONNECTION_STRING = "mongodb+srv://wazord:EaCxw2BHWU4FvC5w@wizautochess-hodzs.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('WizAutoChess')
user_collection = pymongo.collection.Collection(db, 'units')
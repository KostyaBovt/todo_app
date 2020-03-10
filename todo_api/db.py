from pymongo import MongoClient
from flask import g

def get_db():
    if 'db' not in g:
        client = MongoClient('mongodb://user:pass@mongo:27017/todo_db')
        g.db = client.todo_db
    return g.db

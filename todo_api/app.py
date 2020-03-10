from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient
from marshmallow import Schema, fields

from resources.todo_lists import TodoLists
from resources.todo_items import TodoItems

app = Flask(__name__)
api = Api(app)

api.add_resource(TodoLists, '/todolists/', '/todolists/<string:todolist_id>')
api.add_resource(TodoItems, '/todoitems/', '/todoitems/<string:todoitem_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
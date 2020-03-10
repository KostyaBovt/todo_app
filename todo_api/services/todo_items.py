from db import get_db
from flask import  abort
from bson.objectid import ObjectId


def create_todoitem(todoitem):
    todolist_id = todoitem.pop("todolist_id")
    todoitem["_id"] = ObjectId()
    db = get_db()
    db.todolists.update(
        {"_id": ObjectId(todolist_id)},
        {"$push": {"items": todoitem}}
    )
    todolist = db.todolists.find_one(
        {"items._id": todoitem["_id"]},
        {"items": {"$elemMatch": {"_id": todoitem["_id"]}}}
    )
    new_todoitem = todolist["items"][0] 
    return new_todoitem

def update_todoitem(todoitem_id, todoitem):
    db = get_db()
    set_fiels = {f"items.$.{key}": value for key, value in todoitem.items()}
    db.todolists.update({"items._id": ObjectId(todoitem_id)}, {"$set": set_fiels})
    todolist = db.todolists.find_one(
        {"items._id": ObjectId(todoitem_id)},
        {"items": {"$elemMatch": {"_id": ObjectId(todoitem_id)}}}
    )
    updated_todoitem = todolist["items"][0] 
    return updated_todoitem

def delete_todoitem(todoitem_id):
    db = get_db()
    db.todolists.update({}, {"$pull": {"items": {"_id": ObjectId(todoitem_id)} }}, upsert=False, multi=True)

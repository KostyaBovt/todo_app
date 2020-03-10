from db import get_db
from bson.objectid import ObjectId


def get_todolist(todolist_id):
    db = get_db()
    return db.todolists.find_one({"_id": ObjectId(todolist_id)})

def get_all_todolists():
    db = get_db()
    todolists = [todolist for todolist in db.todolists.find()]
    return todolists

def create_todolist(todolist):
    if todolist.get("items", None):
        for item in todolist["items"]:
            item["_id"] = ObjectId()

    db = get_db()
    insert_id = db.todolists.insert_one(todolist).inserted_id
    new_todolist = db.todolists.find_one({"_id": insert_id})
    return new_todolist

def update_todolist(todolist_id, todolist):
    if todolist.get("items", None):
        for item in todolist["items"]:
            item["_id"] = ObjectId()

    db = get_db()
    db.todolists.update_one({'_id': ObjectId(todolist_id)}, {"$set": todolist}, upsert=False)
    updated_todolist = db.todolists.find_one({"_id": ObjectId(todolist_id)}) 
    return updated_todolist

def delete_todolist(todolist_id):
    db = get_db()
    db.todolists.delete_one({'_id': ObjectId(todolist_id)})

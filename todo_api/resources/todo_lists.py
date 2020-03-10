from flask_restful import Resource
from flask import request, abort
from marshmallow import exceptions
from services import todo_lists as todolists_service
from schemas.todo_lists import TodoListSchema, TodoListPostSchema, TodoListPutSchema


class TodoLists(Resource):
    def get(self, todolist_id=None):
        if todolist_id:
            todolist = todolists_service.get_todolist(todolist_id)
            return TodoListSchema().dump(todolist)
        else: 
            todolists = todolists_service.get_all_todolists()
            return TodoListSchema(many=True).dump(todolists)

    def post(self):
        raw_input_data = request.get_json()
        try:
            input_data = TodoListPostSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        new_todolist = todolists_service.create_todolist(input_data)
        return TodoListSchema().dump(new_todolist)

    def put(self, todolist_id):
        raw_input_data = request.get_json()
        try:
            input_data = TodoListPutSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        updated_todolist = todolists_service.update_todolist(todolist_id, input_data)
        return TodoListSchema().dump(updated_todolist)

    def delete(self, todolist_id):
        todolists_service.delete_todolist(todolist_id)
        return {"_id": todolist_id}

from flask_restful import Resource
from flask import request, abort
from marshmallow import exceptions
from services import todo_items as todoitems_service
from schemas.todo_items import TodoItemSchema, TodoItemPostSchema, TodoItemPutSchema


class TodoItems(Resource):
    def post(self):
        raw_input_data = request.get_json()
        try:
            input_data = TodoItemPostSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        new_todoitem = todoitems_service.create_todoitem(input_data)
        return TodoItemSchema().dump(new_todoitem)

    def put(self, todoitem_id):
        raw_input_data = request.get_json()
        try:
            input_data = TodoItemPutSchema().load(raw_input_data)
        except exceptions.ValidationError as e:
            abort(400, str(e))

        updated_todoitem = todoitems_service.update_todoitem(todoitem_id, input_data)
        return TodoItemSchema().dump(updated_todoitem)

    def delete(self, todoitem_id):
        todoitems_service.delete_todoitem(todoitem_id)
        return {"_id": todoitem_id}

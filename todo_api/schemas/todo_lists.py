from marshmallow import Schema, fields
from schemas.todo_items import TodoItemSchema

class TodoListSchema(Schema):
    _id = fields.Str()
    name = fields.Str()
    items = fields.List(fields.Nested(TodoItemSchema))

class TodoListItemsPostSchema(Schema):
    text = fields.Str(required=True)
    due_date = fields.DateTime(required=True)
    finished = fields.Boolean(default=False)

class TodoListPostSchema(Schema):
    name = fields.Str(required=True)
    items = fields.List(fields.Nested(TodoListItemsPostSchema))

class TodoListPutSchema(Schema):
    name = fields.Str(required=False)
    items = fields.List(fields.Nested(TodoListItemsPostSchema))

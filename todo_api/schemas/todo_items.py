from marshmallow import Schema, fields

class TodoItemPostSchema(Schema):
    todolist_id = fields.Str(required=True)
    text = fields.Str(required=True)
    due_date = fields.DateTime(required=True)
    finished = fields.Boolean(default=False)

class TodoItemPutSchema(Schema):
    text = fields.Str(required=False)
    due_date = fields.DateTime(required=False)
    finished = fields.Boolean(required=False)

class TodoItemSchema(Schema):
    _id = fields.Str()
    text = fields.Str()
    due_date = fields.DateTime()
    finished = fields.Boolean()

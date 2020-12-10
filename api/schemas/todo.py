from .. import ml, db
from ..models.todo import Todo
from marshmallow import fields

class TodoSchema(ml):
    
    class Meta(ml.Meta):
        model = Todo
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
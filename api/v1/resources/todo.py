from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from ...models.todo import Todo
from ...schemas.todo import todo_schema, todos_schema

# handle request post
parser = reqparse.RequestParser()
parser.add_argument('title', help = 'This field cannot be blank', required = True)
parser.add_argument('description', help = 'This field cannot be blank', required = True)

class TodoGetdata(Resource):
    """
    get all data from database todo
    """
    def get(self):
        try:
            todo = Todo.query.all()
            return make_response(jsonify(todo=todos_schema.dump(todo)))
        except:
            return {'message': 'Something went wrong'}, 500

class TodoPostData(Resource):
    def post(self):
        data = parser.parse_args()

        try:
            todo = todo_schema.load(data)
            result = todo_schema.dump(todo.create())
            return make_response(jsonify({"todo": result}),200)
        except:
            return {'message': 'Something went wrong'}, 500

class UpdateTodo(Resource):
    def put(self, id):
        data = parser.parse_args()
        get_todo = Todo.updateById(id, data)
        todo = todo_schema.dump(get_todo)
        return make_response(jsonify({"todo-update": todo}))

class DeleteTodo(Resource):
    def delete(self, id):
        return Todo.deleteById(id)
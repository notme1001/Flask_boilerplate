from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from ..models.todo import Todo
from flask_jwt_extended import (jwt_required)

# handle request post
parser = reqparse.RequestParser()
parser.add_argument('title', help = 'This field cannot be blank', required = True)
parser.add_argument('description', help = 'This field cannot be blank', required = True)

class TodoGetdata(Resource):
    def get(self):
        try:
            todo = Todo.getAll()
            return make_response(jsonify(todo=todos_schema.dump(todo)))
        except:
            return {'message': 'Something went wrong'}, 500

class TodoPostData(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()

        try:
            result = Todo.create(data)
            return make_response(jsonify({
                "success": str(result.acknowledged),
                "todo_id": str(result.inserted_id)
            }),200)
        except:
            return {'message': 'Something went wrong'}, 500

class UpdateTodo(Resource):
    def put(self, title):
        data = parser.parse_args()
        cekTodo = Todo.findOne(title)
        if(cekTodo):
            get_todo = Todo.updateById(title, data)
            print(get_todo)
            return make_response(jsonify({"todo-update": 'success'}))
        else:
            return {'message': 'Todo Notfound'}, 400

class DeleteTodo(Resource):
    def delete(self, title):
        try:
            res = Todo.deleteById(title)
            return make_response(jsonify({
                "success": True,
            }),200)
        except:
            return {'message': 'Something went wrong'}, 500
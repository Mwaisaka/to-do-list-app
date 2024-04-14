
from flask import render_template, request, session, jsonify, make_response
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

from config import app, db, api, cors 
from models import Todo

@app.route('/')
def home():
    return "Welcome to my Todo list API"


class Tasks(Resource):
    def get(self):
        tasks = []
        for task in Todo.query.all():
            task_dict = {
                "id": task.id,
                "text": task.text,
                "complete": task.complete
            }
            tasks.append(task_dict)
        return make_response(jsonify(tasks), 200)


class AddTask(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "No data provided"}), 400)
        
        text = data.get('text')
        complete = data.get('complete', False)
        
        new_task = Todo(text=text, complete=complete)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return make_response(jsonify({"message": "Todo item added successfully"}), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"message": f"Failed to Todo item: {str(e)}"}), 500)
        

class DeleteTask(Resource):
    def delete(self, task_id):
        try:
            todo_item = Todo.query.get(task_id)
            if not todo_item:
                return make_response(jsonify({"error": f"Todo item with ID {task_id} not found"}), 404)
            
            db.session.delete(todo_item)
            db.session.commit()
            return make_response(jsonify({"message": f"Todo item with ID {task_id} deleted successfully"}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"message": f"Failed to delete Todo item with ID {task_id}: {str(e)}"}), 500)


api.add_resource(Tasks, "/tasks")
api.add_resource(AddTask, "/add_task")
api.add_resource(DeleteTask, "/delete_task/<int:task_id>")
if __name__ == "__main__":
    app.run(port=5555, debug=True)
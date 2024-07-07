from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

# Todo model


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }


# Create the database tables
with app.app_context():
    db.create_all()

# Get all todos


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

# Get a single todo


@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify(todo.to_dict())
    else:
        return jsonify({'error': 'Todo not found'}), 404

# Create a new todo


@app.route('/todos', methods=['POST'])
def create_todo():
    title = request.json.get('title')
    if title:
        todo = Todo(title=title)
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict()), 201
    else:
        return jsonify({'error': 'Title is required'}), 400

# Update a todo


@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.title = request.json.get('title', todo.title)
        todo.completed = request.json.get('completed', todo.completed)
        db.session.commit()
        return jsonify(todo.to_dict())
    else:
        return jsonify({'error': 'Todo not found'}), 404

# Delete a todo


@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Todo not found'}), 404


if __name__ == '__main__':
    app.run(port=5001)

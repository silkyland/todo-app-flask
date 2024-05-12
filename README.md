# Flask Todo API

This is a simple Flask API for managing a todo list. It allows you to perform CRUD (Create, Read, Update, Delete) operations on todo items.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/flask-todo-api.git
```

2. Change into the project directory:

```
cd flask-todo-api
```

3. Create a virtual environment:

```
python3 -m venv venv
```

4. Activate the virtual environment:

```
source venv/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the Flask development server:

```
python app.py
```

2. The API will be accessible at `http://localhost:5001`.

## API Endpoints

| Endpoint          | HTTP Method | URL Path             | Description                       |
| ----------------- | ----------- | -------------------- | --------------------------------- |
| Get all todos     | GET         | /todos               | Retrieve all todo items           |
| Get a single todo | GET         | /todos/<int:todo_id> | Retrieve a single todo item by ID |
| Create a new todo | POST        | /todos               | Create a new todo item            |
| Update a todo     | PUT         | /todos/<int:todo_id> | Update an existing todo item      |
| Delete a todo     | DELETE      | /todos/<int:todo_id> | Delete a todo item by ID          |

## Request and Response Formats

- Request Body: JSON
- Response Body: JSON

## Example Requests

- Get all todos:

  ```
  GET /todos
  ```

- Get a single todo:

  ```
  GET /todos/1
  ```

- Create a new todo:

  ```
  POST /todos
  Content-Type: application/json

  {
    "title": "New Todo",
    "completed": false
  }
  ```

- Update a todo:

  ```
  PUT /todos/1
  Content-Type: application/json

  {
    "title": "Updated Todo",
    "completed": true
  }
  ```

- Delete a todo:
  ```
  DELETE /todos/1
  ```

## Database

The API uses SQLite as the database backend. The database file is named `todos.db` and will be created automatically when the application is run for the first time.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the README file based on your specific project details and requirements.

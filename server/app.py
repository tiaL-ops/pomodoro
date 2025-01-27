from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)


DATA_FILE = "tasks.json"


def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: {DATA_FILE} not found. Starting with an empty task list.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {DATA_FILE}. Starting with an empty task list.")
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Initialize tasks
todos = load_tasks()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todos)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    new_task = {"Description": task["description"], "Status": "Open"}
    todos.append(new_task)
    save_tasks(todos)
    return jsonify({"message": "Task added successfully"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_done(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["Status"] = "Done"
        save_tasks(todos)
        return jsonify({"message": "Task marked as done"})
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    if 0 <= task_id < len(todos):
        removed_task = todos.pop(task_id)
        save_tasks(todos)
        return jsonify({"message": f"Removed task: {removed_task['Description']}"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

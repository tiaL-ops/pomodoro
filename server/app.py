from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

todos = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todos)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    todos.append({"Description": task["description"], "Status": "Open"})
    return jsonify({"message": "Task added successfully"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_done(task_id):
    if 0 <= task_id < len(todos):
        todos[task_id]["Status"] = "Done"
        return jsonify({"message": "Task marked as done"})
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    if 0 <= task_id < len(todos):
        removed_task = todos.pop(task_id)
        return jsonify({"message": f"Removed task: {removed_task['Description']}"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

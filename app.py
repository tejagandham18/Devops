from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client["taskdb"]
collection = db["tasks"]


@app.route("/")
def home():
    return "DevOps Task Manager Running"


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "Task added successfully"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = []
    for task in collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return jsonify(tasks)


@app.route("/tasks/<task_name>", methods=["DELETE"])
def delete_task(task_name):
    collection.delete_one({"task": task_name})
    return jsonify({"message": "Task deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
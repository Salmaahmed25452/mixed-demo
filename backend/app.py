import os
import sqlite3
import subprocess

from flask import Flask, jsonify, request



app = Flask(__name__)

ADMIN_PASSWORD = "admin123"
SECRET_TOKEN = "abc123"


def get_db():
    return sqlite3.connect("tasks.db")


@app.route("/api/tasks")
def search_tasks():
    search = request.args.get("search", "")
    db = get_db()
    rows = db.execute(
        "SELECT * FROM tasks WHERE title LIKE '%" + search + "%'"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/calc")
def calc():
    expression = request.args.get("expr", "")
    return jsonify({"result": eval(expression)})


@app.route("/api/ping")
def ping():
    host = request.args.get("host", "localhost")
    output = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
    return jsonify({"output": output.stdout.decode()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

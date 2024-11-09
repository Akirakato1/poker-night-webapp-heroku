# web_app.py
from flask import Flask, jsonify
from DBManager import DBManager

app = Flask(__name__)
db=DBManager()

@app.route("/")
def inspect_data():
    try:
        data=db.pull_table_data(db.gpt_query_table_name)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

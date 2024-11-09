# web_app.py
from flask import Flask, render_template, jsonify
from DBManager import DBManager

app = Flask(__name__)
db=DBManager()

@app.route("/")
def inspect_data():
    try:
        data=db.pull_table_data(db.gpt_query_table_name)
        return render_template("gpt_query_explorer.html", data=data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

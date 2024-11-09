# web_app.py
from flask import Flask, render_template, jsonify
from DBManager import DBManager
import re

app = Flask(__name__)
db=DBManager()

@app.route("/")
def inspect_data():
    try:
        data = [process_query(doc) for doc in db.pull_table_data(db.gpt_query_table_name)]
        return render_template("gpt_query_explorer.html", data=data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_query(doc):
    # Extract the player's name after "Query by player:"
    player_match = re.search(r"Query by player:(\w+)", doc['query'])
    player = player_match.group(1) if player_match else "Unknown"

    # Extract the content inside square brackets
    content_match = re.search(r"\[(.*?)\]", doc['query'])
    content = content_match.group(1) if content_match else "No details"

    # Return a processed document with the extracted fields
    return {
        "player": player,
        "content": content,
        "script": doc['script']
    }

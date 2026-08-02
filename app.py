import os
import requests
import psycopg2
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "App2 is running!"})

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return jsonify({"db_status": "connected"})
    except Exception as e:
        return jsonify({"db_status": "error", "details": str(e)}), 500

@app.route("/external")
def external():
    res = requests.get("https://httpbin.org/get")
    return jsonify({"external_status": res.status_code})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

# import numpy as np
# import pandas as pd
import os
import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_timestamp():
    now = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now.isoformat()
    return timestamp, 200, {"Content-Type": "text/plain"}

@app.route("/4")
def get_timestamp2():
    now = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now.isoformat()
    return timestamp, 400, {"Content-Type": "text/plain"}

@app.route("/runprint", methods=["GET"])
def run_print():
    print("Hit endpoint runprint, will try to print errors")
    return "{'status':'running'}", 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    print("Trying to run this app with Flask...")
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
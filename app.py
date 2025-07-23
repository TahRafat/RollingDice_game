from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") 

@app.route("/", methods=["GET", "POST"])
def index():
    if 'rolls' not in session:
        session['rolls'] = []
        session['score'] = 0

    if request.method == "POST":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        session['rolls'].append((die1, die2))


        session['score'] += die1 + die2

        return redirect(url_for("index"))

    return render_template("index.html", rolls=session['rolls'], score=session['score'])

@app.route("/reset")
def reset():
    session.pop('rolls', None)
    session.pop('score', None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

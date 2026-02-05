from flask import Flask, render_template, request
from password_checker import PasswordChecker
import sqlite3

app = Flask(__name__)

def save_to_db(password, rating):
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("INSERT INTO history (password, rating) VALUES (?, ?)", (password, rating))
    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT password, rating FROM history")
    data = c.fetchall()
    conn.close()
    return data
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/check", methods=["POST"])
def check():
    password = request.form["password"]
    checker = PasswordChecker(password)
    rating = checker.get_password_rating()
    save_to_db(password, rating)
    return render_template("result.html", password=password, rating=rating)

@app.route("/history")
def history():
    history_data = get_history()
    return render_template("history.html", history=history_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
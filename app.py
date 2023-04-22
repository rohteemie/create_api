from flask import Flask
from flask import request, jsonify
from db import db_connection

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>Welcome to Transafe!!!</h1>"


@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        query = """SELECT * FROM users"""
        cursor.execute(query)
        user = [
            dict(id=row[0], name=row[1], age=row[2],
                 gender=row[3], email=row[4])
            for row in cursor.fetchall()
        ]
        if user is not None:
            return jsonify(user)

    if request.method == "POST":
        _name = request.form["name"]
        _age = request.form["age"]
        _gender = request.form["gender"]
        _email = request.form["email"]


        query = f"INSERT INTO users(name, age, gender, email) VALUES ('{_name}', '{_age}', '{_gender}', '{_email}')"
        cursor.execute(query)
        conn.commit()
        return f"{cursor.lastrowid} created successfully!"


if __name__ == "__main__":
    app.run(debug=True)

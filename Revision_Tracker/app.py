from flask import Flask, render_template, request
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", message="Revision Tracker is running")

@app.route("/login", methods=["GET","POST"])
def login():
    print("HIT /login", request.method)
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print(f"Username:{username}")
        print(f"Password:{password}")

        return "Submitted, check term"
    
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?,?)",
            (username, password)
        )
        conn.commit()
        conn.close()

        return "User created :)"
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
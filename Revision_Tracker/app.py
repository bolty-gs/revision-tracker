from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run(debug=True)
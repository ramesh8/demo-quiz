from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

#get questions from api, mongodb,...


if __name__ == "__main__":
    app.run(debug=True)
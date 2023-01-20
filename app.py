from flask import Flask, render_template, request, jsonify

from flask_pymongo import PyMongo

import datetime



app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/practice"

mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=['GET'])
def quiz():
    return render_template("quiz.html")

@app.route("/quiz", methods=['POST'])
def quiz_submit():
    questions = request.json
    
    score = 0
    for question in questions:
        if "attempted" in question:
            attemptedOption = question["options"][question["attemptedAnswer"]]
            if attemptedOption == question["correctAnswer"]:
                score += 1

    userid = 1
    quiz = {
        "score":score,
        "timestamp": datetime.datetime.now(),
        "userid":userid
    }
    mongo.db.quiz.insert_one(quiz)
    mongo.db.questions.insert_many(questions)


    return jsonify({"score":score})

#get questions from api, mongodb,...


if __name__ == "__main__":
    app.run(debug=True)
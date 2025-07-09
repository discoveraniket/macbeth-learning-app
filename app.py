from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample questions
QUESTIONS = [
    {"question": "Who kills Macbeth?", "answer": "Macduff"},
    {"question": "What title is Macbeth given after his victory?", "answer": "Thane of Cawdor"},
    {"question": "Who is Macbeth’s wife?", "answer": "Lady Macbeth"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question", methods=["GET"])
def get_question():
    return jsonify(random.choice(QUESTIONS))

@app.route("/check", methods=["POST"])
def check_answer():
    data = request.get_json()
    question = data.get("question")
    answer = data.get("answer")
    for q in QUESTIONS:
        if q["question"] == question:
            return jsonify({"correct": q["answer"].lower() == answer.lower(), "expected": q["answer"]})
    return jsonify({"correct": False, "expected": "Unknown"})

if __name__ == "__main__":
    app.run(debug=True)
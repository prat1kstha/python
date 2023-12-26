from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests
import json

data_API = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean").text
parse_json = json.loads(data_API)
question_data = parse_json["results"]

question_bank = []

for question in question_data:
    q = Question(question["question"], question["correct_answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
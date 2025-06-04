from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

bank = []

for i in question_data:
    x = Question(i['question'], i['correct_answer'])
    bank.append(x)
    # print(x.text, x.answer)

quiz1 = QuizBrain(bank)

quiz1.nq()

while quiz1.kaq():
    quiz1.nq()
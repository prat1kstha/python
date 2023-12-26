class QuizBrain():
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q{self.question_number + 1}: {current_question.question}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Wrong Answer")

        self.question_number += 1
        print(f"You're score is {self.score}/{self.question_number}.")

    def still_has_question(self):
        return self.question_number < len(self.question_list)
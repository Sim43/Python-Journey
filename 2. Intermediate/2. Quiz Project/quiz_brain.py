class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def next_question(self):
        q = self.question_list[self.question_number].question
        a = self.question_list[self.question_number].answer
        self.question_number += 1
        no = self.question_number
        ans = input(f"Q.{no}: {q}. (True/False)?: ")
        if ans.title() == a:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {a}.")
            print(f"Your current score is {self.score}/{no}.")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {a}.")
            print(f"Your current score is {self.score}/{no}.")
        print("\n")

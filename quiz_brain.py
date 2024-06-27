#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: cheking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def contador(self):
        for i in range(1, 11):
            print(i)

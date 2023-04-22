class Question:
    def __init__(self, answer, question):
        self.answer = answer
        self.question = question

    def get_answer(self):
        return self._answer

    def set_answer(self, answer):
        self._answer = answer

    def get_question(self):
        return self._question

    def set_question(self, question):
        self._question = question
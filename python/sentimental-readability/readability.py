import math
class Word_Count:

    def __init__(self, sent):
        self.sentence = sent
        self.list_words = []
        self.count = 0

    def total_letters(self):
        for i in range(len(self.sentence)):
            if self.sentence[i] == " " or self.sentence[i] in "'!?.,":
                pass
            else:
                self.count += 1
        return self.count

    def total_words(self):
        sentence3 = list(map(str, self.sentence.split(" ")))
        return sentence3

    def total_sent(self):
        self.sentence = self.sentence.replace("!", ".")
        self.sentence = self.sentence.replace("?", ".")
        sentence2 = list(map(str, self.sentence.split(".")))
        return sentence2[0:-1]

    def aver_letters(self):
        return self.count/len(self.total_words())*100

    def aver_sentence(self):
        aver = len(self.total_sent()) / len(self.total_words())*100
        return aver

    def grade(self):
        grade_num = round(0.0588 * self.aver_letters() - 0.296 * self.aver_sentence() - 15.8)
        print(grade_num)
        if grade_num > 0:
            if grade_num > 16:
                return "Grade 16+"
            else:
                return f" Grade: {grade_num}"
        elif grade_num <= 0:
            return "Before Grade 1"

sentence = input("Please type in something: ")
sentence = Word_Count(sentence)
sentence.total_letters()
sentence.total_words()
sentence.total_sent()
sentence.aver_letters()
sentence.aver_sentence()
print(sentence.grade())
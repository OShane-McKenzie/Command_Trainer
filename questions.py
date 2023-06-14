import json
import random
import Levenshtein

def is_approximately_equal(string1, string2, threshold):
    def longest_common_subsequence(string1, string2):
        lengths = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
        for i, char1 in enumerate(string1):
            for j, char2 in enumerate(string2):
                if char1 == char2:
                    lengths[i + 1][j + 1] = lengths[i][j] + 1
                else:
                    lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])
        return lengths[-1][-1]

    lcs_length = longest_common_subsequence(string1, string2)
    similarity = (2.0 * lcs_length) / (len(string1) + len(string2))
    return similarity >= threshold

class Questions:
    def __init__(self):
        self.question_list = []
        self.score = 0.0
        self.progress = ""
        self.isQuizEnd = False
        self.isCorrectAnswer=False
        self.correction = ""
        self.total = ""
    def check_commands(self,string,index=0):
        self.progress = "Answered "+str(index+1)+" question(s) out of "+str(len(self.question_list))
        
        if index < len(self.question_list)-1:
            answer = self.question_list[index]["command"]
        elif index == len(self.question_list)-1:
            self.isQuizEnd = True
            answer = self.question_list[index]["command"]
            
        else:
            answer = -1
            self.isQuizEnd = True

        if str(string).strip()==answer.strip():
            self.score = self.score+1
            self.isCorrectAnswer=True
        elif is_approximately_equal(str(string).strip(),answer.strip(),0.66):
            self.correction = "Previous answer Partially Correct. The correct answer is:\n"+answer+"\n"+self.question_list[index]["description"]
            self.score = self.score+0.5
            self.isCorrectAnswer=False
        else:
            self.isCorrectAnswer=False
            self.correction = "Previous answer was incorrect. The correct answer is:\n"+answer+"\n"+self.question_list[index]["description"]
        
        if self.isQuizEnd == True:
            self.score = (self.score/len(self.question_list))*100
            self.total = "Score: "+str(self.score)+"%"
        

    def load_json_from_file(self,file_path):
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            return json_data

    def getQuestions(self,file):
        data = self.load_json_from_file(file)
        self.question_list = random.sample(data["commands"],len(data["commands"]))
        self.progress = "Answered 0 question(s) out of "+str(len(self.question_list))
        return self.question_list

    def restart(self):
        self.question_list = []
        self.score = 0
        self.progress = ""
        self.isQuizEnd = False
        self.isCorrectAnswer=False
        self.correction = ""
        self.total = ""
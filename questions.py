import json
import random

class Questions:
    def __init__(self):
        self.question_list = []
        self.score = 0
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
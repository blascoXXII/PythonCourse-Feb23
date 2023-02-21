"""
Module where questions' classes are stored
"""

import random

class Question():
    
    def __init__(self, question, correct_option, option2, option3, option4):

        self.question = question
        self.options = [correct_option, option2, option3, option4]
        random.shuffle(self.options)
        self.correct_option = correct_option.lower()
        
    def __str__(self):
        
        return f"{self.question}:\n    - {self.options[0]}\n\
    - {self.options[1]}\n    - {self.options[2]}\n    - {self.options[3]}"
    
    def validate_answer(self, answer):
        
        return answer.lower() == self.correct_option
    


def get_questions_from_file(path):
    """

    Parameters
    ----------
    path : String
       CSV file that contains questions and answers in the format question|correctanswer|answer2|answer3|answer4

    Returns
    -------
    question_list : list of Question
        list of Question instances with the thata in the CSV file

    """
    
    with open(path, "r") as file:
        
        source_questions = file.readlines()
            
        
    
    question_list = []
    
    for q in source_questions[1:]:
    
        split_q = q.split("|")
        
        defined_question = Question(split_q[0],
                                              split_q[1],
                                              split_q[2],
                                              split_q[3],
                                              split_q[4])
        
        question_list.append(defined_question)
        
    return question_list
      
            


if __name__ == "__main__":
    
    q = Question("How much is 1+1", "2","1","3","4")    
    print(q)
    print(q.validate_answer("2"))
    print(q.validate_answer("4"))
    
    

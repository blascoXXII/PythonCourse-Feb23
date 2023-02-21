import requests
import html


def get_questions():
    # Make a GET request to retrieve the questions from the Open Trivia API
    response = requests.get("https://opentdb.com/api.php?amount=50&type=multiple&difficulty=easy")
    
    # Parse the JSON response to extract the questions
    questions = response.json()["results"]
    
    # Each element will be a set of question + answers using ; as sep
    questions_list = ["Question|Correct_answer|Answer2|Answer3|Answer4\n"]
    
    # Iterate through each question and extract the relevant information
    for q in questions:
        # Extract the question text
        question = q["question"]
        
        # Extract the correct answer
        correct_answer = q["correct_answer"]
        
        # Extract the incorrect answers
        incorrect_answers = q["incorrect_answers"]
        
        # Combine the correct and incorrect answers into a single list
        answers = [correct_answer] + incorrect_answers
        
        # Create alist with the question and its answers
        question_list = [question] + answers
        
        unescaped_question = html.unescape("|".join(question_list))
        
        questions_list.append(unescaped_question+"\n")
        
    return questions_list

final_questions = get_questions()

with open(r"C:\Users\Blasco\Desktop\CursPython\Day5\Trivial_Solved\TriviaQuestions.csv", "w") as file:
    file.writelines(final_questions)
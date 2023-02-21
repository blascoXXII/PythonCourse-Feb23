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
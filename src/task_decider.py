def get_preferred_option(task_1, task_2):
    
    dictionary_of_winning_condition = {
        # key is preferred over value(s)
        "wash dishes" : ["cook dinner", "wash clothes"],
        "clean windows" : ["wash dishes", "do ironing"],
        "cook dinner" : ["clean windows", "do ironing"],
        "wash clothes" : ["clean windows", "cook dinner"],
        "do ironing" : ["wash clothes", "wash dishes"]
    }

    if task_1.description in dictionary_of_winning_condition and task_2.description in dictionary_of_winning_condition:
        if task_2.description in dictionary_of_winning_condition[task_1.description]:
            return task_1
        else:
            return task_2
        



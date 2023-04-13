def get_preferred_option(first_task, second_task):
    
    dict_preferences = {
        # the key is the preferred task over the tasks in the value list
        "wash dishes" : ["cook dinner", "wash clothes"],
        "clean windows" : ["wash dishes", "do ironing"],
        "cook dinner" : ["clean windows", "do ironing"],
        "wash clothes" : ["clean windows", "cook dinner"],
        "do ironing" : ["wash clothes", "wash dishes"]
    }

    if first_task.description in dict_preferences and second_task.description in dict_preferences:
        if first_task.description == second_task.description: 
            if first_task.duration < second_task.duration:
                #return the longer task
                return second_task
            else:
                return first_task
        
        if second_task.description in dict_preferences[first_task.description]:
            return first_task
        else:
            return second_task
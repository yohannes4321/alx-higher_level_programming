#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None :
        return None
    else:
        max_v=0
        answer=0
        for key in a_dictionary.keys():
            if a_dictionary[key] > max_v:
                max_v=a_dictionary[key]
                answer=key
        return answer


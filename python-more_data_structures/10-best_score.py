#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    clé = None
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if score < a_dictionary[key]:
            score = a_dictionary[key]
            clé = key
    return clé

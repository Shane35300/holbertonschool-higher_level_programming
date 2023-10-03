#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1:
            if dico[roman_string[i]] < dico[roman_string[i + 1]]:
                result += (dico[roman_string[i + 1]] - dico[roman_string[i]])
                i += 1
            else:
                result += dico[roman_string[i]]
        else:
            result += dico[roman_string[i]]
        i += 1
    return result

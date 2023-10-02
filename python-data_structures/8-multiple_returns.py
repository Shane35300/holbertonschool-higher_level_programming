#!/usr/bin/python3
def multiple_returns(sentence):
    first_car = None
    if len(sentence) > 0:
        first_car = sentence[0]
    return (len(sentence), first_car)

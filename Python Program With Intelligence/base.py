# This is an A.I.
from user_responses import *
from ai_classes import *

USER_INPUT = input(">>> ")


def response(USER_INPUT):
    for n in INPUTS.keys():
        if n in USER_INPUT:
            return INPUTS[n]
        else:
            if n not in USER_INPUT:
                INPUTS[USER_INPUT] = ''
                print(INPUTS)

            return("Can't Understand that yet")
    

print(response(USER_INPUT))



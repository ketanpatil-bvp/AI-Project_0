from user_responses import *
class AddInput(object):
    def __init__(self, USER_INPUT):
        self.USER_INPUT = USER_INPUT
    
    def addInput(self, USER_INPUT):
        INPUTS[USER_INPUT] = ''
    
    def __str__(self):
        return INPUTS
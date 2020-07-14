INPUTS = {"hello":"Hi There, Myself A.I.", "hi":"Hello, I am A.I."}


class AddInput(object):
    def __init__(self, USER_INPUT):
        self.USER_INPUT = USER_INPUT
    
    def addInput(self, USER_INPUT):
        INPUTS[USER_INPUT] = ''
    
    
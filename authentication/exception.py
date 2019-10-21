

class DuplicateEmailError(Exception):

    def __init__(self):
        self.msg = "Email already exist, please try another email"





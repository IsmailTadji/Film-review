import re


def verify_username(username):
    if not re.search("^.*(?=.*[a-zA-Z0-9-_])(?=.{3,12}).*$", username):
        return False
    return True

def verify_password(password):
    if not re.search("^.*(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.{8,})", password):
        return False
    return True
"""user user user"""


class User:
    """user"""

    def __init__(self, first_name, last_name):
        """initialize"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """describe"""
        print("User's name is " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        """Greet"""
        print("Hello, " + self.first_name + "!")

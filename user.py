"""user user user"""


class User:
    """user"""

    def __init__(self, first_name, last_name):
        """initialize"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        """describe"""
        print("User's name is " + self.first_name + " " + self.last_name + ".")

    def greet_user(self):
        """Greet"""
        print("Hello, " + self.first_name + "!")

    def increment_login_attempts(self):
        """self explanatory"""
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        """reset to 0"""
        self.login_attempts = 0


user1 = User("mark", "twain")
user2 = User("john", "lennon")

print("User 1's last name is " + user1.last_name)
user1.describe_user()
user2.greet_user()

user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
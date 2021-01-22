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


class Privileges:
    def __init__(self, privileges=["add post", "delete post", "ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: " + ", ".join(self.privileges))


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin1 = Admin("claire", "cox")
admin1.privileges.show_privileges()
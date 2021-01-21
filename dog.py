"""woof"""


class Dog:
    """woof woof"""

    def __init__(self, name, age):
        """initialise name & age attributes"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """simulate dog sitting"""
        print(self.name + " is now sitting.")

    def roll_over(self):
        """simulate roll over"""
        print(self.name + " is now rolling over!")


my_dog = Dog("precious", 10)

print("My dog's name is " + my_dog.name)
my_dog.sit()
my_dog.roll_over()

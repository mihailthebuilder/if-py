"""a restaurant"""


class Restaurant:
    """restaurant class"""

    def __init__(self, name, cuisine):
        """initialise"""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """describe restaurant"""
        print(
            "Restaurant is called "
            + self.name
            + " and its cuisine is"
            + self.cuisine
            + "."
        )

    def open(self):
        """open restaurant"""
        print("Ladies and gentlemen...")
        print("the famous restaurant called " + self.name + "...")
        print("is.open.for.bizinessss")

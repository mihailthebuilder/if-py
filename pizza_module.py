"""pizza module. yum"""


def make_pizza(size, *toppings):
    """makes a pizza"""
    print("\nMaking " + str(size) + "-inch pizza with following toppings")
    for topping in toppings:
        print("- " + topping)

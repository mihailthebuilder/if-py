"""arbitrary func args"""


def make_pizza(*toppings):
    """say you're making pizza"""
    print("\nMaking pizza with these toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza("pepperoni")
make_pizza("salami", "cheese", "pineapple")

a = 1
b = a
a = 2
print(a)
print(b)

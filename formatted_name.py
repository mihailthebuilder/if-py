"""more functions"""


def get_formatted_name(first_name, last_name):
    """Return full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()


MUSICIAN = get_formatted_name("johnny", "depp")
print(MUSICIAN)

def describe_pet(pet_type, name):
    """Display pet info"""
    print("\nI have a " + pet_type + ".")
    print("My pet's name is " + name.title())


describe_pet("hamster", "gollum")

describe_pet(name="bond", pet_type="dog")

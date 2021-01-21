"""start  if"""

CARS = ["audi", "bmw", "subaru", "toyota"]

for car in CARS:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

BANNED_USERS = ["andrew", "carolina", "david"]
USER = "marie"

if USER not in BANNED_USERS:
    print(USER.title() + ", you can post if you want.")

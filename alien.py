"""dictionary"""

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])

alien_0["position"] = 25
print(alien_0)

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)

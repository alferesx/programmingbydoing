name = input("Whats is your name?: ")
age = int(input("Whats your age?: "))
if age < 16:
    print("You can't drive")
if age < 18:
    print("You can't vote")
if age < 25:
    print("You can't rent a car")
if age >=25:
    print("You can do anything that's legal")

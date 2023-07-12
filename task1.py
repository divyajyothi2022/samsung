number =-45
if (number >= 0):
    print("number is positive")
    if (number == 50):
        print("number is 50")
    elif (number == 0):
        print("number is 0")
    elif (number in range(0, 49)):
        print("number is in between 0 to 50")
    elif (number in range(51, 100)):
        print("number is in between 50 to 100")
else:
    print("number is negative")
    if (number == -50):
        print("number is -50")
    elif (number == 0):
        print("number is 0")
    elif (number in range(-49, 0)):
        print("number is in between 0 to -50")
    elif (number in range(-100, -51)):
        print("number is in between -50 to -100")


math = 6
history = 6
fish = 0


print("Hello and welcome to my quiz to determine if you are better in math or history.")
name = input("Please input your name.")
print(f"Hello {name}! You will now answer the following 6 questions to determine if you are better at math or history!")

answer = input("What is 8*7")
if answer == "56":
    print("Correct!")
    math += 2
elif answer == "fish":
    print("fish")
    fish += 1
else:
    print("Incorrect!")
    math -= 2

answer = input("When did World War I start?")
if answer == "1914":
    print("Correct!")
    history += 2
elif answer == "fish":
    print("fish")
    fish += 1
else:
    print("Incorrect!")
    history -= 2
if fish == 2 and name == "fish":
    answer = input("What is fish?")
    if answer == "fish":
        print("Correct!")
        fish += 2
    else:
        print("Incorrect!")
        history -= 2
        fish -= 1
        math -= 2
answer = input("What is 16 / 2")
if answer == "8":
    print("Correct!")
    math += 2
elif answer == "fish":
    print("fish")
    fish += 1
else:
    print("Incorrect!")
    math -= 2

answer = input("When was the first plane created?")
if answer == "1903" or answer == "12/17/1903":
    print("Correct!")
    history += 2
elif answer == "fish":
    print("fish")
    fish += 1
else:
    print("Incorrect!")
    history -= 2
if fish >= 5:
    answer = input("You have input every possible place as fish... why. Well, last question what is 4 + 4?")
    if answer == "fish":
        print("wow.")
        fish += 5
    elif answer == 8:
        print("Good job! You finally stopped!")
        math += 10
    else:
        print("Incorrect, but you did'nt answer fish...")
        math -= 2
        fish -= 5
elif math >= history:
    answer = input("What is 4 + 4")
    if answer == "8":
        print("Correct!")
        math += 2
    elif answer == "fish":
        print("fish")
        fish += 1
    else:
        print("Incorrect!")
        math -= 2
else:
    answer = input("When did World War I end?")
    if answer == "1918":
        print("Correct!")
        history += 2
    elif answer == "fish":
        print("fish")
        fish += 1
    else:
        print("Incorrect!")
        history -= 2

print("Based on your answers you are a...")
if fish >= 10:
    print("Fish Person? You answered fish to every question? Why?")
elif math > history:
    print("Math person! Good job!")
elif history > math:
    print("History person! Good job!")
else:
    print("Both! You are both a History and Math person! Good job!")
print("The End.")
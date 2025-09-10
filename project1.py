print("Hi! My name is Jim. What is your name?")
name = input("")
print(f"Hi {name} nice to meet you! What school do you go to?")
school = input("")
if school == "SAAS" or "Seattle Academy":
    print("I go to SAAS too!")
else:
    print(f"I don't go to {school}, I go to SAAS!")
print(f"Do you like {school}?")
like = input("")
if like == "yes":
    print("Cool! Me too!")
else:
    print("Ok! I like school!")
print("What was your favorite class today?")
variable4 = input("")
if variable4 == "Instrumental Band" or "Band":
    print("Cool! Me too!")
else: 
    print("Cool! My favorite was Instrumental Band!")
print(f"Well goodbye! I have to go now. It was nice meeting you {name}!")
print("The End.")
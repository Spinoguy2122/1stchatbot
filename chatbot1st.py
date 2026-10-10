print("hello I am an AI Bot, what is your name")

name=input()

print(f"its nice to meet you", {name})

print("How are you feeling today good or bad?")
mood=input().lower()

if mood =="good":
    print("good for you")
elif mood == "bad":
    print("huh oh well")
else:
    print("invalid answer please answer in good or bad form")

print ("have you eaten today yes or no?")
food=input().lower()
if food == "yes":
    print("good for you, I whish I could eat as well but alas I am just a chatbot")
elif food == "no":
    print("then you shall starve")
else:
    print("invalid answer please answer in yes or no form")

print("do you like to play games yes or no?")
games=input().lower()
if games == "yes":
    print("good for you, while this version of myself cannot play games i know of some of my bretheren that can play games with you sadly they dont have mush skill")
elif games == "no":
    print("well that is a shame, you should get a life")
else:
    print("invalid answer please answer in yes or no form")

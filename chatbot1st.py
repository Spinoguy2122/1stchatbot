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


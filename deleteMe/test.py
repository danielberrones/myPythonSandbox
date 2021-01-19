from random import choice

iNeedToStudy = True
userLang = []

while iNeedToStudy:
    userInput = input("What language do you need to study? ")
    if userInput == "" and len(userLang) == 0:
        print("Goodbye, procrastinator!")
        break
    elif userInput == "":
        print(f"You should study {choice(userLang)}. Goodbye.")
        print(f"Languages entered: {userLang}")
        break
    userLang.append(userInput)
    print(f"I like {userInput} too.")


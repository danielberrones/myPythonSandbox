while True:
    print("What's your name?")
    name=input()
    if name !="Daniel":
        print("Try again "+name+"!")
        print()
        continue
    print()
    print()
    print("Okay",name,"tell me your cat's name?")
    cat=input()
    if cat !="Kaya":
        print("WRONG!")
        continue
    elif cat =="Kaya":
        print("You are correct!")
        print("THE END!")
        break
          

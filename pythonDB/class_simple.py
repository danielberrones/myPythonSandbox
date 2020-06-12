############
############ create class and print statement
############
############


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight


    def intro_self(self):
        print("\nMy name is " + self.name + ".")
        print("My color is " + self.color + ".")
        print("My weight is " + str(self.weight) + ".")


r1 = Robot("Tom",'red', 30)
r2 = Robot('Jeff','blue', 500)



r1.intro_self()
r2.intro_self()

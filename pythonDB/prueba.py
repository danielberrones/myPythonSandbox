from random import random


class Raquetball:
    def __init__(self):
        # explains rules
        self.printIntro()

        # collects data from user
        self.probA = int(input("ProbA: "))
        self.probB = int(input("ProbB: "))
        self.nGames = int(input("Number games: "))

        # sets default values
        self.winsA = 0
        self.winsB = 0
        self.scoreA = 0
        self.scoreB = 0

        self.simNGames()
        # self.printSummary()

    def printIntro(self):
        print("\n***************************************************************")
        print("This program simulates racquetball between two players")
        print("Each player's skill (probability) is indicated between 0 and 1")
        print("that the player will win the point when serving")
        print("***************************************************************\n")
        input("\nPress enter to continue ")

    def simNGames(self):
        print("this is a text line written in the simNGames method")
        print(self.probA)
        print(self.probB)
        print(self.nGames)

        for i in range(self.nGames):
            # for each game it tests that game, then returns score for that game
            self.scoreA, self.scoreB = self.simOneGame(self.probA, self.probB)
            print(self.scoreA, 'printing self.scoreA')
            print(self.scoreB, 'printing self.scoreB')
            if self.scoreA > self.scoreB:
                self.winsA = self.winsA + 1
            else:
                self.winsB = self.winsB + 1

        return self.winsA, self.winsB

    def simOneGame(self, ):
        serving = "A"
        while not self.gameOver(self.scoreA, self.scoreB):
            if serving == "A":
                if random() < self.probA:
                    self.scoreA = self.scoreA + 1
                else:
                    serving = "B"
            else:
                print("This is if statement in simOneGame")
                if random() < self.probB:
                    self.scoreB = self.scoreB + 1
                else:
                    serving = "A"
        return self.scoreA, self.scoreB

    def gameOver(self, a, b):
        return self.scoreA == 15 or self.scoreB == 15

    def printSummary(self):
        self.totalGames = self.winsA + self.winsB
        print(f"\nGames simulated: {self.totalGames}")
        print("************************************************")
        print(f"\nWins for A: {self.winsA} ({self.winsA / self.totalGames})")
        print(f"Wins for B: {self.winsB} ({self.winsB / self.totalGames})")


def main():
    Raquetball()


if __name__ == '__main__':
    main()

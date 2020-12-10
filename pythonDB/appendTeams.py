## Creates list of NBA teams and prints data
## Modified by Daniel Alexander Berrones 8/6/2019

class addteamNames:
    def __init__(self):
        self.teams = []
    
    def add_teams(self):
        while True:
            print("Enter NBA team " + str(len(self.teams) + 1) + "\n\tOr hit enter to stop.")
            self.name = input()
            if self.name=='':
                break
            self.teams=self.teams+[self.name]
        for self.name in self.teams:
            print(f"The teams you typed: {self.name}")
        print(f"Length of list: {len(self.teams)}")

def main():
    go = addteamNames()
    go.add_teams()

if __name__ == '__main__':
    main()
    

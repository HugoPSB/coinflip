import random
from datetime import datetime

class textScreens:
    def title(self):
        print("   _____      _         ______ _ _       ")
        print("  / ____|    (_)       |  ____| (_)      ")
        print(" | |     ___  _ _ __   | |__  | |_ _ __  ")
        print(" | |    / _ \| | '_ \  |  __| | | | '_ \ ")
        print(" | |___| (_) | | | | | | |    | | | |_) |")
        print("  \_____\___/|_|_| |_| |_|    |_|_| .__/ ")
        print("                                  | |    ")
        print("                                  |_|    ")

class coinFlip:
    def __init__(self):
        self.input = ""
        self.coin_rand = 0
        self.tails = 0
        self.heads = 0

    def user_input(self):
        self.input = input("Would you like to flip a coin or write results or close? (y/w/c): ")
        self.act_on_input(self.input)

    def act_on_input(self, input):
        if input == "y":
            self.flip()
        elif input == "w":
            self.write_log(self.heads, self.tails)
        else:
            raise KeyError("Good Bye")
    '''
    This makes a random number of 1 or 2
    If number is 1 it is heads
    If number is 2 it is tails
    '''
    def flip(self):
        coin_rand = random.randint(1,2)

        if coin_rand == 1:
            self.heads = self.heads + 1
            print(f"You got Heads. There has been {self.heads} heads and {self.tails} tails so far")
            

        elif coin_rand == 2:
            self.tails = self.tails + 1
            print(f"You got Tails. There has been {self.heads} heads and {self.tails} tails so far")
            
        else:
            print(f"Random number error. Num was {self.coin_rand}")

    def write_log(self, heads, tails):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = datetime.today()

        f = open("results.txt", "a")
        f.write(f"On {date} you got {heads} heads and {tails} tails.\n")
        f.close
import random
from datetime import date
from datetime import datetime

heads = 0
tails = 0


while True:
    #get what user wants to do
    get_input = input("Would you like to flip a coin or write results or close? (y/r/c): ")
    if get_input == "y":
        flip_coin = True
    elif get_input == "r":#write reseults to file
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = date.today()
        f = open("results.txt", "a")
        f.write(f"On {date} at {time} you got {heads} and {tails} tails.\n")
        f.close()
        flip_coin = False
    else:
        print("Good bye") 
        break



    #Gen random numbers and chek if even or odd
    if flip_coin == True:
        coin_num = random.randint(1,2)
        if (coin_num % 2) == 0: #even = heads
            print(f"You got Heads. There has been {heads} heads and {tails} tails so far")
            heads = heads + 1
            flip_coin = False
        else:   #if not odd then tails
            print(f"You got Tails. There has been {heads} heads and {tails} tails so far")
            tails = tails + 1
            flip_coin = False
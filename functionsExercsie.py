Write a rock, paper, scissors game using functions.
play against the computer. 
Keep track of the score for the user + computer + draws.
focus on using functions to make the output nice. 

stretch: explore recussrion for winnign logic. 


import random
class bcolors:
    """ Purely color formats """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Global Variables
choices = ["1. Rock","2. Paper","3. Scissors"]
user_score = 0
ai_score = 0
lines = ("-" * 70)
rounds = 1
draws = 0
count = 1

#Functions
def rock_paper_scissors(ai,user):
    """ Logic to decide winner """
    global user_score, ai_score, draws

    if ai == user:
        print(f"{bcolors.WARNING}Both players selected:{choices[ai-1]} - DRAW!{bcolors.ENDC}\n")
        draws += 1

    elif (user == 1 and ai == 3) or (user == 2 and ai == 1) or (user == 3 and ai == 2):
        print(f"{bcolors.OKGREEN}User WINS! +1 point {bcolors.ENDC}- User:{choices[user-1]}, AI:{choices[ai-1]}\n")
        user_score += 1

    elif (ai == 1 and user == 3) or (ai == 2 and user == 1) or (ai == 3 and user == 2):
        print(f"{bcolors.FAIL}AI WINS! +1 point {bcolors.ENDC}- User:{choices[user-1]}, AI:{choices[ai-1]}\n")
        ai_score += 1

    else:
        print("Logic did not match")

#Main loop
while True:
    print(f"{bcolors.WARNING}{lines}\nAI vs User | Rock, Paper, Scissors! | User Score:{user_score} AI Score:{ai_score} Draws:{draws}\nFirst to 10 wins!{bcolors.ENDC}\n")
    for hand in choices:
        print(f"{hand}")

    while True:
        user_choice = input(f"\nRound:{rounds}\nChoice: ")
        if user_choice not in ["1","2","3","q"]:
            print(f"{bcolors.FAIL}Input must be 1,2,3 or q{bcolors.ENDC}\n")
            continue
        else:
            break

    if user_choice == "q":
        print(f"\n{bcolors.HEADER}Exiting...{bcolors.ENDC}")
        break

    rounds += 1
    ai_choice = random.randint(1, 3)
    rock_paper_scissors(ai_choice,int(user_choice))

    if user_score == 10:
        print(f"{bcolors.OKGREEN}You Won with a score of {user_score}! - GAME OVER{bcolors.ENDC}")
        another_one = input("Play again?(y/n): ")
        if another_one != "y":
            break
        else:
            user_score = 0
            rounds = 0
            ai_score = 0
            draws = 0

    if ai_score == 10:
        print(f"{bcolors.FAIL}You Lost, AI reached a score of {ai_score}! - GAME OVER{bcolors.ENDC}")
        another_one = input("Play again?(y/n): ")
        if another_one != "y":
            break
        else:
            user_score = 0
            rounds = 0
            ai_score = 0
            draws = 0

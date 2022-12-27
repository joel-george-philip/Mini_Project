
#The task is to Create the Rock, Paper and Scissors game with Python.


import random

print("| Rock Paper Scissors |")
print("_________________________")

list_Chr = ["rock", "paper", "scissors"]
User_Score = 0
CPU_Score = 0
i=1
n = int(input("Enter Number of Chances: "))
while i <= n:
    CPU_Chr = str(random.choice(list_Chr))
    User_Chr = input("Enter Rock, Paper, Scissors: ").lower()
    if User_Chr == CPU_Chr:
        print("Tie You Both Entered Same")
    elif User_Chr == "rock":
        print("Computer Enter: ", CPU_Chr)
        if CPU_Chr == "paper":
            print(" You lose! Paper covers Rock")
            CPU_Score += 1
        else:
            print(" You win! Rock smashes Scissors")
            User_Score += 1
    elif User_Chr == "paper":
        print("Computer Enter: ", CPU_Chr)
        if CPU_Chr == "scissors":
            print(" You lose! Scissor cut Paper")
            CPU_Score += 1
        else:
            print(" You win! Paper covers Rock")
            User_Score += 1
    elif User_Chr == "scissors":
        print("Computer Enter: ", CPU_Chr)
        if CPU_Chr == "rock":
            print(" You lose! Rock smashes Scissors")
            CPU_Score += 1
        else:
            print(" You win! Scissor cut Paper")
            User_Score += 1
    else:
        print(":(")
    print("\n\t******ScoreBoard******")
    print(f"\t You: {User_Score} | Computer: {CPU_Score}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    i += 1
    print("____________________________________________________________________________________")
    print()
print("\n\n ---------** Game Over **---------")
if User_Score < CPU_Score:
    print("Sorry You LOSE the game ")
    print("Computer WIN the game with score:", CPU_Score)
elif User_Score == CPU_Score:
    print(" Game Tied. Play Again ")
else:
    print(" You WIN the Game with score:", User_Score)
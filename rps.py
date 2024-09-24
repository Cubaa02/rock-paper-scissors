import random

try_again = 'y'
players_points = 0
computers_points = 0
print("Welcome to the ROCK, PAPER, SCISSORS! \n")
while try_again == 'y' or try_again == '':
    print("Choose rock, paper or scissors")
    players_choice = input().lower()


    computer = random.randrange(0,2)
    if(computer == 0):
        computers_choice = "rock"
    elif(computer == 1):
        computers_choice = "paper"
    elif(computer == 2):
        computers_choice = "scissors"

    if (players_choice == computers_choice):
        print("The computer chose " + computers_choice + ". \nIt's a Tie.")
    elif (players_choice == "rock"):
        if (computers_choice == "paper"):
            print("The computer chose " + computers_choice + ". \nYou lost.")
            computers_points += 1
            print(f"player: {players_points}, computer: {computers_points}")
        else:
                print("The computer chose " + computers_choice + ". \nYou won!")
                players_points += 1
                print(f"player: {players_points}, computer: {computers_points}")
    elif (players_choice == "paper"):
        if (computers_choice == "scissors"):
            print("The computer chose " + computers_choice + ". \nYou lost.")
            computers_points += 1
            print(f"player: {players_points}, computer: {computers_points}")
        else:
            print("The computer chose " + computers_choice + ". \nYou won!")
            players_points += 1
            print(f"player: {players_points}, computer: {computers_points}")
    elif (players_choice == "scissors"):
        if (computers_choice == "rock"):
            print("The computer chose " + computers_choice + ". \nYou lost.")
            computers_points += 1
            print(f"player: {players_points}, computer: {computers_points}")
        else:
            print("The computer chose " + computers_choice + ". \nYou won!")
            players_points += 1
            print(f"player: {players_points}, computer: {computers_points}")
    else:
        print("Error!")
    try_again = input("Do you want to calculate again? [y/n] ")
    print(f"player: {players_points}, computer: {computers_points}")
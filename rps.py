"""
Simple rock-paper-scissor game which allows the user to play against the computer.
Tallies the amount of times played and shows how many times the user won, lost, or tied
"""

from random import randint

wins = 0
losses = 0
ties = 0

print ("Hello, let's play a game of Rock-Paper-Scissors\n")

while True:
    user = input("Please select Rock(r), Paper(p), Scissors(s) or enter q to quit  ->  ")
    user = user.upper()
    comp_choice = randint(0,2)

    #makes sure that the user enters a valid input
    if(user != 'R' and user != 'S' and user != 'P' and user != 'Q'):
        print("Please enter a valid input")

    #changes the value of the computer choice for easier comparison against the user
    if(user == 'R' or user == 'P' or user == 'S'):
        if comp_choice == 0:
            computer = 'R'
        elif comp_choice == 1:
            computer = 'S'
        elif comp_choice == 2:
            computer = 'P'

        if(computer == 'R'):
            print("The computer chose ROCK")
        elif(computer == 'S'):
            print("The computer chose SCISSORS")
        elif(computer == 'P'):
            print("The computer chose PAPER")

        if(user == 'R'):
            print("You chose ROCK")
        elif(user == 'S'):
            print("You chose SCISSORS")
        elif(user == 'P'):
                print("You chose PAPER")

        #checks different game options and keeps count
        if computer == 'R' and user == 'R' or computer == 'S' and user == 'S' or computer == 'P' and user == 'P':
            print("You tied!\n")
            ties = ties + 1
        elif(computer == 'R' and user == 'S' or computer == 'P' and user == 'R' or computer == 'S' and user == 'P'):
            print("You lose!\n")
            losses = losses + 1
        elif(computer == 'S' and user == 'R' or computer == 'R' and user == 'P' or computer == 'P' and user == 'S'):
            print("YOU WON!\n")
            wins = wins + 1

    #option for if the user decides to quit the game
    #tallies all games played
    if user.strip() == 'Q':
        print("You played " + str(wins + losses + ties) + " times")
        print("You won " + str(wins))
        print("Lost " + str(losses))
        print("And tied " + str(ties))
        print("Goodbye!")
        break

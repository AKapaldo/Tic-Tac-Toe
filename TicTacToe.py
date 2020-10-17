"""
Author: Andrew Kapaldo
Date: October 15, 2020
Version: 1.0
Python 3.8
"""

# Import functions
from random import randint

# Set variables
space = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
moves = [" ", "X", "O"]
computer = ""
human = ""
p2 = ""


# Create functions for reusable code
def displayboard():
    print("-------------\n"
          "| " + space[1] + " | " + space[2] + " | " + space[3] + " |\n"
          "|-----------|\n"
          "| " + space[4] + " | " + space[5] + " | " + space[6] + " |\n"
          "|-----------|\n"
          "| " + space[7] + " | " + space[8] + " | " + space[9] + " |\n"
          "-------------")


def playermove():
    valid = False
    while not valid:
        player = input("Choose a space: ")
        try:
            player = int(player)
            test = space[player]
            if test != "X" and test != "O":
                space[player] = human
                valid = True
                displayboard()
            else:
                print("Space taken. Choose another.")
        except ValueError:
            print("Invalid entry. Choose a number between 1 and 9.")



def computermove():
    valid = False
    while not valid:
        cpu = randint(1, 9)
        test = space[cpu]
        if test != "X" and test != "O":
            space[cpu] = computer
            valid = True
            displayboard()
        else:
            valid = False


# Start program
valid = False
while not valid:
    choice = input("Do you want to be X or O?: ")
    if choice == "X" or choice == "x":
        human = moves[1]
        computer = moves[2]
        valid = True
    elif choice == "O" or choice == "o" or choice == "0":
        human = moves[2]
        computer = moves[1]
        valid = True
    else:
        print("Invalid input. Choose X or O.")
valid = False
while not valid:
    first = input("Do you want to go first? (Y or N): ").upper()
    if first == "Y":
        p2 = computer
        valid = True
    elif first == "N":
        p2 = human
        valid = True
    else:
        print("Invalid input. Enter Y or N.")
displayboard()
playing = True
lastmove = p2

# Set win conditions
while playing:
    if space[1] == space[2] and space[2] == space[3]:
        playing = False
        if human == space[1]:
            print("Congrats!! You won!")
        else:
            print("You lost. The computer beat you this time.")
    elif space[4] == space[5] and space[5] == space[6]:
        playing = False
        if human == space[4]:
            print("Congrats!! You won!")
        else:
            print("You lost. The computer beat you this time.")
    elif space[7] == space[8] and space[8] == space[9]:
        playing = False
        if human == space[7]:
            print("Congrats!! You won!")
        else:
            print("You lost. The computer beat you this time.")
    elif space[1] == space[4] and space[4] == space[7]:
        playing = False
        if human == space[1]:
            print("Congrats!! You won!")
        else:
            print("You lost. The computer beat you this time.")
    elif space[2] == space[5] and space[5] == space[8]:
        playing = False
        if human == space[2]:
            print("Congrats!! You won!")
        else:
            print("You lost. The computer beat you this time.")
    elif space[3] == space[6] and space[6] == space[9]:
        playing = False
        if human == space[3]:
            print("Congrats!! You won!")
        else:
            print("You lost. The computer beat you this time.")
    elif (space[1] != "1" and space[2] != "2" and space[3] != "3" and space[4] != "4" and
          space[5] != "5" and space[6] != "6" and space[7] != "7" and space[8] != "8" and
          space[9] != "9"):
        print("You tied. Try Again!")
        playing = False
    else:
        if lastmove == computer:
            lastmove = human
            playermove()
        elif lastmove == human:
            lastmove = computer
            computermove()
        else:
            print("Unknown error. How did you do that?!")

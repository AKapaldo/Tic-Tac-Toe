"""
Author: Andrew Kapaldo
Date: October 28, 2020
Version: 2.0
Python 3.8
"""

# Import functions
from random import randint

# Set variables
space = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
moves = ["X", "O"]
computer = ""
p1 = ""
p2 = ""
lastmove = ""
validFirst = ""
validChoice1 = ""
validChoice2 = ""
validAgain = ""
pvpOrPve = ""
playing = ""
game = True


# Create functions for reusable code
def displayboard():
    print("\n"
          "  " + space[1] + " | " + space[2] + " | " + space[3] + "  \n"
          " ----------- \n"
          "  " + space[4] + " | " + space[5] + " | " + space[6] + "  \n"
          " ----------- \n"
          "  " + space[7] + " | " + space[8] + " | " + space[9] + "  \n")


def playermove():
    validplayer = False
    while not validplayer:
        player1 = input("Choose a space player 1: ")
        try:
            player1 = int(player1)
            test = space[player1]
            if test != "X" and test != "O":
                space[player1] = p1
                validplayer = True
                displayboard()
            else:
                print("Space taken. Choose another.")
        except ValueError:
            print("Invalid entry. Choose a number between 1 and 9.")
        except IndexError:
            print("Invalid entry. Choose a number between 1 and 9.")


def player2move():
    validplayer2 = False
    while not validplayer2:
        player2 = input("Choose a space player 2: ")
        try:
            player2 = int(player2)
            test = space[player2]
            if test != "X" and test != "O":
                space[player2] = p2
                validplayer2 = True
                displayboard()
            else:
                print("Space taken. Choose another.")
        except ValueError:
            print("Invalid entry. Choose a number between 1 and 9.")
        except IndexError:
            print("Invalid entry. Choose a number between 1 and 9.")


def computermove():
    validcpu = False
    while not validcpu:
        cpu = randint(1, 9)
        test = space[cpu]
        if test != "X" and test != "O":
            print("The computer chose space: " + space[cpu])
            space[cpu] = computer
            validcpu = True
            displayboard()
        else:
            validcpu = False


def smartcomputer():
    validcpu = False
    while not validcpu:
        if space[1] == space[2] and space[3] == "3":
            print("The computer chose space: " + space[3])
            space[3] = computer
            validcpu = True
            displayboard()
        elif space[2] == space[3] and space[1] == "1":
            print("The computer chose space: " + space[1])
            space[1] = computer
            validcpu = True
            displayboard()
        elif space[4] == space[5] and space[6] == "6":
            print("The computer chose space: " + space[6])
            space[6] = computer
            validcpu = True
            displayboard()
        elif space[5] == space[6] and space[4] == "4":
            print("The computer chose space: " + space[4])
            space[4] = computer
            validcpu = True
            displayboard()
        elif space[7] == space[8] and space[9] == "9":
            print("The computer chose space: " + space[9])
            space[9] = computer
            validcpu = True
            displayboard()
        elif space[8] == space[9] and space[7] == "7":
            print("The computer chose space: " + space[7])
            space[7] = computer
            validcpu = True
            displayboard()
        elif space[1] == space[3] and space[2] == "2":
            print("The computer chose space: " + space[2])
            space[2] = computer
            validcpu = True
            displayboard()
        elif space[4] == space[6] and space[5] == "5":
            print("The computer chose space: " + space[5])
            space[5] = computer
            validcpu = True
            displayboard()
        elif space[7] == space[9] and space[8] == "8":
            print("The computer chose space: " + space[8])
            space[8] = computer
            validcpu = True
            displayboard()
        elif space[1] == space[4] and space[7] == "7":
            print("The computer chose space: " + space[7])
            space[7] = computer
            validcpu = True
            displayboard()
        elif space[1] == space[7] and space[4] == "4":
            print("The computer chose space: " + space[4])
            space[4] = computer
            validcpu = True
            displayboard()
        elif space[2] == space[5] and space[8] == "8":
            print("The computer chose space: " + space[8])
            space[8] = computer
            validcpu = True
            displayboard()
        elif space[4] == space[7] and space[1] == "1":
            print("The computer chose space: " + space[1])
            space[1] = computer
            validcpu = True
            displayboard()
        elif space[5] == space[8] and space[2] == "2":
            print("The computer chose space: " + space[2])
            space[2] = computer
            validcpu = True
            displayboard()
        elif space[2] == space[8] and space[5] == "5":
            print("The computer chose space: " + space[5])
            space[5] = computer
            validcpu = True
            displayboard()
        elif space[3] == space[6] and space[9] == "9":
            print("The computer chose space: " + space[9])
            space[9] = computer
            validcpu = True
            displayboard()
        elif space[6] == space[9] and space[3] == "3":
            print("The computer chose space: " + space[3])
            space[3] = computer
            validcpu = True
            displayboard()
        elif space[3] == space[9] and space[6] == "6":
            print("The computer chose space: " + space[6])
            space[6] = computer
            validcpu = True
            displayboard()
        elif space[1] == space[5] and space[9] == "9":
            print("The computer chose space: " + space[9])
            space[9] = computer
            validcpu = True
            displayboard()
        elif space[5] == space[9] and space[1] == "1":
            print("The computer chose space: " + space[1])
            space[1] = computer
            validcpu = True
            displayboard()
        elif space[1] == space[9] and space[5] == "5":
            print("The computer chose space: " + space[5])
            space[5] = computer
            validcpu = True
            displayboard()
        elif space[3] == space[5] and space[7] == "7":
            print("The computer chose space: " + space[7])
            space[7] = computer
            validcpu = True
            displayboard()
        elif space[5] == space[7] and space[3] == "3":
            print("The computer chose space: " + space[3])
            space[3] = computer
            validcpu = True
            displayboard()
        elif space[3] == space[7] and space[5] == "5":
            print("The computer chose space: " + space[5])
            space[5] = computer
            validcpu = True
            displayboard()
        else:
            cpu = randint(1, 9)
            test = space[cpu]
            if test != "X" and test != "O":
                print("The computer chose space: " + space[cpu])
                space[cpu] = computer
                validcpu = True
                displayboard()
            else:
                validcpu = False


# Start program
while game:
    validStart = False
    print("##################################################")
    print("###                 Tic Tac Toe                ###")
    print("##################################################")
    print("\nTry to get 3 in a row; vertically, horizontally, \nor diagonally! Try to block your opponent!\n"
          "Choose an empty space to claim by typing a number.")
    while not validStart:
        pvpOrPve = input("\n 1. Player vs. Player\n 2. Player vs. Random Computer\n 3. Player vs. Smart Computer"
                         "\n Q. Quit\nHow do you want to play?: ")
# Player vs. Player Game
        if pvpOrPve == "1":
            while not validChoice1:
                choice = input("Do you want to be X or O?: ")
                if choice == "X" or choice == "x":
                    p1 = moves[0]
                    p2 = moves[1]
                    validStart = True
                    validFirst = True
                    playing = True
                    validChoice1 = True
                    lastmove = p2
                    displayboard()
                elif choice == "O" or choice == "o" or choice == "0":
                    p1 = moves[1]
                    p2 = moves[0]
                    validStart = True
                    validFirst = True
                    playing = True
                    validChoice1 = True
                    lastmove = p2
                    displayboard()
                else:
                    print("Invalid input. Choose X or O.")
                    validStart = False
# Player vs. Computer Game
        elif pvpOrPve == "2" or pvpOrPve == "3":
            while not validChoice2:
                choice = input("Do you want to be X or O?: ")
                if choice == "X" or choice == "x":
                    p1 = moves[0]
                    computer = moves[1]
                    validStart = True
                    validFirst = False
                    playing = True
                    validChoice2 = True
                elif choice == "O" or choice == "o" or choice == "0":
                    p1 = moves[1]
                    computer = moves[0]
                    validStart = True
                    validFirst = False
                    playing = True
                    validChoice2 = True
                else:
                    print("Invalid input. Choose X or O.")
        elif pvpOrPve == "Q" or pvpOrPve == "q":
            print("Thanks for playing!")
            validStart = True
            validFirst = True
            playing = False
            validAgain = True
            game = False
        else:
            print("Invalid Input. Choose 1, 2, or 3 for a game or Q to quit.")
    while not validFirst:
        first = input("Do you want to go first? (Y or N): ").upper()
        if first == "Y":
            lastmove = computer
            validFirst = True
            displayboard()
        elif first == "N":
            lastmove = p1
            validFirst = True
            displayboard()
        else:
            print("Invalid input. Enter Y or N.")

    # Set win conditions
    while playing:
        if pvpOrPve == "1":
            if space[1] == space[2] and space[2] == space[3]:
                playing = False
                if p1 == space[1]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[4] == space[5] and space[5] == space[6]:
                playing = False
                if p1 == space[4]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[7] == space[8] and space[8] == space[9]:
                playing = False
                if p1 == space[7]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[1] == space[4] and space[4] == space[7]:
                playing = False
                if p1 == space[1]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[2] == space[5] and space[5] == space[8]:
                playing = False
                if p1 == space[2]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[3] == space[6] and space[6] == space[9]:
                playing = False
                if p1 == space[3]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[1] == space[5] and space[5] == space[9]:
                playing = False
                if p1 == space[1]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif space[3] == space[5] and space[5] == space[7]:
                playing = False
                if p1 == space[3]:
                    print("Congrats player 1!! You won!")
                    validAgain = False
                else:
                    print("Congrats player 2!! You won!")
                    validAgain = False
            elif (space[1] != "1" and space[2] != "2" and space[3] != "3" and space[4] != "4" and
                  space[5] != "5" and space[6] != "6" and space[7] != "7" and space[8] != "8" and
                  space[9] != "9"):
                print("You tied. Try Again!")
                playing = False
                validAgain = False
            else:
                if lastmove == p2:
                    lastmove = p1
                    playermove()
                elif lastmove == p1:
                    lastmove = p2
                    player2move()
                else:
                    print("Unknown error. How did you do that?!")
                    validAgain = False

        elif pvpOrPve == "2" or pvpOrPve == "3":
            if space[1] == space[2] and space[2] == space[3]:
                playing = False
                if p1 == space[1]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[4] == space[5] and space[5] == space[6]:
                playing = False
                if p1 == space[4]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[7] == space[8] and space[8] == space[9]:
                playing = False
                if p1 == space[7]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[1] == space[4] and space[4] == space[7]:
                playing = False
                if p1 == space[1]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[2] == space[5] and space[5] == space[8]:
                playing = False
                if p1 == space[2]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[3] == space[6] and space[6] == space[9]:
                playing = False
                if p1 == space[3]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[1] == space[5] and space[5] == space[9]:
                playing = False
                if p1 == space[1]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif space[3] == space[5] and space[5] == space[7]:
                playing = False
                if p1 == space[3]:
                    print("Congrats!! You won!")
                    validAgain = False
                else:
                    print("You lost. The computer beat you this time.")
                    validAgain = False
            elif (space[1] != "1" and space[2] != "2" and space[3] != "3" and space[4] != "4" and
                  space[5] != "5" and space[6] != "6" and space[7] != "7" and space[8] != "8" and
                  space[9] != "9"):
                print("You tied. Try Again!")
                playing = False
                validAgain = False
            else:
                if pvpOrPve == "2":
                    if lastmove == computer:
                        lastmove = p1
                        playermove()
                    elif lastmove == p1:
                        lastmove = computer
                        computermove()
                    else:
                        print("Unknown error. How did you do that?!")
                        validAgain = False
                elif pvpOrPve == "3":
                    if lastmove == computer:
                        lastmove = p1
                        playermove()
                    elif lastmove == p1:
                        lastmove = computer
                        smartcomputer()
                    else:
                        print("Unknown error. How did you do that?!")
                        validAgain = False
                else:
                    print("Unknown Error. How did you do that?!")
    while not validAgain:
        playAgain = input("Play another round? (Y/N): ").upper()
        if playAgain == "Y":
            validStart = False
            validAgain = True
            validChoice1 = False
            validChoice2 = False
            game = True
            space = [None, "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        elif playAgain == "N":
            print("Thanks for playing!")
            validAgain = True
            game = False
        else:
            print("Invalid input. Choose Y or N.")
            validAgain = False
            game = False

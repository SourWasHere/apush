import random
import sys

arguments = sys.argv
moves = ["rock", "paper", "scissors"]

def decideWinner(user_input, choice):
	if user_input == "rock" and choice == "paper" or user_input == "paper" and choice == "scissors" or user_input == "scissors" and choice == "rock":
		return "you lose"
	elif user_input == choice:
		return "draw"
	else:
		return "you win"

def playGame(user_input):
	choice = moves[random.randrange(0, 3)]
	print("computer choice: " + choice)
	print(decideWinner(user_input, choice))

if len(sys.argv) == 2:
	playGame(sys.argv[1])
else:
	print("error: need one argument, pick from rock, paper, or scissors")








































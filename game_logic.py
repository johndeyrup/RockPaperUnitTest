import random

def do_throw(throws, number):
	return throws[number]

def check_win(your_throw, opponent_throw):
	loss = "You Lose!"
	win = "You Win!"
	tie = "It's a tie"
	if( your_throw == opponent_throw):
		return tie
	elif ( your_throw == "rock" and opponent_throw == "scissor" ):
		return win
	elif ( your_throw == "rock" and opponent_throw == "paper"):
		return loss
	elif ( your_throw == "scissor" and opponent_throw == "paper"):
		return win
	elif ( your_throw == "scissor" and opponent_throw == "rock"):
		return loss
	elif ( your_throw == "paper" and opponent_throw == "rock"):
		return win
	elif ( your_throw == "paper" and opponent_throw == "scissor"):
		return loss
	else:
		raise ValueError("Entered invalid inputs %s and %s should be rock, paper or scissor" % (your_throw, opponent_throw))

def generate_computer_throw(a,b):
	return random.randint(a,b)

def play_computer(your_throw):
	throws = ["rock", "paper", "scissor"]
	comp_number = generate_computer_throw(0,2)
	comp_throw = do_throw(throws, comp_number)
	result = check_win(your_throw, comp_throw)
	return comp_throw.capitalize(), result
# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars


while gameVars.player is False:
	# set gameVars.player to True
	print("**********************************")
	print("gameVars.Computer lives: ", gameVars.computer_lives, "/5\n")
	print("gameVars.Player lives: ", gameVars.player_lives, "/5\n")
	print("Choose your weapon!\n")
	print("**********************************")

	gameVars.player = input("choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()

	print("gameVars.computer chose ", gameVars.computer, "\n")
	print("gameVars.player chose ", gameVars.player, "\n")

	if gameVars.player == "quit":
		exit()
	elif gameVars.computer == gameVars.player:
		print("tie! no one wins, play again")

	elif gameVars.player == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")


	# handle all lives lost for gameVars.player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]	
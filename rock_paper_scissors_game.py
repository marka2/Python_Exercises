"""
*************************************
Author: Mark Arakaki
October 18, 2017
Personal Practice Use
*************************************

Two player Rock-Paper-Scissors game. 

"""

play_again = True

print "\nWelcome to Mark's Awesome Rock-Paper-Scissors Game!\n"

while play_again == True:	

	player1_move = raw_input("\nPlayer 1, please type either rock, paper, or scissors (all lowercase): ")
	player2_move = raw_input("\nPlayer 2, please type either rock, paper, or scissors (all lowercase): ")

	if player1_move == "rock":
		if player2_move == "paper":
			print "\nPlayer 2 Wins!\n"
		elif player2_move == "rock":
			print "\nDRAW!\n"
		elif player2_move == "scissors":
			print "\nPlayer 1 Wins!\n"
		else:
			print "\nInvalid input, listen to instructions!\n"
	elif player1_move == "paper":
		if player2_move == "rock":
			print "\nPlayer 1 Wins!\n"
		elif player2_move == "paper":
			print "\nDRAW!\n"
		elif player2_move == "scissors":
			print "\nPlayer 2 Wins!\n"
		else:
			print "\nInvalid input, listen to instructions!\n"
	elif player1_move == "scissors":
		if player2_move == "paper":
			print "\nPlayer 1 Wins!\n"
		elif player2_move == "rock":
			print "\nPlayer 2 Wins!\n"
		elif player2_move == "scissors":
			print "\nDRAW!\n"
		else:
			print "\nInvalid input, listen to instructions!\n"
	else:
		print "\nInvalid input, listen to instructions!\n"
	
	tryAgain = raw_input("Do you want to play again. If so, in lowercase letters enter yes, if not enter no: ")
	
	if tryAgain == "yes":
		play_again == True
	elif tryAgain == "no":
		play_again == False
		print "\nThank you for playing!"
		break
	else:
		print "\nInvalid input. Ending game.\n"
		break

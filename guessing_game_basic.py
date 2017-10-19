"""
************************************
Author: Mark Arakaki
October 18, 2017
Personal Practice
************************************

Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
Random number must be between 1 and 9 (including 1 & 9). 

"""

import random

attempt_guess = False

num = random.randint(1, 9)

while attempt_guess == False:

	guess = int(raw_input("Please enter in your guess! Remember that you number needs to be between (including) 1 and 9: "))
	if guess > num:
		print "You guess is too high! Try Again."
	elif guess == num:
		print "Your right! Congratulations! Game Over."
		attempt_guess = True
		break
	elif guess < num: 
		print "You guess is too low! Try Again."
	

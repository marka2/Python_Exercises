"""

***********************************************
Author: Mark Arakaki
October 15, 2017
Personal Practice Use
***********************************************

	Ask the user for a number. Depending on whether the number is
	even or odd, print out an appropriate messsage to the user.

	Extras:
	1) if the number is a multiple of 4, print out a different message
	2) ask the user for two numbers one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

print("\nBEGIN PART 1\n")

num = input("Please enter in a number: ")

if num == 0:
        
	print("\nThe number you have entered is a zero, which is neither even nor odd...")

elif num % 2 == 0:
	
	print ("The number you have entered (" + str(num) + ") is even!")
	
	if num % 4 == 0:

        	print ("The number you have entered (" + str(num) + ") is a multiple of 4 as well!")
else:

	print("\nThe number you have entered (" + str(num) + ") is odd!")

#######################################################################################################

print("\nBEGIN PART 2\n")

num = input ("Please enter in a number that you want to be divided by another number: ")

check = input ("\nPlease enter in a number that will divide the original number by: ")

if num == 0:
	print("\nYou cannot divide zero by another number. You literally created a black hole... Congratulations.")
elif num % check == 0:
	print("\n" + str(num) + " divides evenly with " + str(check) + "!")
else:
	print("\n" + str(num) + " does not divide evenly with " + str(check) + "!")

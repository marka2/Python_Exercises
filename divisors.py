"""

******************************************************
Author: Mark Arakaki
October 15, 2017
Personal Practice Use
*****************************************************

Divisors:

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don't know what a divisor is, it is a number that divides evently into another number. For example, 13 is divisor of 26 because 26 / 13 has no remainder.)

"""

number = input("Please enter in a number that you want divided: ")

list_of_divisors = []

print("Listed below are the list of possible divisors for the inputted integer: \n")

if number == 0:
	print("")
		
else:
	
	divisor = number / 2
	
	while divisor > 0:
		list_of_divisors.append(divisor)
		divisor = divisor / 2
	
print(list_of_divisors)

"""
*******************************************
Author: Mark Arakaki
October 18, 2017
Personal Practice Use
*******************************************

Q) Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

userString = raw_input("Please enter in a string that will be checked if it is a palindrome: ")

userString = str(userString)

reverse = userString[::-1] # reverses the string

if userString == reverse:
	print ("Yes, the inputted string is a palindrome!")
else:
	print ("No, the inputted string is not a palindrome.....")


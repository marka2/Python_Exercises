"""
***************************
Author: Mark Arakaki
November 3, 2017
Personal Practice Use
***************************

Q) Ask the user for a number and deterine whether the number is prime or not. (For those who have forgotten, a prime is a number that has no divisors.).

"""

def getInteger():
    return int(input("Please input a number:"))

number = getInteger()
if number % 2 != 0:
    if number % 3 != 0:
        print("The number you have entered is a prime number")
else:
    print("The number you have entered is not a prime number")

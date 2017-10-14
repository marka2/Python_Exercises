"""
    This program asks the user to enter their name and their age. Then the program will print out a message addressed to them that tell them the year they will turn 100 years old.
"""

import datetime

name = input("Please enter in your name: ")

print ("Nice to meet you " + name)
age = input("Please enter in your age: ")

num_of_iterations = input("How many times would you like the final message to display? ")

advanceAge = 100 - age
advanceAge = datetime.datetime.now().year + advanceAge

final_message = ""

for x in range(0, num_of_iterations):
        print ("Hey " + name + " you will turn 100 in the year " + str(advanceAge))

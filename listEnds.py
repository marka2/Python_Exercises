"""
Author: Mark Arakaki
Date: November 24, 2017
Personal Practice Use

Create a program that takes in a list from user input and prints out the first and last element from that list.
"""

def listEnds(list):
    print "The first element in the list is %s." % list[0]
    print "The last element in the list is %s." % list[len(list)-1]
    return;

userInput = "default"
myList = []

while (userInput != "done"):
    userInput = raw_input("Please enter in numbers for your list. When you are done type in 'done'.\n");
    
    if userInput != "done":
        myList.append(userInput);

listEnds(myList);

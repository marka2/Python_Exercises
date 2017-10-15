"""

Author: Mark Arakaki
October 14, 2017
Personal Practice Use

"""

firstVariable = 45

print firstVariable

def printme(str):
	"This prints a passed string into this function"
	print str
	return;

def changeme(myList):
	"This changes a passed list into this function"
	mylist.append([1,2,3,4]);
	print "Values inside the function: ", mylist
	return;

def printinfo(name, age):
	"This prints a passed info into this function"
	print "Name: ", name
	print "Age: ", age
	return;

def sum(arg1, arg2):
	total = arg1 + arg2
	print "Inside the function: ", total
	return total;

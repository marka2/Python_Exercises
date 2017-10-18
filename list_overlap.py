"""

***********************************
Author: Mark Arakaki
October 15, 2017
Personal Practice Use
**********************************

Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure the program works on two lists of different sizes.

Extras:
	1) Randomly generate two lists to test this
	2) Write this in one line of Python

"""

import random

num_of_elements1 = random.randrange(20, 30)
num_of_elements2 = random.randrange(20, 30)

a = random.sample(range(100), num_of_elements1)
b = random.sample(range(100), num_of_elements2)

print "Randomly Generated List 1: " + str(a) 
print "Randomly Generated List 2: " + str(b)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

length_of_list1 = len(a)

overlap_list = []

for x in range (0, length_of_list1):
	if b.count(a[x]) > 0:
		overlap_list.append(a[x])

length_of_final_list = len(overlap_list)

for f in range (0, length_of_final_list - 2):

	if overlap_list[f] == overlap_list[f+1]:
		overlap_list.remove(overlap_list[f])

print "Overlap List: " + str(overlap_list)


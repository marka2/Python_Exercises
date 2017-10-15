"""

Take a list, say for example this one:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 24, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
	1) Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
	2) Write this in one line of Python.
	3) Ask the user for a number and return a list that contains only elements from the original list 'a' that are smaller than the nubmer given by the user.

"""

print("\n PART 1 WILL DISPLAY ELEMENTS LESS THAN 5\n")

a = [1, 1, 2, 3, 5, 8, 13, 21, 24, 34, 55, 89]

pulledList = []
part2List = []

number_of_elements = len(a)

for i in range(0, number_of_elements):
	if a[i] < 5:
		pulledList.append(str(a[i]))
#for d in pulledList:
#	print(d),				

print pulledList

print("\n\nPART 2 WILL DISPLAY ELEMENTS LESS THAN USER INPUTTED NUMBER\n")

num_for_comparison = input("Please enter in a number that will be used to compares values in the list: ")

for k in range(0, number_of_elements):
	if a[k] < num_for_comparison:
		part2List.append(str(a[k]))
print part2List	

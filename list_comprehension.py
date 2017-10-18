"""
***************************************
Author: Mark Arakaki
October 18, 2017
Personal Practice Use
***************************************

Q) If given a saved list in a variable such as "a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]". Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it. 

"""

a = [1, 4, 9, 26, 25, 36, 49, 64, 81, 100]

final_even_list = [number for number in a if number % 2 == 0]

print final_even_list

# Task 4. Write a Python program to convert a given list of strings into list of lists using map
# function.

import ast

str_list = ast.literal_eval(input("Enter a list of strings:"))

lol= map(lambda x: list(x), str_list)

print(list(lol))
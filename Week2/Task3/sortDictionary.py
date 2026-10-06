# Task 3. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries : [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi
# Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue’}]
# Sorting the List of dictionaries :  [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make':
# 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

import ast

dict = ast.literal_eval(input("Enter a list of dictionaries:"))

print("sorted list of dictionary:",sorted(dict,key=lambda x:x['color']))
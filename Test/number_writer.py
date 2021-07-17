import json

numbers = [1, 2, 54, 7, 54, 2]
"""
open file with 'w' will write in a null file
"""
filename = 'numbers.json'
with open(filename, 'w') as file:
    json.dump(numbers, file)

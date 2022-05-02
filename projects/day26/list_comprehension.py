# Pattern:
# new_list = [new_item for item in list]
""" 
numbers = [1, 2, 3, 4, 5]
new_list = [item + 1 for item in numbers]
print(new_list)

name = "Viktor"
letter_list = [letter for letter in name]
print(letter_list)
"""

""" 
with open("file1.txt") as file1:
  numbers_file1 = [int(line.strip()) for line in file1]

with open("file2.txt") as file2:
  numbers_file2 = [int(line.strip()) for line in file2]

result = [num for num in numbers_file1 if num in numbers_file2]
# Write your code above 👆

print(result)
# [3, 6, 5, 33, 12, 7, 42, 13]

 
"""

range_list = [num * 2 for num in range(1, 17, 2) if num > 12]
print(range_list)

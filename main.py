
from hashlib import new


num_list = [5,4,17,19,30,2,7,10,45]

# Q1: Write a Python program to sum all the items in the list.
print(f"the sum: {sum(num_list)}\n")

# Q2: Write a Python program to get the largest number from the list.
print(f"the max: {max(num_list)}\n")

# Q3: using List Comprehension , create a new list from the above list containing only even numbers.

# even_nos = [num for num in list1 if num % 2 == 0]
even_list = [i for i in num_list if i%2==0]
print(f"even list: {even_list}\n")

# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list = even_list[5:]
print(f"sliced list: {new_list}\n")


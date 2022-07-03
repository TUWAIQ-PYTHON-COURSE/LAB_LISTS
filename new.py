## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

# Q1: Write a Python program to sum all the items in the list.

list_1 = [5, 4, 17, 19, 30, 2, 7, 10, 45]

print(list_1)
# Q2: Write a Python program to get the largest number from the list.

largest_number = max(list_1)

print(largest_number)
# Q3: using List Comprehension , create a new list from the above list containing only even numbers.

even_numbers = [number for number in list_1 if number %2 == 0]

print("even numbers in the list are:", even_numbers)
# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_list = list_1 [:5]

print(new_list)
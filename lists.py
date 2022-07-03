# LAB_LISTS

## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]



my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]

### Q1: Write a Python program to sum all the items in the list.
sum = sum(my_list)
print(sum)

### Q2: Write a Python program to get the largest number from the list.

ma= max(my_list)
print(ma)

### Q3: using List Comprehension , create a new list from the above list containing only even numbers.
evensList = [x for x in my_list if x % 2 == 0]
print(evensList)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list

new_list2 = my_list[0:5]

print(new_list2)
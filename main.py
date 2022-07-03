# LAB_LISTS

## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]
### Q1: Write a Python program to sum all the items in the list.

my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
x = sum(my_list)
print(x)

### Q2: Write a Python program to get the largest number from the list.

print("Largest number is:", max(my_list))

### Q3: using List Comprehension , create a new list from the above list containing only even numbers.
my_list2 = [i for i in my_list if i%2 == 0 ]
print(my_list2)


### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_list = my_list[:5]

print(new_list)
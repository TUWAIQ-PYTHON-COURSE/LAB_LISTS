# LAB_LISTS

## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

### Q1: Write a Python program to sum all the items in the list.
### Q2: Write a Python program to get the largest number from the list.
### Q3: using List Comprehension , create a new list from the above list containing only even numbers.
### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

num = [5, 4, 17, 19, 30, 2, 7, 10, 45]
total = 0
for x in num:
    total += x
even_num = [num for num in num if num % 2 == 0]
new_list = num[0:5]
print("The total is:",total)
print("Largest element is:", max(num))

 
print("Even numbers in the list: ", even_num)

print(new_list)
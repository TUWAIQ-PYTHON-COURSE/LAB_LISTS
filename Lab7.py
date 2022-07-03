
list = [5, 4, 17, 19, 30, 2, 1, 10, 45]

# Q1: Write a Python program to sum all the items in the list.

sum = 0 
for i in list:
    sum = sum + i 

print("the sum of all items in list = " , sum)

# Q2: Write a Python program to get the largest number from the list.

largeNumber = 0
for i in list:
    if (i > largeNumber):
        largeNumber = i 

print("the largest number in list  =" , largeNumber) 

# Q3: using List Comprehension , create a new list from the above list containing only even numbers.

evenNumbers = [i for i in list if i % 2 == 0 ]

print(evenNumbers)

# Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

newList = list[:5]
print(newList)
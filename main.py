'''Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]
Q1: Write a Python program to sum all the items in the list.
Q2: Write a Python program to get the largest number from the list.
Q3: using List Comprehension , create a new list from the above list containing only even numbers.
Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.'''


my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
sum = 0
for num in my_list:
    sum+=num

print("The Sum of the list is : ",sum)
largest_num = my_list[0]
for i in my_list:
   if i > largest_num:
    largest_num = i

print("The largest number is :",largest_num)
even_num = list()
for x in my_list:
    if (x % 2) == 0:
        even_num.append(x)

print("The even numbers is : ",even_num)


print(my_list[:5])
## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

from tkinter import N


new_list=[5, 4, 17, 19, 30, 2, 7, 10, 45]

### Q1: Write a Python program to sum all the items in the list.
sum=0
for n in (new_list):
 sum=sum+n
print("Sum all the items in the list",sum)

### Q2: Write a Python program to get the largest number from the list.

max_num=max(new_list) 
print(max_num)

### Q3: using List Comprehension , create a new list from the above list containing only even numbers.
newlist=[n for n in new_list if n%2==0]
print(newlist)


### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_list2=new_list[0:5]
print(new_list2)
    

## Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]
### Q1: Write a Python program to sum all the items in the list.



mylist = [5, 4, 17, 19, 30, 2, 7, 10, 45]
print()
print('the list == >', mylist, '\n')

### Q2: Write a Python program to get the largest number from the list.
 
print('the big Number is ==> ', max(mylist))
print()




### Q3: using List Comprehension , create a new list from the above list containing only even numbers.


for i in mylist:
 if(i%2)==0:
  print('even == >', i)
  ''' here my solution'''

even_number = [n for n in mylist if n%2 ==0]
print()
print('After Solution', even_number)
'''public_solution'''

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

new_list = mylist[5:]
print()
print('slicing == >', new_list)
print()

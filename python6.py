import math
my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
total = 0
for num in my_list:
    total += num 

print(total)

largest_number = my_list [0]
for i in my_list:
    if i > largest_number:
        largest_number = i
print(largest_number)        

even_numper = [a for a in my_list  if (a % 2)== 0]

print( even_numper)        

print(my_list [:5])



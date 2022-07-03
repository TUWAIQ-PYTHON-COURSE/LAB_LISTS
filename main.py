my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]

# Q1
sum = 0
for element in my_list:
    sum += element
print (f"The sum is: {sum}")

#Q2
largest_num = my_list[0]
for element in my_list:
    if largest_num < element:
        largest_num = element
    else:
        largest_num
print(f"The largest number is: {largest_num}")

#Q3
new_list = []
for element in my_list:
    if not element % 2:
        new_list.append(element)
print (new_list)

#Q4
my_list = my_list[:5]

print(my_list)
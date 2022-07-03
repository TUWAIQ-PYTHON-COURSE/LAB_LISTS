list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
sum = sum(list)
print(sum)                                  #   Question 1

list.sort()
print(list)
print(" This is large number :",list[-1])    #  Question 2


even_numbers_list = []

for x in list:
    if x % 2 == 0:
        even_numbers_list.append(x)           # Question 3
print("even numbers :",even_numbers_list)



new_list = list[:5]                       # Question 4
print(new_list)
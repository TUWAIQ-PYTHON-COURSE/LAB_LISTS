my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
print(sum(my_list))
x = max (my_list)
print(x)

for num in my_list:
    even_numbers_list = [n for n in my_list if n%2 == 0]
print(even_numbers_list)
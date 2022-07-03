def sum(list):
    addition = 0
    for i in range(0, len(list)):
        addition = addition + list[i]
    print(f'The sum of the list elements is : {addition}')
    max_element = max(list)
    print(f'The max element of the list is : {max_element}')

def even_elements(list):
    even = []
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            even.append(list[i])
        else:
            continue
    print(f'The even elements in list are : {even}')


list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
sum(list)
even_elements(list)
print(f'Using list slicing :  {list[:5]}')
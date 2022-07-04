numberList= [5, 4, 17, 19, 30, 2, 7, 10, 45]

#[1]
sum = 0
for i in numberList:
    sum += i
print("The sum of all items in the list:", sum)

#[2]
max = numberList[0]
for i in numberList:
    if i > max:
        max = i
print("The largest number in the list:",max)

#[3]
print("The Even numbers in the list: ")
'''Using list comprehension'''
evenNumbers = [i for i in numberList if i % 2 == 0]
print(evenNumbers)

#[4]
print("List starting from the strt to 5th element in the list:")
'''Using list slicing'''
print(numberList[ : 5])
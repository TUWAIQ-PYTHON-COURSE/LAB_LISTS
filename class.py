#creating an empty list

my_empty_list = list()
my_empty_list2 = []

#create a list with initial values 
my_list = ["Apple", "Kiwi", "Orange", "Kiwi"]


#adding an element to the end of the list
my_list.append("Cherry")

print(my_list)

#adding an element at a specific index

my_list.insert(2, "Banana")

print(my_list)

#accessing an elment in the list using the index

print(my_list[4])


#accessing an elment from the end , using negatinve index
print(my_list[-1])

#adding a list to another list

my_list2 = ["Tennis", 547]

my_list.extend(my_list2)

print(my_list)

#combining two lists using the + operator
combined_list = my_list2 + my_list

print(combined_list)



#deleting an element from a list and getting the value

deleted_item = my_list.pop(4)
print(deleted_item)
print(my_list)

#deleting an item using delete
del my_list[1]

print(my_list)


#to loop on list
for element in my_list:
    print("---> ", element)

list_length = len(my_list)
print(f"The list length is : {list_length}")


#to test for membership of an element inside a list

is_tennis = "Tennis" in my_list

if "Tennis" in my_list:
    print("Found !")
else:
    print("Not found")


#slicing in a list

new_list = my_list[1:3]

print(new_list)

print("#"*50)

#Tuples

#creating an empty tupe
empty_tuple = tuple()

#creating with inital values
new_tuple = ("value1", 439, "value3")

new_tuple2 = "value1", 439, "value3"

print(new_tuple[1])


new_combined_tuple = new_tuple + new_tuple2

print(new_combined_tuple)

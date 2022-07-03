
list = [5, 4, 17, 19, 30, 2, 7, 10, 45] 

#Q1
sum = 0 
for elemnt in list :  
    sum += elemnt 
print(sum)


#q2 
larg = 0 
for i in list : 
    if larg < i :
        larg = i 
    elif larg > i :
        larg = larg 

print(larg)

#q3 

list = [5, 4, 17, 19, 30, 2, 7, 10, 45] 
newList = [ i for i in list if i % 2 == 0]
print(newList)

#q4 

print(list[:5])


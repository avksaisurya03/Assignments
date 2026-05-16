#1. Find the size of a set in python
set1 = {1,2,3,4,5}
print(len(set1))

#2. Iterate over a set in python
set2 = {"ram","sai","charan"}
it= iter(set2)
for i in range(len(set2)):
    print(next(it))

#3. To identify the max and min value in numbers set
set3 = {10,20,30,40,50}
print(max(set3))
print(min(set3))

#4. Remove items from set 
set4 = {0,9,8,7,6,5}
set4.remove(0) #in this if the element which we are removing , is does not exist in the set then it gets error
print(set4)
set4.discard(10)  # in this it does not get error if the element is not present 
print(set4)

#5. if two lists have at-least one element common using sets
lst1 = [1,2,3,4]
lst2 = [4,5,6,7]
if set(lst1).intersection(set(lst2)):   #intersect is used to get common elements in the sets. 
    print("True")
else:    
    print("False")

#6. Find common elements in three lists using sets
lst1 = [1,2,5,4]
lst2 = [4,5,6,7]
lst3 = [4,5,8,9]    
print(set(lst1).intersection(set(lst2),set(lst3)))

#7. Find missing and additional values in two lists using sets
lst3 = [1,2,4,5]
lst4 = [3,4,5,7]
print("missing values:",(set(lst3).difference(set(lst4))))  # returns the elements which are not present in set2. 
print("additional values:",(set(lst4).difference(set(lst3)))) 

#8. find the difference between two lists using sets
lst5 = [1,2,3,4]
lst6 = [3,4,5,6]
print(set(lst5) - set(lst6)) # here both the difference method and '-' operator behaves same. 
print(set(lst5).difference(set(lst6)))


#lists
#1.  to interchange first and last elements in a list 
num1 = [1,2,3,4,5,["hi",True],False]
num1[0], num1[-1] = num1[-1], num1[0]
print(num1)

#2. to swap two elements in a list 
num2 = [1,2,3,4,5,["hi",True],False]
num2[2],num2[5] = num2[5],num2[2]
print(num2)

#3. to find ways to get the length of list 
num3 = [1,2,3,4,5,["hi",True],False]
len(num3)    # built in function
count = 0    # using for loop   
for i in num3:
    count +=1
print(count)

#4. to check if element exists in list in different ways. 
num4 = [1,2,3,4,5,["hi",True],False]
# checking 5 is present in num4 or not
5 in num4
print(num4.index(5))
print(num4.count(5))

#5. different ways to clear a list 
num5 = [1,2,3,4,5,["hi",True],False]
num5.clear()
print(num5)

#6. Python program to Reversing a List 
num6 = [100,200,300,400]
num6.reverse()
print(num6)

#7. #Python program to Cloning or Copying a list without using inbuilt function. 
num7 = [1,2,3,4,5,["hi",True],False]
num71 = []
for i in num7:
    num71.append(i)
print(num71)

#8. Python program to Count occurrences of an element in a list
num8 = [0,1,2,3,4,5,["hi",True],False]
print(num8.count(0)) #here false also count as 0

#9. Python Program to find sum and average of List in Python 
num9 =  [100,200,300,400]
print(sum(num9))
print(sum(num9)/ len(num9))

#10.To Sum of number digits in List
num10 = [101,102,103,104]
result = []
for i in num10:
    count = 0
    while i > 0:
        digit = i % 10
        count += digit
        i //= 10
    result.append(count)
print(result)

#11.To Multiply all numbers in the list
num11 = [1,2,3,4]
result = 1
for i in num11:
    result *=i
print(result)

#12. Python program to find smallest number in a list
num12 = [212,132,3243,32454,12]
num12.sort()
print(num12[0])

#13. to find largest number in a list 
num12 = [212,132,3243,32454,12]
num12.sort(reverse = True)
print(num12[0])

#14.to find second largest number in a list
num13 = [212,132,3243,32454,12]
num13.sort(reverse = True)
print(num13[1])

#15. to print even numbers in a list 
num14 = [1,2,3,4,5,21,34,43,45,23,34,123,86,75,12]
for i in num14:
    if i % 2 == 0 :
        print(i, end=" ")

#16. to print odd numbers in a list
num15 = [1,2,3,4,5,21,34,43,45,23,34,123,86,75,12]
for i in num15:
    if i % 2 != 0 :
        print(i, end=" ")

#17. to print all even numbers in a range 
for i in range(1,51):
    if i  % 2 == 0:
        print(i, end=" ")

#18. to print all odd numbers in a range
for i in range(1,51):
    if i % 2 != 0:
        print(i, end=" ")

#19. 
lst = [1,2,3,4,5,6,7,8,9,10]
count1 = 0
count2 = 0
for i in lst:
    if i % 2 == 0:
        count1 +=1
    else:
        count2 +=1
print("Count of even numbers:",count1)
print("Count of odd numbers:",count2)

#20 print positive numbers in a list
lst1 = [1,2,-3,-4,5,6,-7,-9,100]
for i in lst1:
    if i > 0:
        print(i,end= ",")

#21. print negative numbers in a list
lst1 = [1,2,-3,-4,5,6,-7,-9,100]
for i in lst1:
    if i < 0:
        print(i,end=",")

#22. print all positive numbers in a range
pos = []
for i in range(-5,5):
    if i >0:
        pos.append(i)
print(pos)

#23. print all negative numbers in a range
neg = []
for i in range(-5,5):
    if i < 0:
        neg.append(i)
print(neg)

#24 count positive and negative numbers in a list
pos = 0
neg = 0
for i in range(-5,10):
    if i > 0 :
        pos +=1
    elif i < 0:
        neg +=1
print("pos_nums_count:",pos)
print("neg_nums_count:",neg)

#25. Remove multiple elements from a list in Python 
lst2  = [1,2,3,4,5]
remove = [2,4]
for i in remove:
    if i in lst2:
        lst2.remove(i)
print(lst2)

#26. to Remove empty tuples from a list
lst3 = [(1,2),(),(),(3,4)]
result = []
for i in lst3:
    if i !=():
        result.append(i)
print(result)

#27. print duplicates from a list of integers
lst4 = [1,2,2,3,4,4,5,10]
duplicate = []
for i in lst4:
    if lst4.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print(duplicate)    


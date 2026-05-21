#for loop Assignment
#1. factorial of a number
fact = 1
for i in range(1,7):
    fact *= i
print(fact) 

#2. a program in Python to reverse a word. 
reverse = ""
s = "sai surya"
for i in s:
    reverse = i + reverse
print(reverse)

#3. a program in pyhton to reverse a num
num = 123
rev = ''
for i in str(num):
    rev = i + rev
print(int(rev))

#4.  a program to display the first 7 multiples of 7.
for i in range(1,8):
    print(i*7, end = " ")

#5. program that appends the square of each number to a new list. 
list = [2,3,4,5]
new = []
for i in list:
    new.append(i*i)
print(new)

#6.to separate positive and negative number from a list. 
list1 = [1,-2,3,-4,5,-6]
pos = []
neg = []
for i in list1 :
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)

#7. a program that appends the type of elements from a list. 
list2 = [1,True,"hi",20.5]
types = []
for i in list2:
    types.append(type(i))
print(types)

#8. a program to filter even and odd number from a list. 
list3 = [1,2,3,4,5,6,7,8,9,0]
even = []
odd = []
for i in list3 :
    even.append(i) if i % 2 == 0 else odd.append(i)
print(even)
print(odd)

#9. a program to fetch only even values from a dictionary. 
dict1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
for i in dict1 :
    if dict1[i] % 2 == 0:
        print(i,dict1[i])

#10.  a program to check the given string is a palindrome or not. 
s1 = "madam"
rev = ""
for i in s1:
    rev = i + rev 
"palindrome" if s1 == rev else "not a palindrome"

#11. a program to check the given number is a prime or not. 
import math
num = 50
if num > 1 :
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            print("not a prime")
            break
    else:
        print("prime")
else:
    print("not a prime")

#12. a program to print all prime numbers between 0 and user entered number.
num1 = int(input("Enter the prime numbers btw 0 to user entered:"))
if num1 > 1:
    for num in range(2,num1+1):
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                break
        else:
            print(num)

#13. to calculate the sum of all prime numbers between 0 and user entered number.
num1 = int(input("Enter the sum of all prime numbers between 0 and user entered number :"))
total = 0
if num1 > 1:
    for num in range(2,num1+1):
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                break
        else:
            total += num
print(total)

#14. a program to calculate the product of all prime numbers between 0 and user entered number.
num1 = int(input("Enter the product of all prime numbers between 0 and user entered number:"))
total = 1
if num1 > 1:
    for num in range(2,num1+1):
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                break
        else:
            total *= num
print(total)

#15. Reverse the entered number by printing the remainder. 
num = int(input("Enter a Reverse the entered number by printing the remainder "))
for i in range(len(str(num))):
    print(num % 10, end="")
    num //= 10

#16. Reverse the entered number.
num1 = input("Enter Reverse the entered number.:")
rev = ""
for i in str(num1):
    rev = i + rev 
print(int(rev))

#17.Sum of each digit from a number. 
sum1 = 0
num = 12345
for i in str(num):
    sum1 +=int(i)
print(sum1)

#18. check no. is Armstrong or not.   #
# 18) Armstrong number
num = int(input("Enter the Armstrong num:"))
temp = str(num)
power = len(temp)
total = 0
for i in temp:
    total += int(i) ** power
if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#19. A series program: 1 4 9 16 25 36 and so on 
n = 10
for i in range(1,n+1):
    print(i*i,end = " ")

#20. Power of n starting with 1 3. 
n = int(input("Power of n starting with 1 3:"))
for i in range(1, n + 1):
    print(i ** 3)

#21. Find the factorial of n. 
num3 = int(input("Find the factorial of n:"))
fact = 1
for i in range(1,num3+1):
    fact *=i
print(fact)

#22. Find average of list of numbers entered through keyboard. 
list = [10,20,30,40,50,60]
total = 0
for i in list:
    total +=i
print(total / len(list))

#23.Take a number as input and check whether number is 
num = int(input("Enter a number as input and check whether number is :"))
print(type(num))

#24.calculate the value SUM = 1 + 4 – 9 + 16 – 25 + 36 – … for a given number. 
n = int(input("Enter the value SUM = 1 + 4 – 9 + 16 – 25 + 36 – … for a given number. :"))
total5 = 0
for i in range(1,n+1):
    if i % 2 == 0:
        total5 += i * i
    else:
        total5 -= i * i
print(total5)

#25.calculate the value SUM = 12+22+32+42+52+62+72+.. for a given number. 
n = int(input("Enter the value SUM = 12+22+32+42+52+62+72+.. for a given number:"))
sum1 = 0
for i in range(1,n+1):
    sum1 += i * 10 + 2
print(sum1) 

#27. calculate the value SUM = e1 +e2 +e3 +e4 +e5+… for a given number. 
import math
n = int(input("calculate the value SUM = e1 +e2 +e3 +e4 +e5+… for a given number:"))
total = 0
for i in range(1,n+1):
    total +=math.exp(i)
print(total)

#28.  calculate the value SUM = 1 + 2 + 6 + 24 + 120 + … for a given number. 
sum1 = int(input("calculate the value SUM = 1 + 2 + 6 + 24 + 120 + … for a given number:"))
total = 0
fact = 1
for i in range(1,n+1):
    fact *=i
    total +=fact
print(total)

#29. calculate the value SUM = 1 + 1/4 + 1/9 + 1/16 + 1/25 + for a given number. 
n = int(input("calculate the value SUM = 1 + 1/4 + 1/9 + 1/16 + 1/25 + for a given number:"))
total = 0
for i in range(1,n+1):
    total += ( 1 / i**2)
print(total)

#30. calculate the value SUM = 1 + 8 + 27 + 64 + … for a given number. 
n = int(input("calculate the value SUM = 1 + 8 + 27 + 64 + … for a given number:"))
total = 0
for i in range(1,n+1):
    total += i**3
print(total)

#31.To print multiplication table from 1×1 to 10×10. 
for i in range(1,11):
    for j in range(1,11):
        print(i,'*',j, "=" ,i*i )

#32.To compute the sum of the digits of a given positive integer number. 
pos_int = 1234565432
pos = str(pos_int)
total1 = 0
for i in pos:
    total1 +=int(i)
print(total1)

#33. To read any five real numbers and print the average value. 
total = 0
for i in range(5):
    num = float(input("enter the float nums"))
    total += num
print(total/5)

#34. To calculate the sum of first  N natural numbers. 
n = int(input("calculate the sum of first  N natural numbers"))
total2 = 0
for i in range(1,n+1):
    total2 += i
print(total2)

#35.To calculate the average of first N odd numbers. 
n = int(input("calculate the average of first N odd numbers:"))
total = 0
count = 0
for i in range(1,n+1):
    if i % 2 !=0:
        count +=1
        total += i 
print(total/count)


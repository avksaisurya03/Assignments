#While loop
#1.to display the Factorial of a number. 
num = 5
fact = 1
while num > 0:
    fact *= num
    num -=1
print("factorial:",fact)

#2. to reverse a word. 
word = "surya"
rev_word = ""
index = len(word) - 1
while index >=0:
    rev_word += word[index]
    index -=1
print("reversed a word:",rev_word)

#3.to reverse a number. 
num = 12345
result = 0
while num > 0:
    digit = num % 10 
    result = result * 10 + digit 
    num //= 10
print("reversed number:",result)

#4.to display the first 7 multiples of 7.
num = 7
count = 1
while count <=7:
    print("multiples of 7:",num * count)
    count +=1

#5. appends the square of each number to a new list.
num = 1
squares = []
while num <=10:
    squares.append(num ** 2)
    num +=1
print("squares of numbers from 1 to 10:",squares)

#6. to separate positive and negative number from a list. 
num = [1,-1,2,-2,3,-3]
pos = []
neg = []
index = 0
while index < len(num):
    if num[index] >=0:
        pos.append(num[index])
    else:
        neg.append(num[index])
    index +=1
print("positive numbers:",pos)  
print("negative numbers:",neg)

#7. a program that appends the type of elements from a list.
list1 = [1,"sai",True,10.20]
types = []
index = 0
while index < len(list1):
    types.append(type(list1[index]))
    index +=1
print("types of elements in the list:",types)

#8. to filter even and odd number from a list. 
list2  = [1,2,3,4,5,6]
even = []
odd = []
index = 0
while index < len(list2):
    if list2[index] % 2 == 0:
        even.append(list2[index])
    else:
        odd.append(list2[index])
    index +=1
print("even nums:",even)
print("odd nums:",odd)

#9. to fetch only even values from a dictionary. 
dict1 = {"a":1,"b":2,"c":3,"d":4}
even = []
for key in dict1:
    if dict1[key] % 2 == 0:
        even.append(dict1[key])
print("even values from the dictionary:",even)

#10.  to check the given string is a palindrome or not. 
name = "madam"
palin = ""
index = len(name) -1
while index >=0:
    palin += name[index]
    index -=1
print("palindrome") if name == palin else print("not a plaindrome")

#11. to check the given number is a prime or not.
num = 7
if num > 1:
    is_prime = True
    div = 2
    while div < int(num ** 0.5)+1:
        if num % div == 0:
            is_prime = False
            break
        div +=1
print("prime") if is_prime else print("not a prime")

#12. to print all prime numbers between 0 and user entered number. 
num = 20
i = 2
while i < num:
    is_prime = True
    div = 2
    while div < int(i ** 0.5)+1:
        if i % div == 0:
            is_prime = False
            break
        div +=1
    if is_prime:
        print(i, end=" ")
    i +=1

#13. the sum of all prime numbers between 0 and user entered number.
num = 20
total = 0
i = 2
while i < num:
    is_prime = True
    div = 2
    while div < int(i ** 0.5)+1:
        if i % div == 0:
            is_prime = False
            break
        div +=1
    if is_prime:
        total += i  
    i +=1
print("sum of prime numbers between 0 and",num,":",total)

#14. to calculate the product of all prime numbers between 0 and user entered number.
num = 20
product = 1
i = 2
while i < num:
    is_prime = True
    div = 2
    while div < int(i ** 0.5) + 1:
        if i % div == 0:
            is_prime = False
            break
        div += 1
    if is_prime:
        product *= i
    i += 1
print("product of prime numbers between 0 and", num, ":", product)

#15. Reverse the entered number by printing the remainder. 
num = int(input("enter number to reverse:"))
print("reversed number:",end=" ")
while num > 0:
    print(num % 10, end = "")
    num //=10

#16. Reverse the entered number. (Do not print the remainder) 
num = int(input("enter number to reverse:"))
rev = 0
while num > 0:
    rev = rev*10 + num % 10
    num //=10
print("reversed number:",rev)

#17.  Sum of each digit from a number. 
num = 123
total = 0
while num > 0:
    total += num % 10
    num //=10
print("sum of digits:",total)

#18. Check no. is Armstrong or not. 
num = 153
total = 0
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** len(str(num))
    temp //= 10
print("Armstrong number") if total == num else print("not an Armstrong number")

#19. A series program: 1 4 9 16 25 36 and so on 
num = 1
while num <=6:
    print(num ** 2, end=" ")
    num +=1

#20.Power of n starting with 1 3. 
n = 1
while n <=5:
    print(3 ** n, end = " ")
    n +=1

#21. Find the factorial of n.
n = 5
fact = 1
while n > 0:
    fact *= n
    n -=1
print("factorial:",fact)

#22. Find average of list of numbers entered through keyboard. 
list2 = [1,2,3,4,5]
total = 0
index = 0
while index < len(list2):
    total += list2[index]
    index +=1
print("avg:",total/len(list2))

#23.Take a number as input and check whether number is 
num = int(input("enter a number:"))
print("pos") if num > 0  else print("zero") if num < 0 else print("negative")

#24. calculate the value SUM = 1 + 4 – 9 + 16 – 25 + 36 – … for a given number. 
n = 6
total = 0
i = 1
while i <= n:
    if i % 2 == 0:
        total += i**2
    else:
        total -= i **2
    i +=1
print("sum:",total)

#25. Calculate the value SUM = 12+22+32+42+52+62+72+.. for a given number. 
n = 7
total = 0
i = 1
while i <=n:
    total += i**2 + 2
    i +=1
print("sum:",total)

#26.calculate the value SUM = x – x3/3! + x5/5! – x7/7! + x9/9! - for a given number. 
import math
x = 2
n = 9
total = 0
i = 1
while i <=n:
    if i % 4 == 1:
        total += x ** i / math.factorial(i)
    elif i % 4 == 3:
        total -= x ** i / math.factorial(i)
    i +=1
print("sum:",total)

#27.alculate the value SUM = e1 +e2 +e3 +e4 +e5+… for a given number. 
import math
n = 5
total = 0
i = 1
while i <=n:
    total += math.exp(i)
    i +=1
print("sum:",total)

#28.calculate the value SUM = 1 + 2 + 6 + 24 + 120 + … for a given number. 
num = 5 
total = 0
fact = i = 1
while i <= num:
    fact *=i
    total += fact
    i +=1
print("sum:",total)

#29. calculate the value SUM = 1 + 1/4 + 1/9 + 1/16 + 1/25 + for a given number.
n = 5
total = 0
i = 1 
while i <=n:
    total += 1 / i**2
    i +=1
print("sum:",total)

#30. calculate the value SUM = 1 + 8 + 27 + 64 + … for a given number.
n = 5
total = 0
i = 1
while i <= n :
    total += i**3
    i +=1
print("sum:",total)

#31. To print multiplication table from 1×1 to 10×10.
i = 1
while i <=10:
    j = 1
    while j <=10:
        print(i,"*",j,"=",i*j)
        j+=1
    i+=1

#32. To compute the sum of the digits of a given positive integer number.
numbers = int(input("Enter a positive integer:"))
total = 0
while numbers > 0:
    total += numbers % 10
    numbers //= 10
print("Sum of digits1:",total)

#33. To read any five real numbers and print the average value. 
real_nums = [1,2,3,4,5]
total = 0
count = 0
index = 0
while index < len(real_nums):
    total += real_nums[index]
    count +=1
    index +=1
print("average:",total/count)


#34. To calculate the sum of first  N natural numbers.
n = int(input("Enter the value of N:"))
total = 0
i = 1
while i <=n:
    total += i
    i+=1
print("Sum of first N natural numbers:",total)

#35. To calculate the average of first N odd numbers.
n = int(input("Enter the value of N:"))
total = 0
count = 0
i = 1
while i <=n:
    if i % 2 !=0:
        total +=i
        count +=1
    i+=1 
print("Average of first N odd numbers:",total/count)
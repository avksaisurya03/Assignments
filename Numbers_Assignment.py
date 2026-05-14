#1. Define a variable for storing your age and save your age into it.
age = 21
print(age)

#2. Define a variable for storing your name and save your name into it
name = "surya"
print(name)

#3. Define a variable for storing your height and save your height into it.
height1 = 64
print(height1)

#4. What is the value of the expression 2 * (3 + 4) ? 
res1 = 2 * (3 + 4)
print(res1)

#5. What is the value of the expression 2 * 3 + 4 ?
res2 =2 * 3 + 4
print(res2)

#6. What is the value of the expression 2 + 3 * 4 ?
res3 = 2 + 3 * 4
print(res3)

#7. What is the type of the result of the expression 1 + 2.0 + 3?
res4 = 1 + 2.0 + 3
print(type(res4))

#8. How can you truncate and round a floating-point number?
num1 = 7.77
print(int(num1))
print(round(num1))

#9. How can you convert an integer to a floating-point number?
num2 = 77
print(float(num2))

#10. How would you display an integer in octal, hexadecimal, or binary notation?
num3 = 77
print(oct(num3))
print(hex(num3))
print(bin(num3))

#11. How might you convert an octal, hexadecimal, or binary string to a plain integer?
print(int("25",8))
print(int("25",16))
print(int("101010",2))

#12.How to calculate the square of your values in different ways?
num4 = 10
print(num4 * num4)
print(num4 ** 2)
print(pow(num4,2))

#13.Python program to check whether the given number is even or not
num5 = 77
if num5 % 2 == 0:
    print("Even")
else:
    print("odd")

#14. Python program to convert the temperature in degree centigrade to Fahrenheit
celcius = 39
farenheit = (celcius * 9/5) + 32
print(farenheit)

#15.Python program to find the area of a triangle whose sides are given
a,b,c = 3,4,5
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)

#16. Python program to find out the average of a set of integers
num6 = [1,2,3,4,5]
avg = sum(num6) / len(num6)
print(avg)

#17. Python program to find the product of a set of real numbers
num7 = [7,7.77,77.77]
product = 1
for i in num7 :
    product *=i
print(product)

#18. Python program to find the circumference and area of a circle with a given radius
import math
r = 7
circumference = 2 * math.pi * r
area_of_circle = math.pi * r ** 2
print(circumference)
print(area_of_circle)

#19. Python program to check whether the given integer is a multiple of 5
num8 = 77
if num8 % 5 == 0:
    print("multiple of 5")
else:
    print("Not a multiple of 5")

#20. Python program to check whether the given integer is a multiple of both 5 and 7
num8 = 350035
if num8 % 5 == 0 and num8 % 7 == 0:
    print("multiple of both 5 and 7")
else:
    print("Not a multiple of both 5 and 7")

#21. Python program to find the average of 10 numbers using while loop
i = 0
total = 0
while i < 10:
    num = [10,20,30,40,50,60,70,80,90,100]
    total +=num[i]
    i +=1
avg = total / 10
print(avg)

#22.Python program to display the given integer in a reverse manner
num9 = 12345
reverse = 0
while num9 > 0:
    digit = num9 % 10
    reverse = reverse * 10 + digit
    num9 //=10
print(reverse)

#23. Python program to find the geometric mean of n numbers
num = [1,2,3,4,5]
product = 1
for i in num:
    product *= i
geometric_mean = product ** (1/len(num))
print(geometric_mean)

#24. Python program to find the sum of the digits of an integer using a while loop
num10 = 1234
total = 0
while num10 > 0:
    digit = num10 % 10
    total += digit 
    num10 //= 10
print(total)

#25. Python program to display all the multiples of 3 within the range 10 to 50
for i in range(10,51):
    if i % 3 == 0:
        print(i, end= ",")

#26. Python program to display all integers within the range 100-200 whose sum of digits is an even number
for i in range(100,201):
    total = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        total +=digit 
        temp //=10
    if total % 2 == 0:
        print(i, end=",")

#27.Python program to check whether the given integer is a prime number or not
import math
num11 = 77
if num11 < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2,int(math.sqrt(num11)+1)):
        if num11 % i == 0:
            is_prime = False
            break
    if is_prime:
        is_prime = True

#28. Python program to generate the prime numbers from 1 to N
N = 50 
for i in range(2, N+1):
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            break
    else:
        print(i, end=",")
    
#29. Python program to find the roots of a quadratic equation
import math 
a,b,c = 5,10,2
d = b**2 - 4*a*c
if d>0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
print(root1,root2)

#30. Python program to print the numbers from a given number n till 0 using recursion
def PN(n):
    if n <0:
        return None
    print(n)
    PN(n-1)
n = 10
PN(n,end=",")

#31. Python program to find the factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
num12 = 7
print(factorial(num12))


#1. The given number is odd or even. 
num = 100
if num % 2 == 0:
    print("even")
else:
    print("odd")

#2. The given number is positive or negative or zero.
num = 0
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("Zero")

#3. given number is of one digited or two digited or three digited or more than three digited
num = 101
if num < 9:
    print("one digited")
elif num < 99:
    print("two digited")
elif num < 999:
    print("three digited")
else:
    print("more than three digited")

#4. Entered number is smallest 4 digit number or not. 
num = 9000
if num == 1000:
    print("Smallest 4 digit number")
else:
    print("not a smallest 4 digit number")

#5.The given character is an uppercase letter or lowercase letter or a digit or a special character. 
s = "@#$%^&"
if s.isupper():
    print("Uppercase")
elif s.islower():
    print("Lowercase")
elif s.isdigit(): 
    print("digit")
else:
    print("special character")

#6. The given year is a leap year or not
year = 2026
if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
    print("Leap Year")
else:
    print("Not a Leap year")

#7.The given number is divisible by 5 or not. 
year1 = 5000
if year1 % 5 == 0:
    print("Divisible by 5")
else:
    print("Not a divisible by 5")

#8.Find maximum number out of given three numbers. 
a,b,c = 10,20,30
if a>b and a>c:
    print("maximum num is ",a)
elif b > c :
    print("maximum num is",b)
else:
    print("Maximum num is ",c)

#9. Find minimum number out of given three numbers.
a,b,c = 10,20,30
if a<b and a<c:
    print("minimum num is:",a)
elif b < c:
    print("minimum num is",b)
else:
    print("minimum num is:",c)

#10. Write a program that reads three positive numbers a, b, c and determines whether they can form the three sides of a triangle. eA = int(input())
a = int(input())
b = int(input())
c = int(input())
if a+b>c and b+c>a and a+c>b:
    print("Can form the 3 sides of a traingle")
else:
    print("cannot form the 3 sides of a traingle ")

#11. Whether the triangle will be an obtuse-angle, or a right-angle or an acute-angle triangle. 
a = int(input())
b = int(input())
c = int(input())
if a*a + b*b == c*c: 
    print("Right angled triangle")
elif a*a + b*b < c*c:
    print("Acute angled triangle")
else:
    print("Obtuse angled triangled")

#12.If the triangle is an acute angle triangle, determine further whether the triangle is equilateral, isosceles, or scalene. 
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or c == a:
    print("Isosceles triangle")
else:
    print("scalene triangle")

#13. 
product_code = int(input("Enter the product_code:"))
order_amount = int(input("Enter the order_amount::"))
discount = 0
if product_code == 1 and order_amount > 1000:
    discount = order_amount * 0.1
elif product_code == 2 and order_amount > 100:
    discount = order_amount * 0.05
elif product_code == 3 and order_amount > 500:
    discount = order_amount * 0.1
net = order_amount - discount
print(net)

#14.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = int(input())
x = int(input())
if x > k:
    result = a*x**3 - b*x**2 + c*x - d
elif  x == k: 
    result = 0
else:
    result = a*x**3 + b*x**2 - c*x +d
print(result)

#15.
n1 = int(input("Enter n1 num:"))
n2 = int(input("Enter n2 num:"))
opr = input("enter the math opera:")
if opr == '+':
    print(n1+n2)
elif opr == '-':
    print(n1 - n2)
elif opr == '*':
    print(n1 * n2)
elif opr == '%':
    print(n1 % n2)
elif opr == '/':
    print(n1 / n2)
else:
    print("Invalid operator")

#16. 
past = int(input("Enter past meter reading:"))
current = int(input("current meter reading:")) 
units = current - past 
if units <= 100:
    charges = 0.5 * units 
elif units <= 200 and units >= 101:
    charges = 50 + (units-100) * 1
elif units <= 300 and units >= 201:
    charges =  150 + (units-200) * 1.5
elif  units > 300:
    charges = 300 + (units - 300 ) * 2
print(units)
print(charges)

#17.
amount = float(input("Enter amount: "))
code = input("Enter item code: ")
discount = 0
if amount <= 100:
    if code == "sh":
        discount = 0
    elif code == "p":
        discount = 3
    elif code == "sht":
        discount = 5
elif amount <= 200:
    if code == "sh":
        discount = 5
    elif code == "p":
        discount = 8
    elif code == "sht":
        discount = 10
elif amount <= 300:
    if code == "sh":
        discount = 10
    elif code == "p":
        discount = 12
    elif code == "sht":
        discount = 15
else:
    if code == "sh":
        discount = 18
    elif code == "p":
        discount = 20
    elif code == "sht":
        discount = 22
net = amount - (amount * discount / 100)
print(net)

#18. 
category = input("Enter the category:")
units = int(input("Enter the units:"))
bill = 0
if category == "Commercial":
    if units <= 5000:
        bill = 1500
    elif units <=10000:
        bill = 1500 +(units - 5000) * 0.25
    elif units <=20000:
        bill = 2750 +(units - 10000) * 0.23
    else:
        bill = 5050 + (units - 20000) * 0.2
elif category == "Institutional":
    if units <= 5000:
        bill = 1800
    elif units <= 10000:
        bill = 1800 + (units - 5000) * 0.3
    elif units <= 20000:
        bill = 3300 + (units- 10000) * 0.28
    else:
        bill = 6100 + (units- 10000) * 0.28
elif category == "Domestic":
    if units <=100:
        bill = 75
    elif units <= 200:
        bill = 75 + (units - 100) * 1.25
    elif units <=400:
        bill = 200 + (units - 200) * 2.0
    else:
        bill = 600 +( units - 400) * 2.5
print("Bill:",bill)

#19. 
distance = int(input("Enter the dist:"))
if distance <= 50 :
    fare = distance * 8
elif distance <=100:
    fare = distance * 10
else:
    fare = distance * 12
print("fare:",fare)

#20. 
booking_type = input("Enter the booking type:")
seat = input("Enter the typeof_seats:")
amount = 0
if seat == "Ordinary":
    amount = 2500
elif seat == "Pavillion":
    amount = 3500
elif seat == "Upper Pavillion":
    amount = 4500
elif seat == "Commentary Box":
    amount = 6000
elif seat == "VIP":
    amount = 8000
discount = 0
if booking_type == "Online Booking":
    discount = 10
elif booking_type == "Advance Booking":
    discount = 8
elif booking_type == "match day":
    discount = 0
tct_amt = amount - (amount * (discount/ 100))
print(tct_amt)

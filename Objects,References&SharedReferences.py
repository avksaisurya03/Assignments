#1. to verify that built-in functions, user-defined functions, and types are objects with IDs.
print(id(len))
def abc():
    return "HI"
print(id(abc))
print(id(int))
print(id(str))
print(id(float))

#2.Python program to demonstrate the difference between the == operator (value equality) and the is operator(identity comparison).
a = 10000
b = 10000
c = b
print(a==b)
print(a is b)
print(b == c )
print(b is c)

#3. Python program to show shared reference behavior by modifying a list through two different variable names.
lst1 = [1,2,3]
lst2 = lst1
lst1.append(4)
print(lst1)
print(lst2)

#4. to show mutable vs immutable object behavior by trying to modify a list element vs a string character.
lst3 = [1,2,3]
lst3[0] = 200
print(lst3)
s = "Surya"
s = "p" + s[1:]
print(s)

#5. to check memory address caching behavior of integers in the range -5 to 256
a = 256
b = 256
print(a is b )
print(id(a))
print(id(b))

#6. to demonstrate shallow copy vs deep copy of a nested list using the copy module.
import copy
lst1 = [[1,2],[3,4]]
shallow = copy.copy(lst1)
deep = copy.deepcopy(lst1)
lst1[0][1] = 200
print(lst1)
print(shallow) 
print(deep)

#7. to show the effect of passing mutable vs immutable objects as arguments to a function
def numb(num):
    num +=10
    print(num)
def lst1(n):
    n.append(100)

num = 10
numb(num)
print(num)
lst = [1,2,3]
lst1(lst)
print(lst)


#8. to demonstrate the unexpected behavior of using a mutable object as a default argument.
def add_item(item, lst=[]):
    lst.append(item)
    return lst
print(add_item(1))
print(add_item(2))
print(add_item(3))

#9. to demonstrate that list slicing creates a new list object with shared elements.
lst7 = [1,2,[3,4]]
lst8 = lst7[:] 
print(lst7 is lst8)
lst7[2][0] = 100
print(lst7)
print(lst8)

#10.Python program to verify string interning for identical short strings
name1 = "Surya"
name2 = "Surya"
print(name1 is name2)

#11.Python program to demonstrate value vs identity checks for different empty data structures (list, tuple, dict).
lst5 = [1,2]
lst6 = [1,2]
print(lst5 is lst6)
print(lst5 == lst6)
tup1 = ()
tup2 = ()
print(tup1 is tup2)
print(tup1 == tup2)
s = {}
s1 = {}
print(s is s1)
print(s == s1)

#12.to show how modifying an element of a tuple containing a list behaves.
tup3 = ([1,2],3)
tup3[0].append(4)
print(tup3)

#13. Python program to show that a dictionary's keys must be immutable objects, while its values can be mutable 
dict1 = {1:[1,2]}
dict1[1].append(3)
print(dict1)

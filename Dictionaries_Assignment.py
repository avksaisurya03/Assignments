#Dictionaries Assignment 
#1. Sort Dictionaries by Key or Value 
dict1 = {'b':2,'a':1,'c':3}
print(dict(sorted(dict1.items())))

#2. Handling missing keys in Python dictionaries 
dict2 = {'b':2,'a':1,'c':3}
print(dict2.get('f',"Key Not Found")) #to access the data we use get 

#3. to find the sum of all items in a dictionary 
dict3 = {'a':100,'b':10,'c':30}
print(sum(dict3.values()))

#4.to find the size of a Dictionary 
dict4 =  {'a':1,'b':2,'c':3}
print(len(dict4))

#5. to Merge two Dictionaries 
dict5 = {'a':1,'b':2,'c':3}
dict6 = {'d':4,'e':5}
dict5.update(dict6)
print(dict5)

#6.

#7. to remove a key from dictionary 
dict7 = {'a':1,'b':2,'c':3}
dict7.pop('c')   #we use pop instead of del operator 
print(dict7)     #because in pop if the element is not exist , it will not show error unlike del operator

#8. replace value of a key in a Dictionary 
dict = {'a':1,'b':2,'c':3}
dict['c'] = 4
print(dict)

#9.to remove all duplicates values in a given dictionary 
dict11 = {'a':1,'b':2,'c':3,'d':4,'c':4}
result = {}
values = []
for k,v in dict11.items():
    if v not in values:
        result[k] = v
        values.append(v)
print(result)

#10. to create a dictionary with keys are unique elements of string and values as frequency of the char in the string
name = "mahesh"
dict10= {}
for i in set(name):
    dict10[i] = name.count(i)
print(dict10)  

#11.to calculate the mean of Values in a Dictionary
dict8 = {'a':100,'b':200,'c':300}
a = sum(dict8.values())/ len(dict8)
print(a)

#12.find the Maximum record value's key in a dictionary
dict9 = {'a':100,'b':200,'c':300}
print(max(dict9,key =dict9.get))

#13. Extract values of particular key in nested dictionaries
dict11 = {
    'a' :{'x':10},
    'b' :{'x':20},
    'c' :{'x':30}
 }
for i in dict11.values():
    result.append(i['x'])
print(result)
#let's practice 
# what is string? its a sequence of characters 
# name = "janvi"
# lastname = "nandwana"
# print("my name is :-", name)
# print("my lastname is :-", lastname)/

# age = 10
# print("data type of age", type(age))
# y = 29
# print("data type of y", type(y))

# print("data type of name", type(name))

#indexing and slicing of a string in python
# print(name[4]) 
# print(lastname[0:5])
# print(name[-3]) 
# print(lastname[-6])
# print("length of my name :-",len(name))
# print("length of my lastname :-",len(lastname))
#addition of two strings
# print(name + lastname)
# print(name , lastname)
# print(name + " "+ lastname)
#DOUBT
# result = name +  lastname
# # print(result)
# #DOUBT
# #length of result
# print("length of my result :-",len(result))

#>>>>>>>>using uppercase and lowercase functions
# name = "janvi"
# print(name.upper())
# upper_case = name.upper()
# print(upper_case)
# print(name.capitalize())
# print(name.title())
#capitalise and title capitalises the first letter of our sentences when we dont kmow what are our sentences
# python janvipractice.py

# # print(name.lower())
# lower_case = name.lower()
# print(lower_case)
#DOUBT
# print(name.casefold())
# print(name.lower())
#DOUBT
#sequence types :- strings, lists, tuple
#we did strings 
#difference between list and arrays are that arrays are homogenous while lists are heterogenous 
# arrays are alawys ordered and doesnt allow dups,and contains the sane data type
#lists are collection of items which are unordered, takes anything as value unlike arrays,can contain many diffferent datatypes, allows dups as well
#we doing lists now
#lists and arrays are always in sqaure brackets whereas tuple is always in parenthesis
# lst =  [2,4,6,6,5,5,4,"Janvi",]
#indexing slicing length datatype 
# print("length of my list", len(lst))
# print("datatype :-", type(lst))
# print(lst[4])
# print(lst[0:3])
#main function in lst are append(), insert(), remove(), pop()
# lst.append(10000)
# print(lst)
# lst.insert(4,44.4)
# print(lst)
#DOUBT
# print(lst.count(4))
#DOUBT
# lst.append(444)
# print(lst)
# lst.insert(3,0.4)
# print(lst)
#doubt
# lst.remove(4)
# print(lst)
# lst.pop(4)
# print(lst)
# lst =  [2,4,6,6,5,5,4,"Janvi"]

# lst.pop(3)
# print(lst)

# lst.pop(2)
# print(lst)
#  lst.copy()
# print(lst)

# lst.extend([3,4])
# print(lst)

#list..

# lst.append(1000)
# print(lst)
# lst.extend(["yogesh"])
# print(lst)
# lst.remove(3)
# print(lst)
#doubt
# lst.pop(5)
# print(lst)
#doubt
#first question
# tpl = (1,2,3,[1,2,"hello"])
# var = tpl [3]
# print (var[2])

# #second question
# stg = [1,2,3,'hello',((["hello"]))]
# stgg = stg[4]
# print(stgg[0])

# lst = [1,2,3,3,4,4,4,"hello"]
# lst.append(705)
# lst.copy()
# print(lst.count(4))
# lst.extend(["janvi","yogesh"])
# lst.insert(0,"deepak")
# print(lst[7])
# lst.pop()
# lst.pop(6)
# lst.remove(4)
# lst.remove(2)
# lst.remove(3)
# lst.reverse()

# tpl = (1,3,3,5,7,"hello")
#typecasting 
#converting the tuple in list
# lst = [1,3,3,5,7,"hello"]
# lst.append("yogesh")
# print(lst)
# student  = {"name": "janvi",
# "roll no.":"18",
# "age":"20"}
# print(student)
# age = int(input("enter your age"))
# print(age)
# student  = {"name": "janvi",
# "roll no.":"18",
# "age":"20"}
# student.update({"name":"yogesh"})
# print(student)
# student.copy()
# print(student)

#setssss
# sat = {1,2,3,4,"janvi"}
# sats  = {1,2,3,"hello"}
# print(sat)
# print("length of my set :-", len(sat))
# print("data type of my set :-", type(sat))
#indexing and slicing not possible in sets
# print(sat[0])
# print(sat[0:4])cls
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# union_set = set1.union(set2)
# print(union_set)
difference_set = set1.difference(set2)
print(difference_set)
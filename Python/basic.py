# name = "Janvi"
# lastname = "Nandwana"
# print("my name is :-",name)
# print("lastname is :-",lastname)
#name = "janvi"
# lastname = "nandwana"
# print( name +" " + lastname )
# name = "janvi"
# lastname = "nandwana"

# upper_case=name.upper()
# print("upper case :- ", upper_case)
# name = "JANVI"
# lower_case=name.lower()
# print("lower case :- ", lower_case)

# name = "JAANVI"
# print(name.title()).
# print(name.casefold())
# output =name.casefold(), lower ()
# print(output)












# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>...list 
# lst = [2,4,6,8,10,12,14,16]
# print("this is my first list :-", lst)
# print("type of list :-",type(lst))
# print("length of my list :-", len(lst))
# #indexing and slicing
# print(lst[0])
# print(lst[2])
# print(lst[4])
# print(lst[0:7])
lst = [1,2,3,4,4,5,5,5,6]
#lst.append(1000) #append is for adding any no. at the last of a list
#print(lst)
#lst.insert(2,"hello") #insert is for inserting any no. thing at a specific position
# print(lst.count(5)) #count is for counting of any desired no. within the list and count can be directly printed

# (lst.remove(5))
# print(lst)#remove removes the only and first desired no. within the list
#lst.pop()#pop removes the last element by default if we dont specify our
#  desired position otherwise it removes the one we want to remove by specifying the position and we can pop or remove a specific element from a specific position too
#lst.pop(5)
#print(lst)
#lst.clear()# it clears the whole list out leaving the list empty
#lst.copy()#copy is for coping the list 
#lst.extend([3,5,7])#extend is for extending the list by adding our desired no. they can be any but by default they will be added at last


# >>>>>>>>>>>>>>>>>..tuple


# tpl = (1,2,3,4,5,6,6, "hello", "hii")
# print("my first tuple is:", tpl)
# print("length of tuple:",len(tpl))
# print("type of my tuple:, type(tpl))
# print(tpl[4])
# print(tpl[0:6]
#(tpl.count(6))
# var =  1,2,3,4
# print( "this is my first tuple", var)
# a,b= 2,3
# print(a)
# print(b)
#by default when we give any variable inside using normal parenthesis it is a tuple 
#list always in sqaure brackets and tuple always in parenthesis(small brackets)
#there are only two count and index available in tuple because it has property that we cant modify a tuple


#>>>>>>>>>>>>>>..membership in tuple
# tpl = (1,2,3,4)
# print(3 in tpl)
# print(5 in tpl)

#typecasting in tuple
#means coversion of a a datatype into another datatype like list to tuple so that we can modify them and convert them into same as before
# tpl = (1,3,5,7)
# print("this is tuple", tpl)
# print("type of tuple",type(tpl))
# lst = [1,2,3,4]
# print("this is list",lst)
# print("type of list",type(lst) )

# lst.append(1000)
# print("this is list",lst)

# tppl = tuple(lst)
# print("this is tuple", tppl)
#>>>>>>>>>>>>>>>>>>>>dictionary..
# student = {"name": "janvi",
# "class":"3rd year",
# "age": "20",
# "address":"Kota"}
# print(" my first dictionary :-", student)
# print ("length of my dict :-", len(student))
# print("data type of my dict :-", type(student))
# print(student["name"])
# print(student["age"])
# print("total keys", student.keys())
# print("total value", student.values())
# print("total items", student.items())
#we made our first dictionary and it contains key value pairs and then found its length and type and then we found total no. of keys and values and items and typecasting in it too 
# #when  taking input from user using input() by default it stores in string but using typecasting we can change it to our desired datatype

# student["name"] = "Govind"
# student["age"] = "22"
# print(student)
# age = input("enter your age")
# print("data type of age :-", type(age))
# print(age)
#


# name = input("enter your age:-")
# print("data type of age :-", type(age))
# print(age)
# print(student[name])

### copy and deep copy 
# update function 
# print(student.get('age'))

# student = {"name": ["janvi", "janvi"],
# "class":"5rd year",
# "age": "20",
# "address":"Kota",
# "class":"4rd year"}
# student['name'][1]="Govind"
# print(student['name'][1])
# print(student)

# student.

# pin= input("enter your pin:-")

# print("your pin ", pin)
# num1 =int(input("enter number 1 "))
# num2 =int(input("enter number 2 "))
# print(num1+num2)
#>>>>>>>>>>>>>sets..
sat = {1,2,4,3,"hello"}
# print('length of my set', len(sat))
# print('data type of my set :-', type(sat))

# print(sat[0])
# sat=list(sat)
# print(sat[0])
# sat.remove(2)
# print(sat)



# sat.remove(5)
# print(sat)
# sat.discard(5)
# print(sat)
#operators

#variable rules
#a = 10 is possible
# 10 = 20 is not possible
#_a = 20, __a = 25 are two diff. variables
#age = 20, AGE = 21 , Age = 22 are three diff. variables
#print = 20 ia not possible (python keywords not used as variables)
#$,%,^,& can't be used as variable

# print(5+10)
#>>>>>>>string..



  
# first_name=input("Enter Your First Name : ")
# last_name=input("Enter Your Last name : ")

# print(first_name[::-1],last_name[::-1])


#Wap

# age=int(input("Enter age : "))
# year=2024-age
# print("You were Born in ",year)

# print('You will Turn 100 in ', year+100)

#wap
# import string
# lowers=string.ascii_lowercase
# uppers=string.ascii_uppercase

# va=input("enter an alphabet : ")
# if va in lowers:
#     print('You entered lower character ')
# elif va in uppers:
#     print("you enterd upper character ")
# else:
#     print("Invalid Alphabet ! Are You an idiot")


# # wap 
# string1="I AM EATING AN APPLE"
# vowels=['a','e','i','o','u','A','E','I','O','U']
# for i in range(len(string1)):
#     if string1[i] not in vowels:
#         print(string1[i])

# ind=0
# while(ind<len(string1)):
#     if string1[ind] not in ['a','e','i','o','u','A','E','I','O','U']:
#         print(string1[ind])
#     ind+=1

# wap

# a,b=input("Enter Two Numbers ").split()
# c=int(a)+int(b)
# print(c)

# wap

# s=input("enter name roll_no and age: ")
# name,roll_no,age=s.split()
# print("Your Name is : ",name)
# print("Your Age is : ",age)
# print("Your Roll Number is : ",roll_no)

# wap 

# stringsss="ONE*TWO*THREE*FOUR*FIVE"
# splitted=stringsss.split("*",3)
# print(splitted)

# wap
# list1=['a','b','c','d','e']
# list2=[1,2,3,4,5]

# for n in list1:
#     print(n)
#     for m in list2:
#         print(m)


# wap

# * * *
# * * *
# * * *


# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print("\n")

#wap
"""

*
**
***
****

"""
# star='*'

# for i in range(1):
#     for j in range(5):
#         print(star*j)
#     print("\n")



#wap 
"""

****
***
**
*

"""

# star='*'
# for i in range(1):
#     for j in range(5,1,-1):
#         print(star*j)
#     print('\n')


# wap NUmber guessing game
# import random
# numbers=[0,1,2,3,4,5,6,7,8,9,10]
# correct=random.choice(numbers)
# while True:
#     guessed=int(input("Enter A Guess Number 0 --> 10 : "))
#     if guessed==correct:
#         print("You Got It Right ")
#     elif guessed<correct:
#         print("Too Low number guessed")
#     elif guessed>correct:
#         print("Too High Number Guessed")
#     else:
#         print("Invalid Choice Try Again ")
#         break

# wap Head Tails Game
# manipulating game so user never wins 
# import random
# choice=['head','tail']
# selected=random.choice(choice)
# print("Actual Value is ",selected)


# user_input=input("select your choice head or tail : ").lower()
# if user_input==selected:
#     if selected=="head":
#         selected="tail"
#     elif selected =="tail":
#         selected="head"
#         print("You Loose! ")
# else:
#     print("You loose")


# WAP

# lis=[1,2,3,4,5,6,7]
# for i in range(len(lis)-1,-1,-1):
#     print(lis[i])

# wap Modify the list

# liss=["apple","orange","mango"]
# liss[1]="banana"
# liss.insert(1,"banana")
# liss.append("Tomato")

# print(liss)


#  Wap 

# full_name=input("enter your name : ")
# mv=full_name.split()
# print(full_name)


# wap

# numbers=input("enter numbers seperated by spaces : ")
# numbers=numbers.split()
# sum=0
# for val in numbers:
#     sum+= int(val)
#     print(int(val),": is real value"," Added(C.F) : ",sum)


# # wap 
# lists=[x**2 for x in range(1,51)]
# print(lists)

# wap
# vowels=['a','e','i','o','u']
# sentance="ilovecoding"
# listed=[char if char not in vowels else "" for char in sentance ]
# strr=""
# for v in listed:
#     if v==" ":
#         pass
#     else:
#         strr+=v
# print(strr)


#2nd method
# def remove_vowels(statement):
#     for i in range(len(statement)):
#         if statement[i] in vowels:
#             pass
#         else:
#             print(statement[i],end='')
# remove_vowels(sentance)


# # wap pack unpack
# a=1,2,3,4   # pack
# print(a)
# x,y,z,d=a # unpack
# print("x : ",x)
# print("y : ",y)
# print("z : ",z)
# print("d : ",d)

# wap
# stringg="Feroz"
# print(min(stringg))


# ord used for unicode values
# print(ord("A"))

# chr used to make alphabets and symbols from unicodes

# print(chr(97))


# wap

# l1=['T','H','I','S', ' ', 'I','S']
# stt="".join(l1)
# print(stt)

#wap   # .format()
# print("{name} is my name , and {age} is my age ".format(name="feroz",age=21))


# wap
# def absolute(num):
#     if num<0:
#         return -num
#     else:
#         return num
# print(absolute(-22))

#wap

# def nums(*a):
#     multed=1
#     for i in a :
#         multed*=i
#     return multed

# print(nums(10,20,2))


# # wap
# def sentance(*sentances):
#     for sentanc in sentances:
#         return max(sentances)
        

# print(sentance("I AM A GIRL","I AM A BOY"))

# wap
# def foo(x,y):
#     global a 
#     a=42  
#     x,y=y,x
#     b=33
#     b=17
#     c=100
#     print(a,b,x,y)

# a,b,x,y=1,15,3,4
# foo(17,4) # 42 17 4 17
# print(a,b,x,y)


# Lambda Fucntions are anonymous functions 

# print((lambda a,b:a+b)(12,22))

# other way

# _fxn=lambda a,b:a+b
# call=_fxn(10,20)
# print(call)

# wap 
# square=lambda a,b:[a**2,b**2]
# print(square(2,2))

# wap
# strr=input("Enter A String : ")
# print((lambda string:string[0:3])(strr))


#wap
# to_be_passed=int(input("enter Number To check: "))
# checker=lambda flag:flag%2==0
# print(checker(to_be_passed))

#wap
p1=int(input("enter first param: "))
p2=int(input("enter second param: "))

return_gateway=lambda p1,p2:[p1 if p1>p2 else p2]
print(return_gateway(p1,p2)[0])
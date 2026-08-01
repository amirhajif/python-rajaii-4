
# def multiply5(n):
#     print(n*5)

# print(multiply5(6))

# def m5(n):
#     return n*5
# print(m5(6))

# result=m5(6)
# print(result)

# m5 = lambda n:n*5

# print(m5(6))

# rectangleArea = lambda tol,arz:tol*arz
# print(rectangleArea(6,4))


# def isEven(n):
#     # if n%2==0:
#     #     return True
#     # else:
#     #     return False

#     return n%2==0


# # ie = lambda n:n%2==0

# numbers = [1,2,3,4,5,6]

# pow2Numbers = []

# for number in numbers:
#     pow2Numbers.append(number**2)

# print(pow2Numbers)


# def m2(n):
#     return n**2

# newNumbers = list(map(lambda number:number**2,numbers))
# print(newNumbers)

# import functions as f

# from functions import sayHello as SH,sayBye as SB

# f.sayBye()
# f.sayHello()
# SH()

# SB()

# STANDARD MODULE
# import math

# print(math.sqrt(16))

# import modules.functions
# import time

# print("welcome to the class please wait....")
# time.sleep(3)
# print("heloooo")

# name = "amir"
# print(type(name))

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return f"stunde name is {self.name} and  {self.age} year`s old with score: {self.score} "



st = Student("amir",25,20)
# print(st.score) 
print(st)

st2 = Student("reza",18,17)
print(st2)

# for i in range(0,5):
#     print("hello")

# i=0
# while i<5:
#     print("hello")
#     i+=1

# n = int(input("please enter n: "))
# sum=0
# while n>0:
#     # sum = sum + (n%10)
#     sum += n%10
#     # n = n//10
#     n//=10

# print(sum)


# 156 ---> 651

# n= int(input("please enter number: "))
# rev=0
# while n>0:
#     rev = (rev*10) + (n%10)
#     n=n//10

# print(rev)


# palindrome number
# 121 ---> 121
# n= int(input("please enter number: "))
# rev=0
# baseN = n
# while n>0:
#     rev = (rev*10) + (n%10)
#     n=n//10

# if baseN==rev:
#     print("palindrome")
# else:
#     print("not-palindrome")


# sum = 0
# count = 0
# while True:
#     score = int(input("please enter score: "))
#     sum+=score
#     count+=1

#     option = input("do you want continue?y/n ")
#     if option=="n":
#         break

# print(sum/count)

# Collection
"""
1-List + []
2-Tuple + ()
3-Dictionary + {}
4-set + {}
"""

# salaries = (1000,1500,2000,3000)
# print(salaries[1])
# for salary in salaries:
#     print(salary)

user = {
    "username":"amir",
    "password":"amir123",
    "age":25,
    "isProgrammer":True,
    "programmingLanguages":["python","c#","js"]
}

print(user["password"])

# users =["amir","reza","ali","ahmad"]

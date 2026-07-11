# scores = [20,12,14,19,8,12,3,4,9,12]
# names = ["amir","reza","jafar"]
# print(type(scores))
# print(scores)
# print(scores[9])

# users = ["amir","ali","reeza","mohammad","armin"]

# # update
# users[2] = "reza"
# print(users)

# # append
# users.append("arsham")
# print(users)

# # insert
# users.insert(1,"arsam")
# print(users)

# # del
# del users[1]
# print(users)

# # pop
# popedItem = users.pop(2)
# print(users)
# print(popedItem)

# # pop - last item
# popedItem2 = users.pop()
# print(users)
# print(popedItem2)

# # remove
# users.append("mohammad")
# print(users)

# users.remove("mohammad")
# print(users)

# SORT
# numbers = [10,12,2,19,3,4,8,12]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# SORTED
# sortedList = sorted(numbers)
# print(sortedList)
# print(numbers)

# REVERSE
# numbers.reverse()
# print(numbers)

# REVERSED
# reversedList = list(reversed(numbers))
# print(reversedList)
# print(numbers)

# numbers = [10,12,2,19,3,4,8,12]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sum(numbers)/len(numbers))

# carsaleCars = ["benz","bmw","prado","lexus"]
# myCars = carsaleCars[:]

# myCars.append("haima")
# carsaleCars.append("prosche")

# print(myCars)
# print(carsaleCars)



# CONDITIONS
# score = int(input("pelase enter score: "))
# if score > 10:
#     print("pass")
# else:
#     print("fail")


number1 = int(input("please enter number1: "))
number2 = int(input("please enter number2: "))

# if number1 == number2:
#     print("Equal")
# else:
#     print("not-equal")


# if number1 != number2:
#     print("not-Equal")
# else:
#     print("equal")

# number = int(input("please enter number: "))
# if number>0:
#     print("+")
# elif number==0:
#     print("zero")
# else:
#     print("-")

username = "amir"

users = ["jafar","ahmad","reza","amir"]

if username in users:
    print("login")
else:
    print("cant-login")

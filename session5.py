# user = {
#     "username":"amir",
#     "password":"amir123",
#     "age":25,
#     "isProgrammer":True,
#     "programmingLanguages":["python","c#","js"]
# }

# print(user["password"])

# users =["amir","reza","ali","ahmad"]


# user["password"]="123amir"
# print(user)

# user["nationalCode"]=205
# print(user)

# print(user["fatherName"])

# print(user.get("fatherName","the key not exist"))

# del user["programmingLanguages"]
# print(user)

# user.clear()
# print(user)


# users = [
#     {
#         "username":"amir",
#         "password":"amir123",
#         "age":25
#     },
#     {
#         "username":"ali",
#         "password":"a123",
#         "age":25
#     },
# ]

# user = {
#     "username":"amir",
#     "password":"amir123",
#     "age":"25"
# }

# users.append(user)
# print(users)


# print(user.items())
# [('username', 'amir'), ('password', 'amir123'), ('age', 25)]

# key,value = ('username', 'amir')
# print(key)
# print(value)

# for key,value in user.items():
#     print(f"{key}--->{value}") 

# print(user.keys())
# for key in user.keys():
#     print(key)

# print(user.values())
# for value in user.values():
#     value = value + " test"

# print(user)


# students = {
#     "mohammad":20,
#     "reza":18,
#     "amir":19
# }

"""
amir ---> 19
mohammad ---> 20
reza ----> 18
"""

# for key in sorted(students.keys()):
#     print(f"{key}--->{students[key]}")


# sentence = input("please enter sentence: ")

# lettersCount={}

# for letter in sentence:
#     lettersCount[letter] = lettersCount.get(letter,0) + 1 


# print(lettersCount)


# SET

# cars = {"bmw","benz","prado"}
# print(cars)
# cars[1] = "lambo"
# print(cars)

# for car in cars:
#     print(car)

# cars.add("pego")
# print(cars)


cars = {"bmw","benz","prado"}
carsaleCars = {"lambo","toyota","bmw"}

# cars.update(carsaleCars)
# print(cars)

# allCars = cars.union(carsaleCars)
# print(allCars)
# print(cars)

# cars.intersection_update(carsaleCars)
# print(cars)

# sameCars = cars.intersection(carsaleCars)
# print(sameCars)
# print(cars)

cars.symmetric_difference_update(carsaleCars)
print(cars)

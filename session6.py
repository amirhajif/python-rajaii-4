def sayHello(firstName="amirhossein",lastName="hajitabar",nationality="Iran"):
    return f"hello {firstName} {lastName} and from {nationality}"

def factoriel(n):
    sum=1
    for i in range(1,n+1):
        sum = sum*i    
    return sum


def sumFromZero(n):
    if n==0:
        return 0
    else:
        return n+sumFromZero(n-1)

def factoriel(n):
    if n==1:
        return 1
    else:
        return n*factoriel(n-1)

def introduceFoods(*foods):
    for food in foods:
        print(food)

def restaurantFoods(**foods):
    # print(foods)
    for key,value in foods.items():
        print(f"{key} ----> {value}")

# introduceFoods("burger","pizza","salad")
# ('burger', 'pizza', 'salad')
restaurantFoods(burger = 2000,pizza=3000,salad=3500)
# {'burger': 2000, 'pizza': 3000, 'salad': 3500}

# def greet(name):
#     print(f"hello {name}")

# greet("amir hossein")

# fact = factoriel(5)
# print(fact)


# print(sayHello())

# message = sayHello("amirhossein","hajitabar")
# print(message)

# greet = sayHello(lastName="hajitabar",nationality="Iran",firstName="amirhossein")
# print(greet)

# message = sayHello(nationality="Iraq")
# print(message)

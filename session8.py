class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return f"stunde name is {self.name} and  {self.age} year`s old with score: {self.score} "
    

# st = Student("amir",25,20)
# # print(st.score) 
# print(st)

# st2 = Student("reza",18,17)
# print(st2)


# ENCAPSULATION + METHOD
class Rectangle:
    def __init__(self,tol,arz):
        self.tol = tol
        self.arz = arz
    
    def __str__(self):
        return f" rectangle tol = {self.tol} rectangle arz= {self.arz}"
    
    def area(self):
        return self.tol*self.arz
    
    def env(self):
        return (self.tol+self.arz)*2
    
    # getter
    def getTol(self):
        return self.tol
    # setter
    def setTol(self,tol):
        self.tol = tol
    
    # getter
    def getArz(self):
        return self.arz
    # setter
    def setArz(self,arz):
        self.arz=arz
    

# rect = Rectangle(8,6)
# # print(rect)
# # set
# rect.setTol(12)
# rect.setArz(8)
# # get
# print(rect.getTol()*rect.getArz())
# # print(rect.area())
# # print(rect.env())


# INHERITANCE

class Person:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country

    def getName(self):
        return self.name
    def setName(self,name):
        self.name= name
    
    def getAge(self):
        return self.age
    def setAge(self,age):
        self.age= age
    
    def getCountry(self):
        return self.country
    def setCountry(self,country):
        self.country= country


class Employee(Person):
    def __init__(self,name,age,country,salary):
        super().__init__(name,age,country)
        self.salary = salary

    def getSalary(self):
        return self.salary
    def setSalary(self,salary):
        self.salary= salary    

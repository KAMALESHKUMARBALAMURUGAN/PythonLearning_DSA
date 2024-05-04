"""     #function definition and function call
def sum():
    no1= int(input("a= "))
    no2= int(input("b= "))
    result= no1+no2
    return result
answer= sum()
print("sum of two numbers =",answer)
"""


"""     #class and objects
1. create a class called laptop and create a following variables and functions 
variables  => Price, Processor, RAM
Create object HP, DELL, LENOVO
"""


"""     #Without constructor
class laptop:
    Price= ""
    Processor = ""
    RAM =""

HP= laptop()
DELL=laptop()
LENOVO = laptop()

HP.price =40000
HP.Processor= "i5"
HP.RAM= "2GB"

print(HP.price)
print(HP.Processor)
print(HP.RAM)
"""


"""     #Class With Constructor
class laptop:
    def __init__(self):
        self.price = 0
        self.processor =""
    def printdis(self):
        print(self.price)
        print(self.processor)

hp= laptop()
hp.price = 15000
hp.processor = "i5"

dell= laptop()
dell.price = 50000
dell.processor = "i5"

hp.printdis()
dell.printdis()
    """


"""     #"pass" is used to create empty class
class kamal:
    pass
    
    """

"""     #Example for class (Create a class called "Fruit",create a variable called color using __init__method, create a object called apple "Pass the color variable as a parameter through object")
class Fruit:
    def __init__(self,color,taste):
        self.color= color
        self.taste=taste
    
    def display(self):
        print("color of ",self,"is ",self.color)
        print("taste of ",self,"is ",self.taste)
    
apple= Fruit("red","Sweet")
apple.display()
"""


#create a class called calculator, create two variables called a and b. create a function called add, sub, mul, div and all functions should take 2 variables as a parameter. pass the a and b through object()

class calculator:
    def __init__(self,no1,no2):
        self.a=int(no1)
        self.b=int(no2)
    def display(self):
        print(self.a)
        print(self.b)
    
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def divide(self):
        print(self.a/self.b)
    def mul(self):
        print(self.a*self.b)

    
obj1=calculator(10,5)
# obj1.a=5
# obj1.b=500
obj1.display()
obj1.add()
obj1.sub()
obj1.mul()
obj1.divide()


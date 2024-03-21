# 1.) tasks
# write the code for the below tasks using function
# 1.) {"shirt":1000,"pant":1500,"shoes":900,"handkey":30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 's'

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 ---> [5,6 1,2,3,4]
# n=3 --> [4,5,6,1,2,3]


# ! method riding
# * polymorphism in classes using inheritance

'''
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

IOB rate is 7.5%
SBI rate is 9%
'''
# ! Eg:2
'''
class USA:
    def language(self):
        print("English")

    def capital(self):
        print("Washington DC")

class India(USA):
    def language(self):
        print("None")

    def capital(self):
        print("New Delhi")

I = India()
I.language()
I.capital()

None
New Delhi
'''

# Eg:3
# polymorphism using objects

#c1, c2 ---> = print(c1), print(c2)
# f1,f2a                                                                                                                                                                                                        

'''
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

class 1
class 2
'''
    
# Eg:4
'''
class c1:
    def f1(slef):
        print("class 1")

class c2(c1):
    def f1(slef):
        print("class 2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()

display(obj1)
display(obj2)

class 2
class 1
'''

# changing the functionally of built in function
'''
class shooping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length

s = shooping([1,2,3,4,5])
print(len(s))
#print(len(s))

5
'''

'''
a = 9
b = 6
#print(a+b)
#print(a.__add__(b)) # number method

# int()
#print(a.__sub__(b))
len()
'''

# ! ---> Method overload
# ! Eg:1
'''
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self, a,b,c):
        print(a+b+c)

s = suming()
#s.add(4,3)
s.add(4, 5, 1)


10

'''

# ! Eg:2
'''
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a,b,c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj = summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)


2
7
1 2 3
'''
'''
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj = summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

2
7
6

'''


# ! ------> Abstraction
# The process of hiding the implimentation details is adstraction


# ? Eg:1

'''
from abc import ABC, abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

    def name(self):
        print("I am triangle")

    def sides(self):
        pass

class square(shapes):
    def sqaure(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()
tr.name()

3 sides
I am triangle

'''

# ! Rules to define abstract class1
# 1.) Abstract class cannot be instantiated
# 2.) from abc import ABC, abstract method
# 3.) sub class the normal class with ABC
# 4.) convert the normal method inside the abstract  class to abstract
# 5.) all the child classes have to be sub classed with abstract class
# 6.) the abstract method should be present in the child classes



# Eg:2
# super()
'''
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1 (self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print(" I am child 1")

    def m1(self):
        pass

class2 = c2()
class2.m2()

This is abstract class
 I am child 1
'''


# * Eg:3
'''
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd

class login(password):
    def validate(self,name,passwrd):
        if super().pwd() == passwrd:
            print("welcome", name, "!!")
            print(" Login succesfull")
        else:
            print("Please check the password")

    def pwd(self):
        pass


login = login()
name = input("Enter the name: ")
pwd = input("Enter the password: ")
login.validate(name, pwd)

Enter the name: Mahesh
Enter the password: 123456
Please check the password
123456
123456

'''
# ! Encapsulation

'''
class car:
    name = "BMW" # private variable

c1 = car()
print(c1.name)
c1.name = "audi"
print(c1.name)

BMW
audi

'''


# * ---> Eg:2
# ? Accessing private date outside the class
'''
class c1:
    __phone = '9876543210'

    def display(self):
        print(self.__phone)
c = c1()
c.display()

9876543210

'''

# * ------> Eg:3
# ? declare private method
'''
class class1:
    def __m1(self):
        print("I am private method")

    def __init__(self):
        self.__m1()

c = class1()
#c.__m1() # error

I am private method

'''

# ? nested class
'''
class class1:
    class class2:
        name = "mahi"

        def display(self):
            print(self.name)
    obj1 = class2()


obj = class1()
obj.obj1.display()

mahi

'''








































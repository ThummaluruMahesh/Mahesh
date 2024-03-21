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





'''
a, b=c=7,8
print(a)
print(b)
print(c)
'''


'''
a=b, c=4,2
print(a,b,c)
'''

'''
---> changing of variables
a=7
b=5
Eg:1
temp=a temp=7
a=b    a=5
b=temp b=5

a=5,b=7
print(a,b)
'''
Eg:2
a=7
b=5
a=a+b
b=a-b
a=a-b

print(a,b)

'''
Eg:3

a=7
b=5
a, b=b, a
print(a,b)
'''
'''
Eg:4
a=7
b=5
a=a*b
b=a/b
a=a/b
print(int(a), int(b))
'''

'''
Eg:5
id()--->used to find the memory address of the variable
a=7
b=5
print(id(a)
print(id(b)
'''

'''
--->keywords
keywords are reserved words which provides special meaning to compiler or interpreteor
'''
import keyword+   
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))

'''
#To check if the string is keyword or not
print(keyword.iskeyword("mahesh"))# false

if = 8
print(if)# error coz if is a keyword
'''
'''
#--->literals
Literal is the constant value assigned  to a variable
A variable is considers to be constant when it is defines
in caps

a= 78 # a is variable
A=78 # A is constant
'''

'''
hash() -->it creates a hash value for constan datatypes and
provides error for non constant datatypes 
n1=89+7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1))# error --> list is non constant or mutable datatype
'''

a=9
b=9
b=90
print(id(a))
print(id(b))

# ---->operators
#operators are symbols which is used to perform various operations between 2 or more operations 

#Arithmatic
#Assignment
#Logical
#Relations or comparison
#Bitwise
#Identity
#Membership


# todo ----> Arithmatic ---> +,-,*,/,%,//,**
#Eg:1
'''
a=8
b=6
c=9
print(a+b+c)
'''

input() --> used to get the runtime input
n1 = input ("enter the value")
print(n1)






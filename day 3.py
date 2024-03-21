'''
# Eg: 3
# ? take the value lenth and breadth of a from user and check if it is square or not.
length=int(input())
breadth=int(input())
if length==breadth:
    print("its a square")
else:
    print("its not square")
'''


'''
# ! Eg:4
python program to check whether the given integer is a multiple of both 5 and 7

n=int(input("enter the number"))
if n%5==0 and n%7==0:
     print("yes")
 else:
     print("no")
     '''
'''
#Eg:5
#write a program to accept the cost price of a bike and display the road tax to be paid
#according to the following criteria :

#   cost price (in Rs)          Tax
#   >100000                     15% + discount 6%
#  >50000 and <=100000          10%
#  <=50000                      5%
'''
'''
price = int(input("enter the price:"))
amount = 0
if price >=100000:
   discount = 100000*(6/100)
   value = price-discount
   amount=value*(15/100)
   print(value+amount)

   enter the price:120000
114000.0
'''

'''
#Eg:6
#write a program to accept the cost price of a bike and display the road tax to be paid
#according to the following criteria :

#   cost price (in Rs)          Tax
#   >100000                     15% + discount 6%
#  >50000 and <=100000          10%
#  <=50000                      5%
   '''
'''
price = int (input("enter the price"))
total= 0
if price >=100000:
    discount = price*(6/100)
    value = price-discount
    tax = value*(15/100)
    total= value+tax
else:
    tax = price*(5/100)
    total = price +_tax
    print("the onroad cost of bike is: ",total)
'''

#------> if elif else
#Eg:1
'''
a = 7
b = 9
c = 3


if a<b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print(" c is greater")
'''

#Eg:2
# A school has having following  rules for grading system
#a. below 25 - F
#B. 25 to 45 - E
#C. 45 to 50 - D
#D. 50 to 60 - C
#E. 60 to 80 - B
#F. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
'''
mark = int(input("enter mark:"))
if mark>=80 and mark <=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("Fail")
'''

#! Eg: 7
#? accept the age of 4 people and display the oldest ane.

# ! --> short hand else
# Eg : 1
'''
a = 9
b = 60
if a>b:
      print("A")
else:
    print("B")
'''

# ! --> using short hand if else
# * Rules
#1.)statement inside the if condition have to be present at first
#2.)elif cannot be used in short hand if else
#3.)always it have to end with else
'''
print("A") if a<b else print ("B")
'''

# ! code  to check the given char is vowel or consonent
'''
char = input("Enter the char :")
if char=="a" or char =='e' or char=='i' or char=='o' or char=='u':
              print(" is a vowel")
else:
     print("its consonent")


# ? or

char = input("Enter the value")
str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")
'''

# ! shorthand if else
'''
char = input("enter the char:")
str1 = "aeiouAEIOU"
print("vowels")if char in str1 else print("consonent")
'''
# ! ---> elif ladder usig short hand if else
#Eg:1
# ? find greatest among 3 variables using short hand if else
'''
a = 8
b = 5
c = 9

print("A is greater ") if a>b and b>c else print("B is greater ")
if b>a and b>c else print("C is greater")
C is greater
'''
# ! ---------> looping

# looping can be implimented using
# for loop
# while loop

#--->  for loop
# ? for loop is used to iteartion, if we know the number of times the loop have to run
# ? it is used to iterate the iterables eg(string, list, tuple, etc...)


# todo --> syntax for loop

# ! for syntax in c
#for(i=0;i<10;i++){
#   print("hello");
#  }

# ! for syntax in python
#for user defined_variables in range (start, end, step): default step value is 1
#    statement
#    statement
#    statement

# ? Eg:1
# To print the value from 1 to 10 using for loop
'''
for i in range(0, 10): #(n, n-1)
    print(i)
'''
# ? Eg:2
'''
for val in range(23,50, 3):
    print(val)

 '''
'''
for val in range(23,50, 3):
    print(val)
'''

# ? Eg;3
# To decrement the value
'''
for val in range(10, 0,-1):
    print(val)
'''
'''
for val in range(10, 0,-2):
    print(val)
'''
# ? Eg:4
# ! print the output of 7th multiplicati0on table from 21 to 43
'''
for val in range (1,10+1):
    print('7','x',val,'=' ,val*7)
    7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''

# Eg:5
# ! print the output of 7th multiplicati0on table from 21 to 43
'''
m ethod 2
for val in range (1,10+1):
    ans="7 x {} ={}"
    print(ans.format(val,val*7))

7 x 1 =7
7 x 2 =14
7 x 3 =21
7 x 4 =28
7 x 5 =35
7 x 6 =42
7 x 7 =49
7 x 8 =56
7 x 9 =63
7 x 10 =70
'''

#---> method 3
'''
for val in range (1,10+1):
    print(f"7 x {val}={val*7}")

7 x 1=7
7 x 2=14
7 x 3=21
7 x 4=28
7 x 5=35
7 x 6=42
7 x 7=49
7 x 8=56
7 x 9=63
7 x 10=70
'''

#Eg:6
#break --> used to terminate thye loop
'''
for val in range (1,10):
    if val ==6:
        break
    print(val)
    '''


#Eg:7
'''
for val in range (1,10):
    if val ==6:
       print(val)
       break
'''

# ! continue
# Eg: 1
'''
for val in range(1,20):
    if val ==6:
        continue
    print(val)
1
2
3
4
5
7
8
9
10
11
12
13
14
15
16
17
18
19
'''

# EG: 3
'''
for val in range (1,40):
    if val ==7 or val ==8 or val ==24:
       continue
    print(val)
'''
'''
# ! practice problems
# ? print the even number between 20 to 40
for val in range(20,41, 2):
    print(val)
20
22
24
26
28
30
32
34
36
38
40
'''

#!---------> while loop
#while is used when we do not know the number of times the loop have to run
# ? to iterate the non iterable elements while loop is used


# todo sytax
# initialisation
# while condition
#     statement
#     incre or decre
'''
i = 0
while i<11:
    print(i)
    i+=1 # or +=1
0
1
2
3
4
5
6
7
8
9
10
'''
# Eg:2
#10,1
'''
i=10
while i>0:
    print(i)
    i-=1
10
9
8
7
6
5
4
3
2
1
'''
# ! ----> 1-4+9-16+25=15
'''
n =int(input("enter number"))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2!=0:
        sum=sum+sq
    else:
        sum=sum-sq
print(sum)
'''
i=0
'''
for val in range(1,6):
    i=val+i
    print(i)

1
3
6
10
15
'''


# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432















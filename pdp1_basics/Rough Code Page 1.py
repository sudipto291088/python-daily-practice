#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def evenandoddnum(onelis,twolis):
    thir = []
    
    for i in onelis:
        if i%2 == 0:
            thir.append(i)
    for j in twolis:
        if j%2 != 0:
            thir.append(j)
            
    return thir


lisa = []
lisb = []

a = int(input("Enter the range for list: "))

for i in range(a):
    ele = int(input())
    lisa.append(ele)

print("This is first list: ",lisa)

for k in range(a):
    vele = int(input())
    lisb.append(vele)

print("This is the second list: ",lisb)

evenandoddnum(lisa,lisb)


# In[ ]:


get_ipython().run_cell_magic('html', '', '<a href="https://www.geeksforgeeks.org/python-programming-language/">\n')


# In[ ]:


a = eval(input("enter a number"))
print("the number entered is {0}".format(a))
print(type(a))


# In[ ]:


s = eval(input("enter a list of number to print upto that number:   "))
print("just printing the usual list: ",list(range(0,s+1)))
print("printing the even list:  ",list(range(1,s+1,2)))
for i in range(0,s+1):
    if i%2 != 0:
        print(i, end = " ")


# In[ ]:


f = 0
while f <= 10:
    print(f)
    f = f+1
    #print(f)


# In[ ]:





# In[ ]:


def Suma(a,b):
    c = a+b
    print(c)
    return 


# In[ ]:


print(Suma(20,30))


# In[ ]:


def sum2(a,b):
    c = a + int(b)
    print(c)


# In[ ]:





# In[ ]:


import numpy as np


# In[ ]:


print(len(dir(np)))


# In[ ]:


def Suma(a,b,*arg):
    c = a+b
    print (c)
    print(*arg)
    


# In[ ]:


##Tuple inside a Tuple
Suma(10,20,(30,40,(50,)))


# In[ ]:


def sumb(a,b,*arg,**barg):
    c=a+b
    print(arg)
    print(barg)
    print(c)


# In[ ]:


sumb(50,50,50,x=50,y=50)


# In[ ]:


sumb(10,20)


# In[ ]:


global x
def scopevar(x,y):
    global z  
    print(x)
    print(y)
    z=x+y 
    print(z)
    return z
scopevar(20,30)
print(z)
print(x)


# In[ ]:


a=np.array({1,2})
a


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


a = np.random.randint(1,10,20).reshape(5,4)
#
a


# In[ ]:


df = pd.DataFrame(a,index=list("abcde"),columns=list("ABCD"))
df


# In[ ]:


df[["A","C","B"]]


# In[ ]:


df.iloc[0:4]


# In[ ]:


a = "python"
for i in a:
    if a == "h":
        break
    else:
        print(i)


# In[ ]:


a = "pypthonhdfg"
cnt = 0
for chr in a:
    if chr == "h":
        break
    print(chr)


# In[ ]:


a = "sutgiodfgkkkkgkkkkkk"
cnt = 1
for i in a:
    
        print(cnt,i)
        cnt = cnt+1


# In[ ]:


a = 1
b = 2
print("both {} and {}".format(a,b))


# In[ ]:


def greet(name):
    print("Hello,\n " + name + " Good Morning")
    return 

print(greet('Sudipto'))


# In[ ]:





# In[ ]:


def sum(a,b):
    c = a+b
    print(c)
    
sum(10,20)


# In[ ]:


a = eval(input("enter something: "))
len(a)


# In[ ]:


a = "ddd"
len(a)


# In[ ]:


print("Hello World")


# In[ ]:


a = "'Hello'"
print(a)


# In[ ]:


a = eval(input("Enter the first number: "))
b = eval(input("Enter the second number: "))

sum = a+b
print('sum of {} and {} is {}'.format(a,b,sum))


# In[ ]:


a = 3
print(id(a))


# In[ ]:


a = "0123456789"
len(a)
print(a[1])


# In[ ]:


a = "Entering AAAAnother String"
print(type(a),"\n\n")
print(dir(a), "\n")
print(a.lower())

a.capitalize()


# In[ ]:


a = []
dir(a)
a.


# In[ ]:


a=(1,2,4,5,6,7,8)
print(type(a), "\n")
print(dir(a))
a.count()


# In[ ]:


# Three sides of the triangle is a, b and c:  
a = int(input('Enter first side: '))  
b = int(input('Enter second side: '))  
c = int(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 5  
print('The area of the triangle is %0.2f is: ', area)


# In[ ]:


a = eval(input("enter a number for a:  "))
b = eval(input("enter your number for b:  "))

s = b
b = a
a = s

print("value of a after swapping is {} and for b is {}".format(a,b))


# In[ ]:


a = input("enter a number for a:  ")
b = input("enter your number for b:  ")

s = b
b = a
a = s

print("value of a after swapping is {} and for b is {}".format(a,b))


# In[ ]:


a = [34,67,89,23,29,18,90,-89]
b = 78 is a 
print(b)


# In[ ]:


a = [34,67,89,23,29,18,90,-89]
for i in a:
    print(i)


# In[ ]:


a = "ghghghghghghghg"
for ch in a:
    print (ch)


# In[ ]:


a = eval(input("Enter a specific value to generate number till that value: "))
for i in range(1,a+1):
    print(i)


# In[ ]:


a = "10"
len(a)


# In[ ]:


a = 15
for i in range(a,-a-1,-1):
    print(i)


# In[ ]:


a = 0
while a <= 10:
    print(a)
    a = a+1


# In[ ]:


g = 10
while g >= 0:
    print(g)
    g = g-1
    


# In[ ]:


def myfunc():
    x = 10
    print("value of x inside the function: ", x)


#x = 30
myfunc()
#print("value of x outside the function: ",x)


# In[ ]:


def Sum(a,b):
    c = a+b
    print(c)
    return c

print(Sum(10,20))


# In[ ]:


def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		print(num)
	else:
		print(-num)

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))


# In[ ]:


def test(a,b,*arg):
    return arg

print(test(1,2,5))


# In[ ]:


def justtest(*arg):
    return arg

justtest([5,6,7,8,9])


# In[ ]:


def anot(a,b,*arg):
    c = a+b
    print(c)
    print(*arg)

print(anot(5,6,8))


# In[ ]:


def anott(a,b,**kwarg):
    c = a+b+kwarg["x"]
    print(kwarg)
    return c
    

print(anott(1,2,x=3))


# # Programme to study the Scope of Variable

# In[ ]:


#global g
def study(a,b):
    print(a)
    print(b)
    global g
    g = a+b
    print(g)
    
study(12,23)
print(g)


# In[ ]:


global y
def suma(a,b):
    global y
    y = a+b
    print(y)

suma(10,20)
print(y)


# In[ ]:


def sum(a,d):
    global s
    s = a+d
    return s

sum(10,20)
print(s)


# In[ ]:


a = [1,2,3,4,5,6,7,8]
itr = iter(a)
print(next(itr))


# In[ ]:


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
#print(next(myit))
#print(next(myit))


# In[ ]:


##Create an iterator that returns numbers, starting with 1, 
## and each sequence will increase by one (returning 1,2,3,4,5 etc.)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# In[ ]:


s = 10

while s >= 0:
    print(s)
    s = s-1
    


# In[ ]:


a = [1,2,3,4,5]
itr = iter(a)
next(itr, "out of elements")



# In[ ]:


mystr = "naiyyukhapa"

for x in mystr:
    print(x)


# In[ ]:


gen = (i for i in range(5))
gen
next(gen, None)


# In[ ]:


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# In[ ]:


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
    a = my_gen()
    next(a)
    
    print(next(a))


# In[ ]:


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
    print(item) 


# In[ ]:


def astr(mystr):
    length = len(mystr)
    for i in range(length-1,-1,-1):
        yield mystr[i]
    
    

    
for char in astr("vartika"):
    print(char)


# In[ ]:


import numpy as np

a = np.array([])
a


# In[ ]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[ ]:


a = np.random.randint(1,7,25)
b = a.reshape(5,5)
print(b)
b[::-1,::-1]


# In[ ]:


import numpy as np
a = np.array([1,2,3])
print (a)


# In[ ]:


import numpy as np 
a = np.array([1, 2, 3,4,5], dtype = complex) 
print (a)
print(type(a))


# In[ ]:


import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape) 


# In[ ]:


# this is one dimensional array 
import numpy as np 
a = np.arange(24) 
a.ndim  

# now reshape it 
b = a.reshape(2,4,3) 
print (b) 
# b is having three dimensions


# In[ ]:


import numpy as np

x = [1,2,3]
a = np.asarray(x)
print(type(a))


# In[ ]:


import numpy as np

arr = np.array([1,2,3,4,5], ndmin = 5)

print(arr)
print(arr.shape)


# In[ ]:


import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

b = arr.reshape(-1)
print(b)


# In[ ]:


import numpy as np

arr = np.array([[1,2,3,4], [5,6,7,8]])

for x in arr:
    print (x)


# In[ ]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)


# In[ ]:


import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

z = np.concatenate((x,y))

print(z)


# In[ ]:


#3,5 and 6 are the indexes
import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x = np.where(arr == 4)
print(x)


# In[ ]:


import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr%2 == 0)
print(x)


# In[ ]:


import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

for x in arr:
    for y in x:
        print (y)


# In[ ]:


import numpy as np

arr = np.array([1,2,3,4,5,6])

x = np.array_split(arr,3)
print(x)


# In[ ]:


import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

x = np.array_split(arr,4)
print(x)


# In[ ]:


import numpy as np

arr = np.array([1,2,3,4,5,6])

x = np.array_split(arr,3)

print(x[0])
print(x[1])
print(x[2])


# In[ ]:


import numpy as np

from numpy import random


x = random.randint(100, size=(3,5))
print(x)


# In[ ]:


import numpy as np
from numpy import random

x = random.choice([3,5], size = (3,5))
print(x)


# In[ ]:


import numpy as np
from numpy import random

arr = np.array([1,2,3,4,5])
print(random.permutation(arr))


# In[ ]:


a = [1,2,3,4,5]
a.


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

print(mydb)


# In[ ]:





# In[ ]:


pip install mysql-connector-python


# In[ ]:


import mysql.connector


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# In[ ]:


import array as arr

a = arr.array('i',[1,2,3,4,5])
print(a)


# In[ ]:


import sys
 
stdin_fileno = sys.stdin
 
# Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
for line in stdin_fileno:
    # Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    else:
        print('Message from sys.stdin: ---> {} <---'.format(line))


# In[ ]:


import sys
txt = "  stupid  "
x = txt.strip()
print("monu is a",x,"girl")


# In[ ]:


import random

x = random.betavariate(2,1)
print(x)


# In[ ]:


a = input("Enter a number: ")
print(a)


# In[ ]:


n = int(input("Enter a specific number less than 25: "))

for i in range(0,n):
    
    if n>20:
        print("it should be less than 20")
        break        
    else:
        print(i**2)
        


# In[ ]:


a = eval(input("Enter a number to find the square of: "))
x = a**2
print("the number is {0} and the square is {1}".format(a,x))


# In[ ]:


n = int(input("Enter a partiular number: "))


if n%2==1:
    print ("Weird")
elif n%2 == 0 and 2 <= n <= 5:
    print ("Not Weird")
elif n%2 == 0 and 6 <= n <= 20:
    print ("Weird")
else:
    print ("Not Weird")


# In[ ]:


n = int(input("Enter a particluar number: "))

if n<0:
    print("only input a positive number please: ")
elif n%2 == 0 & 2 < n <60:
    print("the number is considerable: ")
else:
    print("odd")


# In[ ]:


def simpl(n):
    print(n)
    
simpl(5)


# In[ ]:


def is_leap(year):
    leap = False
    
    if 1900>=year or year>100000:
        leap = False
    elif year%4 == 0:
        if year%100 != 0 or year%400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = False
    
    return leap


is_leap(2000)


# In[ ]:


def is_leap(y):
    return (y%400==0) or (y%100!=0 and y%4==0)

is_leap(1992)


# In[ ]:


n = eval(input("Enter a number to print the range: "))

if n>=1 and n<=150:
    for i in range(1,n+1):
        print(i,end = "")
else:
    print("nok")


# In[ ]:


print reduce(lambda x, y: x+y, map(lambda x: str(x+1), range(int(input()))))


# In[ ]:


N = int(input())
print(*range(1,N+1), sep='')


# In[ ]:


ra_nge = []

for i in "human":
    ra_nge.append(i)
    print(ra_nge)
    


# In[ ]:


ra_nge = [i for i in "human" ]
print(ra_nge)


# In[ ]:


[i**2 if i<=5 else i**3 for i in range(10)]


# In[ ]:


for i in range(10):
    if i<=5:
        print(i**2)
    else:
        print(i**3)


# In[ ]:


lisst = [x for x in range(10) if x%2 == 0]
print(lisst)


# In[ ]:


neext = [x for x in range(100) if x%2 == 0 if x%5 == 0]
print(neext)


# In[ ]:


neext = ["Even" if x%2 == 0 else "Odd" for x in range(25)]
print(neext)


# In[ ]:


#Original Matrix
x = [[1,2],[3,4],[5,6]]
result = [[0, 0, 0], [0, 0, 0]]
# Iterate through rows
for i in range(len(x)):
#Iterate through columns
   for j in range(len(x[0])):
      result[j][i] = x[i][j]
   for r in result:
    print(r)


# In[ ]:


A = [[1,2],[3,4],[5,6]]

x = [[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[2])):
        result[j][i]=A[i][j]

for x in result:
    print(x)


# In[ ]:


A = [[1,2],[3,4],[5,6],[7,8]]

result = [[0,0,0,0],[0,0,0,0]]

for i in range(len(A)):
    for j in range(len(A[2])):
        result[j][i] = A[i][j]

print (result)


# In[ ]:


A = [[1,2],[4,5],[7,8]]

transp = [[row[i] for row in A] for i in range(2)]
print(transp)


# In[ ]:


A = [[1,2],[3,4],[5,6],[7,8]]
Transpo = [[row[i] for row in A] for i in range(2)]
print(Transpo)


# In[ ]:


A = [[1,2],[3,4],[5,6],[7,8]]

result = [[0,0,0,0],[0,0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i]=A[i][j]

print(result)


# In[ ]:


A = [[1,2],[3,4],[5,6],[7,81,3411]]
len(A)


# In[ ]:


a = [1,2,3,4]
b = {'a','b','c','d'}

dict.fromkeys(a,b)


# In[ ]:


keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
#value.append(2)
#print(vowels)


# In[ ]:


diction = {'Name':'Sudipto', 'Age':25, 4:'5'}
print(diction.get(4),"\n")

diction[4] = 6
print(diction)

diction[5] = 78
print(diction)


# In[ ]:


dict2 = {'a':2, 'b':'Sudipto'}
type(dict2)

dict2['a']=5

dict2['c']= 'Monu_barbie'
print(dict2)



# In[ ]:


#Demonstrating Dictionary examples
dict4 = {'a':2, 'b':5, 'name':'Sudipto' , 'surname':'Bhadra', 'd':89}

dict4.popitem()

print(dict4)
dict4.popitem()

dict4.setdefault('wifey','Monu_Barbie')
print(dict4)


# In[ ]:


diction = {'a':5,'b':6}
doc = {'a':78}

diction.update(doc)
print(diction)


# In[ ]:


a = {'a':5,'b':6,'name':'sudipto', 'surname':'bhadra'}
a.fromkeys('name')


# In[ ]:


a = [1,2,3,4,5,'tuple']
b = (1,2,3,4,5,'sudipto')
c = ["Ma"]

print(type(c))f


# In[ ]:


squares = dict()
for x in range(6):
    squares[x]= x*x

print(squares)


# In[ ]:


asq = {x:x*x for x in range(6)}
print(asq)


# In[ ]:


abs = dict()

for x in range(12):
    abs[x] = x*5
    
print(abs)
    


# In[ ]:


abs2 = {x:x*5 for x in range(12)}
print(abs2)


# In[ ]:


akku = {'sudipto': 25, 'akancha': 56}
resu = {}

for key in akku:
    akku[key] = akku[key]*25

print(akku)


# In[ ]:


sampl = {"sudip":564, "animesh":432}

for (key, value) in sampl.items():
    print(key)


# In[ ]:


ano_sam = {"santy":250, "sudipto": 240}
intere = 25

resu = {item:value*intere for (item, value) in ano_sam.items()}
print(resu)


# In[ ]:


furt = {"twi":54, "kwi":26, "amer":15, "swe":61}

resu = {item:value for (item, value) in furt.items() if value%2 == 0}
print(resu)


# In[ ]:


fibi2 = {"Avdesh":26, "Sunil":56, "Santy":45}

resu = {k:("old" if v>30 else "young") for (k,v) in fibi2.items()}
print(resu)


# In[ ]:


nayya = {'finnish':25, 'kidd':45, 'monish':35}
result = 1

for key in nayya:
    result = result*nayya[key]


print(result)


# In[ ]:


nayya = {'seco':24, 'pedocr':25}

for (key,value) in nayya.items():
    print(value)


# In[ ]:


saiyya = {"monu":45, "barbie": 35}
result = 1
for (key,value) in saiyya.items():
    result = result*value

print(result)


# In[ ]:


saiyya = {"monu":45, "barbie": 35}

for c in saiyya.values():
    c = c*24

    
print(c)


# In[ ]:


a = [1,3,"python","1+2j","python"]
a.pop()


# In[ ]:


a = [2,3,4,"sudpito"]
print(a[0])

dir(a)


# In[ ]:


nl = ['Happy',[0,16,28,39]]
print(nl[1][1])


# In[ ]:


a = [1,2,3,"pidus"]
type(a)


# In[ ]:


sampl = [13,32,87,12,56,29,50]
sampl[1:3] = [1,6]
print(sampl)


# In[ ]:


sandy = [21,43,67,89]
a = sandy*3
print(a)


# In[ ]:


a = [12,89,56]
a.insert(3,78)
print(a)


# In[ ]:


battle = ['p','r','o','b','l','e','m']
battle[2:3] = []
print(battle)


# In[ ]:


X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
lis = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]
print (lis)


# In[ ]:


x = int(input("input for x: "))
y = int(input("input for y: "))
z = int(input("input for z: "))
N = int(input("Finally for N: "))
combi = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != N]
print(combi)


# In[ ]:


x = int(input())
y = int(input())
z = int(input())
N = int(input())

obbo = []

for a in range(x):
    for b in range(y):
        for c in range(z):
            if a+b+c!= N:
                obbo = [a,b,c]
                print(obbo,end = "")


# In[ ]:


w = int(input())
l = int(input())
h = int(input())
A = 2*w*h + 2*l*w + 2*l*h
print(A)


# In[ ]:


a, b, c, n = [int(input()) for _ in range(4)]
print ([x,y,z] for x in range(a + 1) for y in range(b + 1) for z in range(c + 1) if x + y + z != n)


# In[ ]:


# Creating a list of desired size,
# Entering numbers into it,
# Printing the maximum number out of the inputs 
# We employ the max method()
li = []

m = int(input("Enter a number for the list: "))

for i in range(1,m+1):
    ele = int(input("Enter the numbers: "))
    li.append(ele)

print("the maximum number out of the list is {}".format(max(li)))


# In[ ]:


#Entered a list of number and print the sum of the numbers
a  = input("Enter a list of numbers separated by space: ")

b = a.split()

Sum = 0

for i in b:
    Sum = Sum+int(i)

print(Sum)


# In[ ]:


a = input("Enter a list of numbers: ")

b = a.split()
print(type(b))


# In[ ]:


#Demonstration of inputing numbers without split method

final_list = []

n = int(input("Enter a number for list range: "))

for i in range(n+1):
    print("Enter the number for",i,"position: ")
    number_add = int(input())
    final_list.append(number_add)

print(final_list)


# In[ ]:


#Without employing split method, input numbers and add them
a = []

n = int(input("enter a range of number: "))

for i in range(n):
    inpu = int(input("Enter the numbers: "))
    a.append(inpu)
    
print(sum(a))
    


# In[ ]:


for i in range(5):
    i = i+1
    print(i)
    


# In[ ]:


from platform import python_version
print(python_version())


# In[ ]:


def findSM(l):
    f, s = l[0], l[0]
    for i in range(len(l)):
        ##if the value is greater than f, s will be f and f will be the greater value
        if l[i] > f:
            s, f = f, l[i]
        ##when the value is less than f, and f is equal to s...s will be the value
        ##When the value is less than f, but more than s...s will be the value
        elif l[i] < f:
            if f == s:
                s = l[i]
            elif l[i] > s:
                s = l[i]
    return s            

n = int(input("Enter the number for range: "))
l = input("Enter the {} numbers with a space: ".format(n)).split() 
##without using split, we cannot have..
##...us enter numbers to be considered as list.

for i in range(n):
    l[i] = int(l[i])

print(findSM(l))


# In[ ]:


l = [12,23,4,6,7]

for i in range(len(l)):
    print("Hi")


# In[ ]:


n = int(input())
a = sorted([int(num) for num in input().split()])
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b[len(b)-2])b


# In[ ]:


help("modules")


# In[ ]:





# In[ ]:


my_num = int(input("Enter a number for the range: "))

prevnum = 0

for i in range(my_num):
    sum = prevnum+i
d    print("The current number is {}, previous num is {},hence the sum is {}".format(i,prevnum,sum))
    prevnum = i


# In[ ]:


Degg = int(input("Enter a valid number for celsius: "))
Fahren = (Degg*9/5)+32

print("The corresponding transformation of {} C to Fahrenheigt is {}".format(Degg,Fahren) )


# In[ ]:


##Trying to print of the alphabets in the even places of a string
def func(a):
    for i in range(0,len(a),2):
        print(a[i])
    

func('abraham')


# In[ ]:


s = "Python Rocks"
print(*dict.fromkeys(s))


# In[ ]:


for i in range(2,30,3):
    print('n')


# In[ ]:


def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 4))


# In[ ]:


input()
nums = sorted([int(x) for x in input().split()])
print([x for x in nums if x != nums[-1]][-1]);


# In[ ]:


a = [12,45,78,90,45]
b = sorted(a)
print(max(b))


# In[ ]:


a = input("Enter the nubmer for range determination: ")
b = sorted(input("Enter {} numbers: ".format(a)).split())
print([i for i in b if i != b[-1]][-1])


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (max[arr])


# In[ ]:


class MyClass(object):
    class_var = 1

    def __init__(self, i_var):
        self.i_var = i_var

foo = MyClass(2)
bar = MyClass(3)

print (MyClass.__dict__)
print (foo.__dict__)
print (bar.__dict__)


# In[ ]:


from bs4 import BeautifulSoup ##Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
import requests
import pandas as pd
x = []
x1 = []
source = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(source,'lxml')
z = soup.find_all('div',id='maincounter-wrap')
z1 = soup.find_all('div',class_='maincounter-number')


for k in z:
    y = k.h1.text
    x.append(y)
    
for i in z1:
    y1 = i.spam.text
    x1.append(y1)

df=pd.DataFrame(X1,x,['Number'])
df.head()


# In[ ]:


def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
    
p1 = twoSum([1,2,3,4,5,6], 10)
print(p1)


# In[ ]:


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}
        nums_len = len(nums)
        for i in range(nums_len):
            complement = target - nums[i]
            if complement in complement_dict:
                return [complement_dict[complement], i]
            else:
                if nums[i] in complement_dict:
                    continue
                complement_dict[nums[i]] = i  
                
                
    p1=Solution()
    print(p1.twoSum([1,2,3,4,5,6],10))


# In[ ]:


def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
    
p1 = twoSum('[1,2,3,4,5,6]',10)


# In[ ]:


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        for index, num in enumerate(nums):
            other = target - num
            
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index
                
        return []
    
p1 = Solution()
print(p1.twoSum([1,2,3,4,5,6],10))


# In[ ]:


class Solution:
    def twoSum(self, nums: [], target: int) -> []:
        r={}
        for i,j in enumerate(nums):
            s=target-j
            if s in r:
                return [r[s],i]
            r[j]=i
        return []
    

p1 = Solution()
print(p1.twoSum([1,2,3,4,5,6], 10))


# In[ ]:


class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5


# In[ ]:


def PrevSum(a):
    prevnum = 0
    for i in range(a):
        sum = prevnum+i
        print("the number is {} prev num is {} and the sum is {}".format(i,prevnum,sum))
        prevnum = i

a = int(input("enter a number for range: "))
PrevSum(a)


# In[ ]:


def add(a,b):
    c = a+b
    print(c)

n = 15
c = 45

v = add(n,c)
print(v)
    


# In[ ]:


class street:
    
    
    def __init__(self, length = 0, name = ""):
        self.length = length
        self.name = name
        
        

s = street(15, "MLD")

print(f"{s.length} and {s.name}")


# In[ ]:


class bus:
    name = ""
    
    def color(self):
        print(" the color of the bus is black")
        
class grey(bus):
    def display(self):
        print(" the name is: ", self.name)
        
        
#g1 = grey()
#g1.name = "greyhound 1980s"

#g1.color()
#g1.display()

b = bus()
b.name = "lacro"

print(b.name)


# In[ ]:


class Singer:
    def render(self):
        print("all the singers")
        
        
class soul(Singer):
    def render(self):
        print(" I am a soul singer")
        
class hiphop(Singer):
    def render(self):
        print(" I am a rapper ")
        
class metal(Singer):
    def render(self):
        print("I am a rockstar ")

        
m = metal()
m.render()

h = hiphop()
h.render()


# In[ ]:


import math as ma
class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by 
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        #area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        area = ma.sqrt(s * (s - a) * (s - b) * (s - c))
        print('The area of the triangle is %0.2f' %area)

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()


# In[ ]:


class sclass:
    def info(self):
        print("i am the sclass: ")
        
class sclass2:
    def info(self):
        print("i am the next super: ")
        
class der(sclass2, sclass):  ##the leftmost arguement class name will get called
    pass

d = der()
d.info()


# In[ ]:


sample = [1,2,3,4,5]

la = iter(sample)

print(next(la))
print(next(la))
print(next(la))
print(next(la))
print(next(la))
print(next(la))


# In[ ]:


def geno(n):
    
    value = 0
    while value<n:
        yield value
        value += 1
        
for value in geno(7):
    print(value)


# In[ ]:


class ptwo:
    
    def __init__(self, max=0):
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
        
    def __next__(self):
        if self.n <= self.max:
            res = 2 ** self.n
            self.n += 1
            return res
        else:
            raise StopIteration
            

mi = ptwo(3)

for i in ptwo(3):
    print(i)


# In[ ]:


def generator(n):
    
    value = 0
    while value < n:
        yield value
        value += 1
        
        
#for value in generator(3):
 #       print(value)
    
mu = generator(3)
print(next(mu))
print(next(mu))


# In[ ]:


def powtwo(max=0):
    n = 0
    while n < max:
        yield 2**n
        n += 1
        
mu = powtwo(6)
for i in mu:
    print(i)


# In[ ]:


def greet(name):
    def display_name():
        print("hi", name)
    
    display_name()
    
greet('rony')


# In[ ]:


def outer(x):
    def inner(y):
        return x+y
    return inner

plas = outer(6)
res = plas(5)

print(res)


# In[ ]:


def add(x,y):
    return x+y
def calc(func, x, y):
    return func(x,y)

result = calc(add, 5, 7)
print(result)


# In[ ]:


def make_pretty(func):
    def inner():
        print("i got decorated ")
        func()
    return inner

##@make_pretty
def ordi():
    print("i am ordinary")
    

a = make_pretty(ordi)
a()

        


# In[ ]:


def unordi(func):
    def inner():
        print("I am drizzled")
        func()
        print("Caramba")
    return inner

@unordi
def bunch():
    print("i am a hustler")
    
@unordi    
def pantaloon():
    print("pantaloon is the best shop")

bunch()
pantaloon()


# In[ ]:


def aldivide(func):
    def inner(a,b):
        print("I am going to divide", a ,"and", b)
        if b==0:
            print(" we cannot divide this: ")
            return
        return func(a,b)
    return inner


@aldivide
def divide(a,b):
    print(a/b)
    

divide(4,5)   









# In[ ]:


# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(300)

# Get the to_fahreheit method
print(human.to_fahrenheit())


# In[ ]:


## Demonstrating getters and setters
class Agelar:
    
    def __init__(self):
        self._age = 0
    
    def get_age(self):
        print("getter method")
        return self._age
    
    def set_age(self,a):
        print("setter method")
        self._age = a
    
    def del_age(self):
        del self._age
        
    age = property(get_age, set_age, del_age)

mr = Agelar()
mr.age = 10
print(mr.age)

    



# In[ ]:


class Price:
    def __init__(self):
        self._mpri = 900
        
    def sell(self):
        print("Selling price: {}".format(self._mpri))
        
    def setMax(self, a):
        self._mpri = a
        
pre = Price()
pre.sell()

pre.setMax(5000)
pre.sell()

pre.mpri = 8000 ##this assignment does not work
pre.sell()
        


# In[ ]:


class Glaza:
    
    def __init__(self):
        self._age = 0
        
    
    @property
    def age(self):
        print("Getter method called")
        return self._age
    
    @age.setter    
    def age(self,a):
        if(a<18):
            raise ValueError("Sorry you are not eligible")
        print("Setter method called")
        self._age = a
        

oma  = Glaza()
oma.age = 70
print(oma.age)
        
    
    


# In[ ]:


class random:
    
    def __init__(self, value):
        self._value = value
        
    def show(self):
        print(f"value is {self._value}")
        
    @property
    def ten_value(self):
        print("getter method is called: ")
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
        
        

ob = random(3)
##ob.ten_value = 67
print(ob.ten_value)
ob.show()
        


# In[ ]:


import re

pattern = '[abs]'
text = '''Hello
             Hey Jude, all i wanted to tell you is that i wanted to speak to you regarding the homework
             will you please let me know
             i am anxiously waiting'''
result = re.match(pattern,text)

if result:
    print("got it")
else:
    print("nope")


# In[ ]:


l = [2, 6, 10, 12, 16, 20]

def sumOfSquares(alist):
    return ((sum([i**2 for i in alist]))-(sum(alist)**2)/len(alist))

print(sumOfSquares(l))


# In[ ]:


##n=int(input("n="))

def sumsquare(neo):
    sum=0
    
    ##while(i<=n):
    for i in neo:
        sum= sum + i**2
        ##i += 1
    return sum

# print(sumsquare(n))
#print('the sum of square is {}'.format(sumsquare(n)))
sumsquare([1,2,2])


# In[ ]:


def someFunc(myList = [], *args):
    for x in myList:
        print (x)


# In[ ]:


def fact(n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))

a = int(input('enter a number to find fact: '))
fact(a)


# In[ ]:


def factworecursion(a):
    l=a
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        while a>1:
            a = a-1
            print(l,'*',a,'=',l*a)
            l=l*a
        return l
            
        
n = int(input('enter a number for fact: '))          
factworecursion(n)
    


# In[ ]:


fh = open("test1.txt")
fh


# In[ ]:


fh.read()


# In[53]:


import re

cnt = 0

a  = "This is Learnbay Learnbay Learnbay Learnbay i am a fan"

op = a.split()
for char in op:
    cnt = cnt+1
    where cnt == '3':
        re.sub('Learnbay','LB',a)


# In[51]:


def minmax(digits):
    max = digits[0]
    min = digits[0]

    for d in digits:
        if d > max:
            max = d
        if d < min:
            min = d
    result = (min, max)

    return result

digits = input('Enter integers seperated by space: ')
digits = [int(i) for i in digits.split()] #converting string into list of integers
print(minmax(digits))


# In[152]:


def sumar(m):
    mina = maxa = m[0]
    
    for i in m[1:]:
        if i <mina:
            mina = i
        else:
            if i>maxa:
                maxa = i
                
    return maxa,mina


sumar([12,3,2,5,6,89,100,67,4151,67])


# In[4]:


def pree(a):
    prev = 0
    for i in range(a):
        print('the prev {} the current {} the sum {}'.format(prev,i,prev+i))
        prev = i

pree(9)


# In[ ]:





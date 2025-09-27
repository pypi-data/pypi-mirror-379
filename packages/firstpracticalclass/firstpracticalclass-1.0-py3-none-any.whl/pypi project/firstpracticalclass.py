#Python Fundamentals

#Buildin Functions
#input/output
#Datatypes
#variables
#decisions in python along with operators
#Loops (For, while)
#File i/o
#functions/ modules
#list
#dictionaries
#string

#print = To print any statement
#if, else, elif, def, str, int, float

#Data types in Python
'''int-Numeric(whole number) 0,1,2,3,4 .....""
float-Numeric(Decimal) 0.1,0.2,0.3 ....."""
str- Characters (A, B , C)""
bool: True and false'''
#arithmetic operators
"+,-,/,*,//,*,%,**"

'''print("Hello world")
print ("0.1+0.2")
print ("hello"+"world")
print(123+123)
print("Hello World")

#Variables in python!
name="hafsa"
print(name)
print("Name:",name)

num=123
print(num)
print(num+num)
print(num+num*num/num)

a="hello"
b="world"
print(a+b)
a=1
b=2
c=3

quad=(-b+((b**2)-4*a*c)**(1/2))/(2*a)
print(quad)
a=2
c=3

formula2 = a**2 + 2*a*b + b*2
print(formula2)
#Areaofcircle = pi*r**2
pi=3.14
r=2
Areaofc = pi*r**2
print(Areaofc)

#Variable in variable
num1=int(input("Enter a first Value: "))
num2=int(input("Enter a second Value: "))
 
add=num1+num2
sub=num1-num2
div=num1/num2
mul=num1*num2
print("This is Addition:",add,"\nThis is Subtraction:",sub,"\nThis is Division:",div,"\nThis is multiplication",mul)

#Quad1= + (a,b,c)
#Quad2= -
#AOC=(pi,r)
#(a+b)**2(a,b)
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
pi=3.14
r=3

quad1=(-b+((b**2)-4*a*c)**(1/2))/(2*a)
quad2=(-b-((b**2)-4*a*c)**(1/2))/(2*a)
AOC=pi*r*2'''
'''formulae=a**2+(2*a*b)+b**2
print("quadratic1:",quad1)
print("quadratic2:",quad2)
print("Areaofcircle:",AOC)
print("formulavalue:",formulae)
m=int(input("Enter value of mass(m):"))
c1=3*(10**-8)
E=m*(c1**2)
print("Energy released:",E)'''
#arithmetic operators
#+,-,*,/
#Logical Operators
#and, or, not

#relational/comparision operators
#== leftside=rightside
#<  lessthan
#>  greaterthan
#<=lessthanequalto
#>=greaterthanequalto
#in

#Decisions in python
#if #always works for true condition
#else #always welcomes false condition

'''shafi=26
sami=35
check=shafi<=sami   #shafi==sami(False), shafi>=sami(False), shafi<=sami(True)
print(check)'''

#marksheet
'''obtain=int(input("Enter your obtained marks:"))
total=500
per=(obtain/total)*100

if per>=80:
    print("A+(Pass), and Percentage is:", per)
elif per>=70:
    print("A, and Percentage is:", per)
elif per>=60:
    print("B, and Percentage is:", per)
elif per>=50:
    print("C, and Percentage is:", per)
else:
    print("Fail",per)'''
#calculation by pressing

    def calculator()
    print("Welcome to calculator!")
    a=int(input("Enter value one:"))
    b=int(input("Enter value two:"))
    c=str(input("Enter your desire calculation:"))

    press1 =a+b
    press2 =a-b
    press3 =a*b
    press4 =a/b
    press5 =a**2
    if press1:
       print("press1 for addition of two numbers:",press1)
    elif press2: 
       print("press2 for subtraction of two numbers:",press2)
    elif press3:
       print("press3 for multiplication of two numbers:",press3)
    elif press4:
       print("press4 for division of two numbers:",press4)
    elif press5:
       print("press5 for power of value one to value two:",press5)
    else:
        print("wrong value")

#Another way

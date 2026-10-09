#code 1
def greet(name):
    print("Hello",name)
greet("Rashi")

print()

#code2
def add(num1,num2):
    print("sum =",num1+num2)
add(2,1)
    
print()

#code3
def greet(name):
    print("Hi",name, "! Nice to meet you", name )
greet("Rashi")

print()

#code4
def mul(num1):
    print("multiplication of",num1,"and",num1, "is", num1*num1 )
mul(3)

print()

#code5
def even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "False"
print(even_or_odd(5))

print()

#code6
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return("Cannot divide by zero")
    return a%b

def run_cal():
    x=3
    y=4
    print
    print(f"The numbers are {x} and {y}")
    print(f"Addition = {add(x,y)}")
    print(f"Subtraction = {sub(x,y)}")
    print(f"Multiplication = {mul(x,y)}")
    print(f"Division = {div(x,y)}")

run_cal()
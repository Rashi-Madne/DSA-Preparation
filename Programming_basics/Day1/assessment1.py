'''Write a Python program that:
1. Takes an integer from the user.
2. Checks whether it is positive, negative or zero.
3. Prints the appropriate message.'''


num=int(input("enter an integer: "))
if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")
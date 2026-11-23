'''Write a Python program that:
1. Creates a function called is_even().
2. Accepts an integer as a parameter.
3. Returns True if the number is even, otherwise returns False.
4. Takes input from the user and calls the function.
5. Prints the returned result.'''


def is_even(int):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter number: "))
result=is_even(int)
print(result)
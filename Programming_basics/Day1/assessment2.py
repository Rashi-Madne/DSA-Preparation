'''Write a program that:
1. Takes an integer n from the user.
2. Calculates the sum of all even numbers from 1 to n.
3. Prints the final sum.'''

numbers=int(input("enter an integer : "))
total=0
for number in range(1,numbers+1):
    if number%2==0:
        total+=number
print(total)
#code 1
#Take n integers as input and find the second-largest distinct number without using sort(), sorted(), max() or set().

n=int(input("How many integers are there in all : "))
first=int(input("enter first num : "))
largest_num=first
second_largest=None

for i in range(2,n+1):
    num=int(input(f"enter num {i} : "))

    if num>largest_num:
        second_largest=largest_num
        largest_num=num
        
    else:
        if num != largest_num and second_largest is None or num>second_largest:
            second_largest=num

if second_largest is None:
    print("There is no number which is second largest")
else:
    print(f"second largest num is {second_largest}")


#code 2
#Check whether a string is a palindrome, ignoring spaces and letter case but preserving all other characters.


#code 3
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
numbers=[]
for n in range(2000,3200):
    if n%7==0 and n%5!=0:
        numbers.append(str(n))  
print(",".join(numbers))

#code4
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n=int(input("num: "))
dict={}
for i in range(1,n+1):
    dict[i]=i*i
print(dict)








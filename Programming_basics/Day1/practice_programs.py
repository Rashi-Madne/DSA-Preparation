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






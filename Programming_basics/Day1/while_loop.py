#code 1
count=1
while count<=5:
    print(count)
    count=count+1

print()

#code 2
num=1
while num<=10:
        if num%2==0:
            print(num)
        num=num+1

print()

#code 3
num=1
while True:
    if num%2!=0:
        if num==123 or num==125:
            print(num)
    if num>125:
        break
    num=num+1

#code 4
sum=0
num=int(input("enter a num :"))
counter=1
while counter<=num:
    sum=sum+counter

    if counter==num:
        print(counter,end="=")
    else:
        print(counter,end="+")
    counter+=1
print(sum)

print()

#code 5
counter=1
num=int(input("enter a num : "))
while counter<=10:
    result=num*counter
    print(f"{num}x{counter}={result}")
    counter+=1


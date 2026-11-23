#tuples

#code1
colours=("red","yellow","blue","gray","black")
print(len(colours))
print(colours[0])
print(colours[1])
#colours[2]="black" not allowed because tuples are immmutable

print()

#code2
numbers=[3,54,23,45]
print(numbers)
print(len(numbers))
print(numbers[2])

print()

#code3
numbers=[3,54,23,45,46]
for num in numbers:
    print(num)
    
print()

#code4
numbers=[3,54,23,45,46]
print(numbers[0:2])

print()

#code5
numbers=[3,54,23,45,46]
num=int(input("enter the number: "))
if num in numbers:
    print("the num exists in the tuple")
else:
    print("the num does not exist in the tuple")

print()

#code6
numbers=[3,54,23,45,46]
num=int(input("enter the number from the tuple : "))
occurrences=numbers.count(num)
print(f"{num} appears {occurrences} times in the tuple")

print()

#code7
numbers=[3,54,23,45,46]
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print("largest number :",largest)
print("smallest number :",smallest)






























































































































 




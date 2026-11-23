#sets

numbers={43,23,76,65,56,65,76,23} #a set doesnt print repeated values
print(numbers)
print(len(numbers))
numbers.add(87)
print(numbers)
print(len(numbers))
numbers.remove(43)
print(len(numbers))
numbers=numbers-{65,76}
print(len(numbers))

#.add is used for sets
#.append is used for list

#practice programs
#pr1
a={2,1,1,3,5}
b={5,3,4,2}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#pr2
#Create a set with duplicate values and print it. Observe how duplicates are removed.
a={2,1,1,3,5}
print(a)

#pr3
#Create a set of 5 numbers. Add a new number using add() and print the updated set.
a={2,8,7,3,5}
a.add(4)
print(a)

#pr4
#Create a set of 5 numbers. Remove one element using remove() and print the updated set.
a={45,8,9,3,35}
a.remove(45)
print(a)

#pr5
#Create a set of numbers from 1 to 10. Ask the user for a number and check whether it exists in the set.
a={1,2,3,4,5,6,7,8,9,10}
num=int(input("enter the number: "))  
if num in a:
    print(f"{num} exists in a")
else:
    print("does not exist")


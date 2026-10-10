#list programs

#code1
marks=[43,45,65,32,76]
print(marks[0])
print(marks[-1])
marks[0]=21
print(marks)
print(marks[0])

print()

#list methods
roll_no=[34,26,22,27,35,32]
print(roll_no.append(13)) #this will return None because append method updates the list but returns None
roll_no.append(13)
print(roll_no)

print()

roll_no.remove(34)
print(4)
print(roll_no)

print()

print(len(roll_no))

print()

#slicing
numbers=[54,23,61,21,65,22]
print(numbers[0:3])
print(numbers[-1:-3]) #prints empty list because python doesnt go right to left
print(numbers[-1:-3:-1]) #third -1 tells to move backwards




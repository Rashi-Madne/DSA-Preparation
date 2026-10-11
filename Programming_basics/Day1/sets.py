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

#practice program
#Create a list and a tuple containing three fruits each. Print the second fruit from each. Then change the second fruit in the list and print the updated list.
fruits=["Mango","Apple","Papaya"]
FRUITS=("Banana","Litchi","Orange")

print(fruits[1])
print(FRUITS[1])
fruits.append("Watermelon")
FRUITS.append("Muskmelons") #will generate error
print(fruits)
print(FRUITS)  #will generate error




#.add is used for sets
#.append is used for list
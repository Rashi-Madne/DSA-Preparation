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
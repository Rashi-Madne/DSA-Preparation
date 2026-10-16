#With a given list of fruits, write a program to generate a dictionary that contains (fruit, len(fruit)) such that each fruit in the list is mapped to its total character count. Then, the program should print the dictionary.
FRUIT=input("Enter fruit names separated by commas : ")
fruits=[fruit.strip() for fruit in FRUIT.split(",")]
fr_dict={fruit:len(fruit) for fruit in fruits}
print(fr_dict)
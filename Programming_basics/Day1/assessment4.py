'''Write a program that:
1. Takes a string from the user.
2. Stores each character in a list.
3. Reverses the list using a loop (don't use reverse() or slicing).
4. Prints the reversed result.'''

str=input("Enter a word : ")
list1=[]
for ch in str:
    list1.append(ch)
reversed_list=[]
for i in range(len(list1)-1,-1,-1):
    reversed_list.append(list1[i])
print("Reversed :","".join(reversed_list))
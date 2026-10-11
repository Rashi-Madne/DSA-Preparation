num=int(input("Enter a num : "))
even_sum=0
odd_nums=0

for i in range(1,num+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_nums+=1
print(even_sum)
print(odd_nums)
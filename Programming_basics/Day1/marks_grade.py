marks=int(input("enter your marks: "))
print("Your marks are ",marks)

if(marks>=90 and marks<=100):
    print("excellent")
elif(marks>=75 and marks<=89):
    print("very good")
elif(marks>=60 and marks<=74):
    print("good")
elif(marks>=40 and marks<=59):
    print("pass")
elif(marks>=0 and marks<40):
    print("fail")
else:
    print("invalid")
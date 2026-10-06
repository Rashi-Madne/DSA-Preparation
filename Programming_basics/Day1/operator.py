day=input("enter the day: ").title()

if day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday":
    print("Its a week-day")
elif day=="Saturday" or day=="Sunday":
    print("Its a weekend")
else:
    print("invalid day ")


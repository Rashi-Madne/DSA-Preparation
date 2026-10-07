age=int(input("enter your age : "))
ID=input("Do you have your ID (yes or no) ? : ").lower()

if age>=18:
    if ID=="yes":
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Under-age entries are not aloowed")
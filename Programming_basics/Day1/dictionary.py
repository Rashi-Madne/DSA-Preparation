#dictionary
student={"name":"Rashi","age":22,"college":"RBU"}
print(student)

print()

print(student["name"]) #lists uses indexes, dic uses keys

print()

student["age"]=21
print(student)

print()

print(student.pop("age"))
print(student)

print()

#looping through a dictionary
for key in student:
    print(key,student[key])

#practice programs

#code 1
#Create a dictionary containing your name, age, and college. Print each value separately using its key.
details={"name":"Harry",
         "age":8,
         "School":"Sandipani"}
print(details["name"])
print(details['age'])
print(details['School'])

print()

#code2
#Add a "city" key and update the age. Print the final dictionary.
details["city"]="Nagpur"
print(details)

print()

#code3
#Remove one key using pop(), and print the result.
details.pop("age")
print(details)

print()

#code4
#Create a dictionary containing three subjects and their marks.Use a loop to calculate and print the total marks. Don't use sum() yet.
marks={"Maths":45,"Hindi":49,"English":45}
total=0
for mark in marks.values():
    total+=mark
print(total)

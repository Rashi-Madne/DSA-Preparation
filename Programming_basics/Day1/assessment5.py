'''Write a program that:
1. Creates a dictionary containing three students and their marks.
2. Uses a for loop to calculate total marks.
3. Calculates the average marks.
4. Prints both total and average.'''

Performance={"A":45,
             "B" :65,
             "C" : 76}
total_marks=0
average_marks=0
for marks in Performance.values():
    total_marks+=marks
average_marks=total_marks/len(Performance)
print(total_marks)
print(average_marks)
# Student Grade Calculator

   # Input  Of   System
 
 # In this system every subject contain 100 marks
 

name = input("Enter student name: ")

english = float(input("Enter English marks: "))
math = float(input("Enter Math marks: "))
python = float(input("Enter Python marks: "))
ai = float(input("Enter AI marks: "))
dld = float(input("Enter DLD marks: "))

total = english + math + python + ai + dld
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Output   of   System


print("----- Student Result -----")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
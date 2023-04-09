"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.2 - Grade Calculator
"""
# Criteria
30% - Assignments
70% - Final Exam

# Grade Classification
1. score >= 80% : "A"
2. score >= 70% : "B"
3. score >= 550% : "C"
4. score >= 45% : "D"
"""

# Creating a dictionary which includes the student names,
# assignment result, exam results

# 1. Seannie's Dictionary
seannie = {"name" : "Vo Thien Hai Le",
           "assignment" : [90, 93, 95, 100], "exam" : [97.55]}

# 2. Dustin's Dictionary
dustin = {"name" : "Dustin Timm",
           "assignment" : [80, 96, 75, 95], "exam" : [95.57]}

# 3. Yvonne's Dictionary
yvonne = {"name" : "Yvonne Timm",
           "assignment" : [70, 73, 97, 99], "exam" : [98.59]}

# 4. Khai's Dictionary
khai = {"name" : "Ngoc Khai Le",
           "assignment" : [100, 83, 100, 90], "exam" : [94.76]}

students = [seannie, dustin, yvonne, khai]

# Function to calculate average
def average(scores):
    total = sum(scores)
    total = float(total)
    return total / len(scores)
    
# Function to calculate total average
def calculate_total_avg(students):
    assignment = average(students["assignment"])
    exam = average(students["exam"])
    # return the result based on the criteria
    return (0.3 * assignment + 0.7 * exam)

# Function to classify students
def students_classification(gpa):
    if gpa >= 80: return "A"
    elif gpa >= 70: return "B"
    elif gpa >= 55: return "C"
    elif gpa >= 45: return "D"
    else: return "E"

for i in students:
    print(i["name"])
    print("GPA of %s is: %.2f" %(i["name"], calculate_total_avg(i)))
    print("It is equivalent to %s" %(students_classification(calculate_total_avg(i))))
    print("--------------------------------------------------------")
    print()
    
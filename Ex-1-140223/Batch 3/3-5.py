"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.5
n = int(input("Enter the number that you want to have the multiplication table: "))
print("The Multiplication Table of:", n)
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)
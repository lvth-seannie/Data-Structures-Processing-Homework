"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 1.4
n = int(input('Enter a number: '))
sum = 0
while (n > 0):
    dig = n % 10
    sum += dig
    n = n // 10
print("Sum of digits is:", sum)
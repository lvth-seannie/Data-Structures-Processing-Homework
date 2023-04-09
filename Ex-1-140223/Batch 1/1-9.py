"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 1.5
# Using statistics.mean() to calculate the average of the list
from statistics import mean 
list = []
# Asking for the number of elements in the list 
n = int(input("Enter the number of elements in the list = "))
# Loop through and take input for each element
for i in range(n):
    element = int(input("Enter elements {}: \n".format(i + 1)))
    list.append(element)
average = mean(list)
print("List =", list)
print("Average =", average)


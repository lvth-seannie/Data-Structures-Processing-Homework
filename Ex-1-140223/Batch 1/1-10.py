"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 1.10
from statistics import median
list = []
# Find the number of elements in the list
number_of_elements = int(input("Enter the number of elements = "))
# Loop through and add elements into the list
for i in range(number_of_elements):
    element = int(input("Enter elements {}:\n".format(i+1)))
    list.append(element)
print("List =", list)
# Find the median of the list
Median = median(list)
print("Meidan =", Median)
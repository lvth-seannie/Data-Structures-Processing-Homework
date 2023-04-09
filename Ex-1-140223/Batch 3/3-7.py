"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.7
list = []
number_of_elements = int(input("Enter the number of elements in the list: "))
for i in range(number_of_elements):
    element = int(input("Enter elements {}: ".format(i + 1)))
    list.append(element) # Add elements into the list
print("List =", list)
reversed_list = list[::-1] # Reverse the elements in the list
print("New List =", reversed_list)
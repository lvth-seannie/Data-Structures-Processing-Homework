"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 2.7 - Largest String
list = []
number_of_elements = int(input("Enter the number of elements in the list of strings: "))
for i in range(number_of_elements):
    element = str(input("Enter elements {}:\n".format(i+1)))
    list.append(element)
print("List =", list)
# Find the largest string
def largeststring(list):
    count = 0
    for i in list: # Loop through the list
        if len(i) > count: # Check for the longest sring
            count = len(i)
            word = i
    return ("The Largest String is " + "'" + word + "'")
print(largeststring(list))

    
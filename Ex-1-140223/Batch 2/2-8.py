"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 2.8
def reversestring(string):
    rvstr = string[::-1]  # reverse string
    return ("The reverse string is " + rvstr)

string = str(input("Enter a string: "))
print(reversestring(string))
"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 2.3 - Palindrome
def palindrome(string):
    # compares the original string with the reverse string
    if (string == string[::-1]):
        return True # returns true if it is equal to each other
    else:
        return False # returns false otherwise
    
string = str(input("Enter a string: "))
print(palindrome(string))
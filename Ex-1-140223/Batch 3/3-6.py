"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.6
string = str(input("Enter a sentence: "))
split_str = string.split(' ') # Split the string by spaces
reversed_str = reversed(split_str) # Reverse every single word
final_str = ' '.join(reversed_str) # Join the reversed words
print("The new sentence is", final_str)
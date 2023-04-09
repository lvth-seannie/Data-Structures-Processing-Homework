"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.8 - Word Count
OUT = 0
IN = 1
def wordcount(string):
    count = 0
    state = OUT
    for i in range(len(string)):
        if (string[i] == ' ' or string[i] == '\n'
            or string[i] == '\t'):
            state = OUT
        elif state == OUT:
            state = IN
            count += 1
    return count

string = str(input("Enter a string: "))
print("The number of words in the string: " + str(wordcount(string)))
"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.9
def vowelcount(string):
    count = 0
    # Loop through the string to count vowels
    for i in range(len(string)):
        if (string[i] == 'a' or string[i] == 'e' or
            string[i] == 'i' or string[i] == 'o' or
            string[i] == 'u'):
            count += 1
    return count

string = str(input("Enter a string: "))
print("The number of vowels in the string is " + str(vowelcount(string)))

"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 2.4: LCM
def main():
    # take 2 positive integers
    a = int(input("Enter the first positive integer: "))
    b = int(input("Enter the second positive integer: "))
    c = a * b
    # find the least common multiple by looping through
    for i in range(1, c + 1):
        if (i % a == 0 and i % b == 0):
            print("The least common multiple of the given two positive integers is:", i)
main()
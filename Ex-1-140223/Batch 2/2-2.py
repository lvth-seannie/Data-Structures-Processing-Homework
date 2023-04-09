"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 2.2 - Fibonacco Sequence
def fibonacci(n):
    a, b = 0, 1 # initialize the first 2 numbers of the sequence
    if n <= 0: # check if the input is <= 0
        n = int(input("Please enter a positive integer = "))
    
    # Print the first 2 numbers
    print(a, end = '')
    print(b, end = '')
    
    # Loop through and calculate the next numbers in the sequence
    for i in range(2, n):
        c = a + b
        print(c, end = '')
        a = b
        b = c
        
# Call the function
n = int(input("Enter a positive integer = "))
fibonacci(n)
    
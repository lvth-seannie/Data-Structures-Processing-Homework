"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.4
n = int(input("Enter a number = "))
if n > 1:
    for i in range(2, n // 2):
        if (n % i) == 0:
            print(n, "is not a prime number.")
            break
    else:
        print(n, "is a prime number.")  
# If the number is <= 1, it is not a prime number.
else:
    print(n, "is not a prime number.")

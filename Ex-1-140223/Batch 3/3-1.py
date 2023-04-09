"""
Name: Vo Thien Hai Le
Class: CH-701-A
Matriculation Number: 30006085
v.le@constructor.university 
"""
# Batch 3.1 - Convert Temperature
cel_1 = float(input("Temperature in Celsius = "))
fah_1 = (cel_1 * 1.8) + 32
print("The %.2f degree Celsius is equal to %.2f Fahrenheit!" %(cel_1, fah_1))

print("--------OR--------")

fah_2 = float(input("Temperature in Fahrenheit = "))
cel_2 = (fah_2 - 32) * 5/9
print("The %.2f degree Fahrenheit is equal to %.2f Celsius!" %(fah_2, cel_2))
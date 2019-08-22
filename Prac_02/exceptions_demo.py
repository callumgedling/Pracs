"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Please enter a value which is not 0:"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

# A value error will occur when a user attempts to enter a string instead of an integer.

# Zero division error will occur when the user enters zero for the denominator

# yes, a while loop could be used which will not allow the program to run if the user enters the value 0 for the denominator

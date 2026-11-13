# FUNCTION-CALCULATOR

# PART 1: Import random and math modules
import random
import math

def calculate_operators(plus,minus,multiply,divide):
    return sum

print("===== FUNCTION-CALCULATOR =====")

print("Pick an Operation and eneter two numbers")

try:
    number = int(input("Please enter a number: "))
#using Valuerror
except ValueError as ex:
    print("Enter an actual number please:")

try: 
    num1 = int(input("Cannot divide by zero"))
    num2 = int(input("Undividble by zero"))
    Result = num1 / num2 
    #using Zerodivisionerror
except ZeroDivisionError as ex:
    print("!ERROR!,Cannot divide by zero!")

# PART 2: Genearate seperate functions for each operation
float(int(input("Enter an operator and two numbers")))


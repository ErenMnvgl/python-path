"""
import math

yarıcap = int(input("Lutfen yarıcap gırınız: "))

C = 2*math.pi*yarıcap

print(f"{C}")
"""
num1 = float(input("Please enter a number"))
num2 = float(input("Please enter a number"))

operator = input("Please enter a operator")

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2 
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("Please enter correct things")

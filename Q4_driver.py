# Test driver for Q4
from Q2 import convert
import Q4

while 1:
    num1 = convert(str(raw_input("Enter 1st number ('q' to quit): ")))
    if num1 == 'q':
        break
    num2 = convert(str(raw_input("Enter 2st number ('q' to quit): ")))
    if num2 == 'q':
        break
    num3 = convert(str(raw_input("Enter 3st number ('q' to quit): ")))
    if num3 == 'q':
        break
    print("Inputs: " + str(num1)+ ", " + str(num2)+ ", " + str(num3))
    print("The minimum value is " + str(Q4.findMinimum(num1, num2, num3)))

    

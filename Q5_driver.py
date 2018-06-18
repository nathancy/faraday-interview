# Test driver for Q5
from Q2 import convert
import Q5

while 1:
    left_operand = convert(str(raw_input("Enter left_operand ('q' to quit): ")))
    if left_operand == 'q':
        break
    right_operand = convert(str(raw_input("Enter right_operand ('q' to quit): ")))
    if right_operand == 'q':
        break
    operator = convert(str(raw_input("Enter operator ('q' to quit): ")))
    if operator == 'q':
        break
    print("Inputs: " + str(left_operand)+ ", " + str(right_operand)+ ", " + str(operator))
    print("Result is: " + str(Q5.apply_operation(left_operand, right_operand, operator)))
    

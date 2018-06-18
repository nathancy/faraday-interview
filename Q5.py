"""
File: Q5.py
Author: Nathan Lam
Description: Modularized operation functions into separate functions

Reformat this code to be more elegant

def apply_operation(left_operand, right_operand, operator):
    if operator == '+':
    	return left_operand + right_operand
    elif operator == '-':
    	return left_operand - right_operand
    elif operator == '*':
    	return left_operand * right_operand
    elif operator == '/':
    	return left_operand / right_operand 
"""

def apply_operation(left_operand, right_operand, operator):
    operation_table = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
            }
    return operation_table[operator](left_operand, right_operand)

# Modularize operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


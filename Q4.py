'''
File: Q4.py
Author: Nathan Lam
Description: Method to find miniumun without using min()

Implement a method that takes 3 numbers as input and finds the minimum of the three without using the built-in min function
'''

# Finds the minimum between a, b, and c
def findMinimum(a, b, c):
    minimum = minimumHelper(a,b) 
    return minimumHelper(minimum, c)

# Helper function that returns the minimum between a and b
def minimumHelper(a, b):
    return a if a <= b else b

# Scalability version
# Instead of taking 3 separate inputs, put as many inputs as needed into a list (l)
def findMinimumScale(l):
    minimum = float('inf')
    for number in l:
        minimum = minimumHelper(minimum, number)
    return minimum


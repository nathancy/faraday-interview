"""
File: Q2.py
Author: Nathan Lam
Description: Convert function which returns the converted int, float, or string 
             value of a given string

Write a function that takes string as input.
a. Output to be int/float/string depending if the string can be converted to float or integer type
b. Example:

def convert(a=""):
return converted_value
>>> type(convert('1'))
<type 'int'>
>>> type(convert('1.0'))
<type 'float'>
>>> type(convert('asd'))
<type 'str'>
"""

# Takes a string as input and outputs int/float/string depending on type
def convert(a):
    try:
        i = int(a)
    	return i
    except ValueError:
	try:
            f = float(a)
            return f
        except ValueError:
            return a


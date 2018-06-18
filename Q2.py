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

# ==========================
# Test Driver 
# ==========================
def unitTests():
    a = "1"
    b = "1.0"
    c = "asd"
    d = "A1B2C3.3;;'"
    e = "{\{{{PP{O}}"
    f = "12777777*"
    g = "+asssssdf"
    h = "123666.6345"
    i = "-123"
    j = "0"

    print("""
Some unit tests are:
a = "1"
b = "1.0"
c = "asd"
d = "A1B2C3.3;;'"
e = "{\{{{PP{O}}"
f = "1#2777777*"
g = "+asssssdf"
h = "123666.6345"
i = "-123"
j = "0"
    """)
    print("Result from convert function:")
    print(type(convert(a)))
    print(type(convert(b)))
    print(type(convert(c)))
    print(type(convert(d)))
    print(type(convert(e)))
    print(type(convert(f)))
    print(type(convert(g)))
    print(type(convert(h)))
    print(type(convert(i)))
    print(type(convert(j)))

def customTester():
    print(" ")
    print("Custom tester")
    s = str(raw_input("Enter a string to convert ('q' to quit): "))
    while s != 'q':
        print(s)
        print(type(convert(s)))
        s = str(raw_input("Enter string for conversion tester ('q' to quit program): "))

unitTests()
customTester()

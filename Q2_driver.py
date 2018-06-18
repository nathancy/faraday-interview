# Test driver for Q2
from Q2 import convert

# Individual unit tests
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

# Custom tester for inputs from console
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

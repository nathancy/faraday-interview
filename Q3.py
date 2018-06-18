"""
File: Q3.py
Author: Nathan Lam
Description: Defines the simpleDatabase class which stores items and can return
             the unique elements as well as the frequency of elements. Contains a test driver
             to test the functions of the class.

Reformat this code to be more elegant

abc = ['dog', 'Fido', 10]
animal = abc[0]
name = abc[1]
age = abc[2]
output = ('{name} the {animal} is {age} years old'.format(animal=animal, name=name, age=age))
"""

dictonary_argv = {
        'animal':'dog',
        'name':'Fido',
        'age':10
        }
output = '{name} the {animal} is {age} years old'.format(**dictonary_argv)
print(output)


"""
File: Q1.py
Author: Nathan Lam
Description: Defines the simpleDatabase class which stores items and can return
             the unique elements as well as the frequency of elements. Contains a test driver
             to test the functions of the class.

Write a new class with the following requirements
a. To store a list of items
b. A method to return all unique items from the list
c. A method to return all items and their frequency
d. Should be able to append/insert new items to the list
"""

# ==========================
# Class Definition 
# ==========================

class simpleDatabase(object):

    # Initialize class instance 
    def __init__(self, contents=None):
        if not contents:
            self.contents = []
        else:
            self.contents = contents

        self.initializeUnique(contents)
        self.initializeFrequency(contents)

    # Initialize structure to contain unique contents
    def initializeUnique(self, contents):
        self.unique = set()
        if not contents:
            return
        for item in contents:
            if item not in self.unique:
                self.unique.add(item)

    # Initialize structure to keep track of the frequency of the contents 
    def initializeFrequency(self, contents):
        self.frequency = {}
        if not contents:
            return
        for item in contents:
            if item not in self.frequency:
                self.frequency[item] = 1
            else:
                self.frequency[item] += 1

    # Insert content into list and update properties
    def insert(self, content, index):
        if (index > len(self.contents) - 1) or index < 0:
            print("ERROR: Invalid index value, out of bounds!")
            exit(1)
        self.contents.insert(index, content)
        self.updateUnique(content)
        self.updateFrequency(content)

    # Append content to end of the list and update properties
    def append(self, content):
        self.contents.append(content)
        self.updateUnique(content)
        self.updateFrequency(content)

    # Update unique contents in the list 
    def updateUnique(self, content):
        if content not in self.unique:
            self.unique.add(content)

    # Update frequency of content in the list
    def updateFrequency(self, content):
        if content not in self.frequency:
            self.frequency[content] = 1
        else:
            self.frequency[content] += 1

    # Return unique contents as a list
    def getUnique(self):
        return list(self.unique)

    # Return the frequency as a hash table with content (key) and frequency (value)
    def getFrequency(self):
        return self.frequency
   
    # Return all of the contents in the list
    def getContents(self):
        return self.contents

# ==========================
# Test Driver 
# ==========================

# ==========================================
# Test #1
# ==========================================
print("Test #1 (Initial list empty)")
test_list = []
database1 = simpleDatabase(test_list)

print("Initial contents of list are:")
print(database1.getContents())

print("Unique contents of the list are:")
print(database1.getUnique())

print("The contents of the list with its respective frequency are:")
print(database1.getFrequency())

print("Appending some contents into the list")
for num in range(5):
    database1.append(num)

print("Current contents of the list")
print(database1.getContents())

print("Inserting some items into the list")
database1.insert(123, 4)
database1.insert(3, 5)
database1.insert(4, 5)

print("Contents of the list after inserting items")
print(database1.getContents())

print("Unique contents of the list are:")
print(database1.getUnique())

print("The contents of the list with its respective frequency are:")
print(database1.getFrequency())

print(" ")

# ==========================================
# Test #2
# ==========================================
print("Test #2 (Initial list not empty)")
test_list = [3,3,3,123,3,1,5,6,7]
database2 = simpleDatabase(test_list)

print("Initial contents of list are:")
print(database2.getContents())

print("Unique contents of the list are:")
print(database2.getUnique())

print("The contents of the list with its respective frequency are:")
print(database2.getFrequency())

print("Inserting and appending some contents into the list")
database2.append(9999)
database2.insert(12333, 3)
database2.insert(3, 3)
database2.insert(3, 4)

print("Contents of the list after inserting items")
print(database2.getContents())

print("Unique contents of the list are:")
print(database2.getUnique())

print("The contents of the list with its respective frequency are:")
print(database2.getFrequency())


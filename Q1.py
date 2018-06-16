"""
File: Q1.py
Author: Nathan Lam
Description: Defines the simpleDatabase class which stores items and can return
             the unique elements as well as the frequency of elements.

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

    # Ensure only one instance of the database
    _instances = []

    # Initialize class instance 
    def __init__(self, contents=None):

        if(len(self._instances) > 1):
            print "ERROR: One instance of simpleDatabase is already running!"
            exit(1)
        self._instances.append(self)

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
            print "ERROR: Invalid index value, out of bounds!"
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

# Create a database
test_list = [3,3,3,123,3,1,5,6,7]
database = simpleDatabase(test_list)

# Returns all current items and their frequency
print database.getContents()

# Returns unique items
print database.getUnique()

# Returns the contents with its respective frequency
print database.getFrequency() 

# Add items into list
database.append(9999)
database.insert(12333, 3)
database.insert(3, 3)

# Returns all current items and their frequency
print database.getContents()

# Returns unique items
print database.getUnique()

# Returns the contents with its respective frequency
print database.getFrequency() 


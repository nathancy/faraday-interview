"""
Write a new class with the following requirements
a. To store a list of items
b. A method to return all unique items from the list
c. A method to return all items and their frequency
d. Should be able to append/insert new items to the list
"""
# ==========================
# Class definition
# ==========================

class simpleDatabase(object):
    _instances = []
    _internal_list = []

    def __init__(self):
        """
        Initialize simple database

        Args: 
            None

        Returns:
            None
        """
        if(len(self._instances) > 1):
            print("ERROR: One instance of simpleDatabase is already running!")
            exit(1)
        self._instances.append(self)

    def insert(self, l):
        """
        Takes in a list and inserts the contents into the internal database

        Args:
            l (list): list to insert into the database

        Returns:
            None
        """
        if not l:
            return
        for item in l:
            self._internal_list.append(item)
   
    def unique(self):
        """
        Iterates through the internal database to find the unique items 

        Args:
            None

        Returns:
            All unique items from the database as a list
        """
        hash_table = {}
        ans = []
        for item in self._internal_list:
            if item not in hash_table:
                hash_table[item] = 1
                ans.append(item)
        return ans
    
    def databaseItems(self):
        """
        Returns all items in the database and its frequency

        Args:
            None

        Returns:
            A hash table with key (item) and value (frequency)
        """
        hash_table = {}
        for item in self._internal_list:
            if item not in hash_table:
                hash_table[item] = 1
            else:
                hash_table[item] += 1
        return hash_table

# ==========================
# Test Driver 
# ==========================

test_list = [3,3,3,123,3,1,5,6,7]
database = simpleDatabase()

# Returns all current items and their frequency
print database.databaseItems()

# Insert a list
database.insert(test_list)

# Returns all current items and their frequency
print database.databaseItems()

# Returns all unique items from the database
print database.unique()

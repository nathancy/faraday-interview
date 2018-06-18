# Test driver for Q1
from Q1 import simpleDatabase 

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


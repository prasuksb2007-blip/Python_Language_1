# Program to demonstrate various operations on lists in Python.

# 1. List References (shared memory)
list_1 = [1, 2, 3]
list_2 = list_1
list_1[0] = 99
print("Both change because of shared reference:", list_2)

# 2. Making Independent Copies Using Slices ([:])
original = [10, 20, 30]
copied = original[:]
original[0] = 999
print("Copy stays safe:", copied)

# 3. Using Slices
my_list = [10, 8, 6, 4, 2]
print("Slice [1:3]:", my_list[1:3])
print("Slice from beginning [:3]:", my_list[:3])
print("Slice to end [3:]:", my_list[3:])

# 4. 'in' and 'not in' operators
numbers = [1, 2, 3, 4]
print("Is 3 in list?", 3 in numbers)
print("Is 5 not in list?", 5 not in numbers)
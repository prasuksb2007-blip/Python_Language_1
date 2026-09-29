# Program to demonstrate various operations on lists in Python.

# Creating a list and checking its length
numbers = [10, 5, 7, 2, 1]
print("Length:", len(numbers))

# Indexing and modifying elements
numbers[0] = 111
print("First element:", numbers[0])

# Negative indexing
print("Last element:", numbers[-1])

# Adding elements
numbers.append(99)
numbers.insert(0, 55)
print("After adding elements:", numbers)

# Removing elements
del numbers[1]
print("After deleting element at index 1:", numbers)
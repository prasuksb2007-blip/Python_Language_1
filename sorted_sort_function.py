# Program to demonstrate the sorted() and sort() functions

# Demonstrating the sorted() function: creates a new sorted list, original remains untouched
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()

# Demonstrating the sort() method: sorts the list in-place, no new list is created
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)
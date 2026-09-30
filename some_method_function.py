# Program to demonstrate some string methods and functions

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Simple Python code demonstrating all string methods from Section 3

# 1. capitalize(): Makes the first letter uppercase, rest lowercase
print("hello world".capitalize())          # Output: Hello world

# 2. center(): Centers string within a given width using spaces or a character
print("cat".center(7, "*"))                # Output: **cat**

# 3. endswith(): Checks if string ends with specific letters (True/False)
print("python".endswith("on"))             # Output: True

# 4. find(): Finds position (index) of a substring, returns -1 if not found
print("apple".find("p"))                   # Output: 1

# 5. isalnum(): Checks if string has only letters and numbers (no spaces/symbols)
print("User123".isalnum())                 # Output: True

# 6. isalpha(): Checks if string has letters only
print("Python".isalpha())                  # Output: True

# 7. isdigit(): Checks if string has numbers only
print("12345".isdigit())                   # Output: True

# 8. islower(): Checks if all letters are lowercase
print("hello".islower())                   # Output: True

# 9. isspace(): Checks if string has whitespace only
print("   ".isspace())                     # Output: True

# 10. isupper(): Checks if all letters are uppercase
print("HELLO".isupper())                   # Output: True

# 11. join(): Glues a list of strings together using a separator
print("-".join(["2026", "09", "30"]))      # Output: 2026-09-30

# 12. lower(): Converts all letters to lowercase
print("PYTHON".lower())                    # Output: python

# 13. lstrip(): Removes spaces or characters from the left side
print("   hello".lstrip())                 # Output: hello

# 14. replace(): Swaps out a part of a string with something else
print("I like cats".replace("cats", "dogs")) # Output: I like dogs

# 15. rfind(): Like find(), but searches starting from the right side
print("banana".rfind("a"))                 # Output: 5

# 16. rstrip(): Removes spaces or characters from the right side
print("hello   ".rstrip())                 # Output: hello

# 17. split(): Cuts a string into a list of pieces using a separator
print("apple,banana,grape".split(","))     # Output: ['apple', 'banana', 'grape']

# 18. startswith(): Checks if string starts with specific letters (True/False)
print("python".startswith("py"))           # Output: True

# 19. strip(): Removes spaces from both sides
print("   hello   ".strip())               # Output: hello

# 20. swapcase(): Flips uppercase to lowercase and vice versa
print("Python".swapcase())                 # Output: pYTHON

# 21. title(): Capitalizes the first letter of every word
print("hello world".title())               # Output: Hello World

# 22. upper(): Converts all letters to uppercase
print("python".upper())                    # Output: PYTHON
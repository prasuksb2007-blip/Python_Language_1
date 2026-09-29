# 1. Tuples (Immutable sequences - cannot be changed)
my_tuple = (1, 10, 100)
print("First element:", my_tuple[0])
print("Length:", len(my_tuple))

# 2. Dictionaries (Mutable key-value pairs)
my_dict = {"cat": "chat", "dog": "chien"}
print("French for cat:", my_dict["cat"])

# Adding and modifying items
my_dict["horse"] = "cheval"  # Add new item
my_dict["cat"] = "minou"    # Modify existing item

# 3. Looping through dictionaries
for key, value in my_dict.items():
    print(key, "->", value)
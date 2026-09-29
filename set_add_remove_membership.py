# Program to demonstrate set membership, addition, and removal.
set={"apple","banana","cherry","orange","mango"}
print(set)
for i in set:
    print(i)
print("banana" in set)
print("banana" not in set)
set.add("strawberry")
print(set)
set.remove("cherry")
print(set)

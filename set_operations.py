# Program to demonstrate union, intersection, difference, and subset operations.
set1={"apple","banana","cherry","orange","kiwi","melon","mango"}
set2={"apple","banana","cherry","orange","mango"}
print (set1.union(set2))
print (set1.intersection(set2))
print (set1.difference(set2))
print (set2.difference(set1))
print (set1.issubset(set2))
print (set1.issuperset(set2))
print (set2.issubset(set1))
print (set2.issuperset(set1))
# Program to demonstrate dictionary keys, values, items, and access.
dict1={ "name":"Prasuk",
        "age":"18",
        "city":"Pune",
        "state":"Maharastra",
      }
print(dict1) 
print(dict1["city"])
print(len(dict1))
print(type(dict1))
print(dict1.keys()) 
print(dict1.values()) 
print(dict1.items())
for i in dict1.items():
    print(i)

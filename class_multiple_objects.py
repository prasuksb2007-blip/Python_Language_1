# Program to demonstrate creating multiple objects from a class.
class MyClass:
    def __init__(self, name, section):
        self.name=name
        self.section=section

obj1=MyClass("Prasuk", "SOC23")
print(obj1.name)
print(obj1.section)
obj2=MyClass("Vansh", "SOC23")
print(obj2.name)
print(obj2.section)
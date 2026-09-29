# Program to demonstrate a class constructor with name and age attributes.
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
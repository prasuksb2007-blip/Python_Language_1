# Program to demonstrate a class method accepting a variable number of arguments.
class MathOperations:
    def add(self, *args):
        return sum(args)
    
math=MathOperations()
print(math.add(5))
print(math.add(5,10))
print(math.add(5,10,15))
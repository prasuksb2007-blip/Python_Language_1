# Program to calculate factorial using functions without arguments and return values.
def facto_for():
    num1=int(input("Enter number for factorial:"))
    facto_for = 1
    for i in range(1, num1 + 1):
        facto_for *= i
    print(f"Factorial of {num1} is {facto_for}")
def facto_while():
    facto_while = 1
    i = 1
    num1=int(input("Enter number for factorial:"))
    while i <= num1:
        facto_while *= i
        i += 1    
    print(f"Factorial of {num1} is {facto_while}")
facto_for()
facto_while()
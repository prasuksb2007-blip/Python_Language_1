# Program to calculate factorial using functions without arguments and with return values.
def facto_for():
    facto_for = 1
    num1=int(input("Enter number for factorial:"))
    for i in range(1, num1 + 1):
        facto_for *= i
    return facto_for
def facto_while():
    facto_while = 1
    i = 1
    num1=int(input("Enter number for factorial:"))
    while i <= num1:
        facto_while *= i
        i += 1    
    return facto_while
result1=facto_for()
result2=facto_while()
print("factorial:",result1)
print("factorial:",result2)


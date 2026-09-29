# Program to calculate factorial using functions with arguments and no return values.
def facto_for(n):
    facto_for = 1
    for i in range(1, n + 1):
        facto_for *= i
    print(f"Factorial of {num1} is {facto_for}")
def facto_while(n):
    facto_while = 1
    i = 1
    while i <= n:
        facto_while *= i
        i += 1    
    print(f"Factorial of {num1} is {facto_while}")
num1=int(input("Enter number for factorial:"))
facto_for(num1)
facto_while(num1)

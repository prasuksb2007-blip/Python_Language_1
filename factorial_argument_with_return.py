# Program to calculate factorial using functions with arguments and return values.
def facto_for(n):
    facto_for = 1
    for i in range(1, n + 1):
        facto_for *= i
    return facto_for
def facto_recursive(n):
    if(n<=1):
        return 1
    return n * facto_recursive(n-1)
def facto_while(n):
    facto_while = 1
    i = 1
    while i <= n:
        facto_while *= i
        i += 1    
    return facto_while
num1=int(input("Enter number for factorial:"))
result1=facto_for(num1)
result2=facto_recursive(num1)
result3=facto_while(num1)
print("factorial:",result1)
print("factorial:",result2)
print("factorial:",result3)



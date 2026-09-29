# Program to swap two numbers using a function.
def swap(x,y):
    x,y=y,x
    return x,y

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("\nBefore Swaping:")
print("The value of first number:",num1)
print("The value of seconf number:",num2)

num1,num2=swap(num1,num2)
print("\nAfter Swaping:")
print("The value of first number:",num1)
print("The value of seconf number:",num2)
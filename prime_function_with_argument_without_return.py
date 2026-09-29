# Program to check whether a number is prime using an argument and no return value.
def prime(x):
    i=2
    prime=True
    while i<x:
        if(num1 % 2==0):
            prime=False
            break
        i+=1
    print("Prime:",prime)

num1=int(input("Enter number:"))
prime(num1)


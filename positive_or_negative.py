# Program to determine whether a number is positive, negative, or zero.
a=int(input("Enter your number:"))
if a==0:
    print("Number is neither positive nor negative")
elif a>0:
    print(f'{a} is positive')
else:
    print(f'{a} is negative')
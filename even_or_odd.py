# Program to determine whether a number is even, odd, or zero.
a=int(input("Enter your number:"))
if a==0:
    print("Number is neither even nor odd")
elif (a%2)==0:
    print("Number is even")
else:
    print("Number is odd")
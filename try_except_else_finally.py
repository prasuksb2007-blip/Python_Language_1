# Program to demonstrate try, except, else, and finally blocks.
try:
    num1= int(input("Enter a number:"))
    num2= int(input("Enter a number:"))
    answer=num1/num2
except ZeroDivisionError:
    print("Number divided by Zero")
else:
    print("Execution Succesfull")
finally:
    print("In Finally Block")
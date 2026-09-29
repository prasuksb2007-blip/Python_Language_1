# Program to demonstrate arithmetic operations using a menu.
print("Menu:")
print("1.Addition:")
print("2.Subtraction:")
print("3.Multiplication:")
print("4.Division:")
print("Exit")
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2st Number:"))
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Addition of two number:",num1+num2)
    if choice==2:
        print("Subtraction of two number:",num1-num2)
    if choice==3:
        print("Multiplication of two number:",num1*num2) 
    if choice==4:
        print("Division of two number:",num1/num2)
    if choice>=5:
        break

# Program to check whether a number is prime without arguments and with a return value.
def prime():
    i=2
    prime=True
    num1=int(input("Enter number:"))
    while i<num1:
        if(num1 % 2==0):
            prime=False
            break
        i+=1
    return prime

result=prime()
print("Prime:",result)



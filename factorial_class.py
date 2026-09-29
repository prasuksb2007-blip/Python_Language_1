# Program to calculate a factorial using a class method.
class Factorial:
    def myFact(self,num):
        fact=1
        for i in range(1, num+1):
            fact =  fact * i
        print("Fcatorial of number:",fact)

object1= Factorial()
num1 = int(input("Enter Number:"))
object1.myFact(num1)
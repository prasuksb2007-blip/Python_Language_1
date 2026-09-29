# Program to demonstrate breaking a while loop at a condition.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
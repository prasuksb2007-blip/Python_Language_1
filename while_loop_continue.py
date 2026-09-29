# Program to demonstrate skipping an iteration in a while loop using continue.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
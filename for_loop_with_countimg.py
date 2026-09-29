# A program that counts to five, printing "Mississippi" after each number. After counting, it prints "Ready or not, here I come!"
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")
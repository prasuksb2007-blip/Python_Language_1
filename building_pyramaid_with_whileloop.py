# Program to build a pyramid with a given number of blocks using a while loop.

blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1

while blocks >= in_layer:
    blocks -= in_layer
    height += 1
    in_layer += 1

print("The height of the pyramid:", height)
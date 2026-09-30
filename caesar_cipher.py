# Program to implement a simple Caesar cipher that shifts letters by 1 position in the alphabet.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    # For decryption, you would subtract 1 instead of adding 1
    # code = ord(char) - 1
    # if code < ord('A'):
        # code = ord('Z')
    cipher += chr(code)

print(cipher)
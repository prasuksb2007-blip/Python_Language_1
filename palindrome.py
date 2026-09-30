# Palindrome Checker
text = input("Enter text: ")
# Remove spaces and convert to lowercase
cleaned = "".join(text.split()).lower()

if cleaned == "":
    print("It's not a palindrome")
elif cleaned == cleaned[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
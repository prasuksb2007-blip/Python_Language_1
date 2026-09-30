# Anagram Checker
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

clean1 = "".join(text1.split()).lower()
clean2 = "".join(text2.split()).lower()

if clean1 == "" or clean2 == "":
    print("Not anagrams")
elif sorted(clean1) == sorted(clean2):
    print("Anagrams")
else:
    print("Not anagrams")
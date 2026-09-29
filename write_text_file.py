# Program to write text content to a file.
text="This is my new content"
fp=open(r'C:\Users\S11404\PRASUK JAIN 57\Regular Lecture\TextFile.txt','w')
fp.write(text)
print("Completed writing")
fp.close()
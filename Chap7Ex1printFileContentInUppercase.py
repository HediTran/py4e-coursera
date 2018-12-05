# This program to read through a file and print the contents
# of the file (line by line) all in upper case.
	
fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except:
	print("File cannot be opened:", fname)
	exit()
inp = str(fhand.read())
print(len(inp))
inp = inp.upper()
print(inp[:20])

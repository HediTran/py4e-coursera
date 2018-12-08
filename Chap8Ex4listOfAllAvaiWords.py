# This program read a file, and print out a list of
# all available words sorted in alphabetical order

fname = input("Enter the file name: ")
try:
	fhand = open(fname)
except:
	print("File cannot be opened:", fname)
	exit()
    
 ans = list()
    
for line in fhand:
	words = line.split()
	for word in words:
		if word not in ans:
		ans.append(word)
    
ans.sort()
print(ans)

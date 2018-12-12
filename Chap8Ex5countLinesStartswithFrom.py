# This program read through the mail box data and find 
# line that starts with "From". Then, it will count the
# number of From (not From:) lines and print out the result
# https://www.py4e.com/code3/mbox.txt
# https://www.py4e.com/code3/mbox-short.txt

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
    
count = 0
    
for line in fhand:
    if line.startswith("From:"): continue
    elif line.startswith("From"):
        words = line.split()
        print(words[1])
        count += 1
    
print("There were ", count, "lines in the file with From as the first word")

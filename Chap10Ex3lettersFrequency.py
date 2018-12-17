# This program reads a file and prints the letters in 
# decreasing order of frequency

import string
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
    
letter_freq = dict()
    
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        for c in word:
            if c.isalpha():
                if c not in letter_freq:
                    letter_freq[c] = 1
                else:
                    letter_freq[c] += 1
                
t = list()
for letter, freq in list(letter_freq.items()):
    t.append((freq, letter))
    
t.sort(reverse=True)
    
for freq, letter in t:
    print(letter, freq)

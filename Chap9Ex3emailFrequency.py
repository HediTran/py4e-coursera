# This program read through a mail log, buid a histogram
# to count how many messages have come from each email address
# https://www.py4e.com/code3/mbox.txt
# https://www.py4e.com/code3/mbox-short.txt

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
        
email_freq = dict()
        
for line in fhand:
    if line.startswith("From:"): continue
    elif line.startswith("From"):
        words = line.split()
        email_freq[words[1]] = email_freq.get(words[1], 0) + 1

for email in email_freq:
    print(email, email_freq[email])

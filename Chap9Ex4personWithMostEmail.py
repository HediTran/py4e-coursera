# This program read through a mail log and print out
# the email address with the most messages in the file
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

lst = list(email_freq.values())
    
for email in email_freq:
     if email_freq[email] == max(lst):
        print("This is the person with the most messages:", email, email_freq[email])

# This program read through a mail log and print out
# the email address with the most commits
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
    
t = list()
for email, count in list(email_freq.items()):
    t.append((count, email))
    
t.sort(reverse=True)
    
freq, person_with_the_most_emails = t[0]
    
print(person_with_the_most_emails, freq)

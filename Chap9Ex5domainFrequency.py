# This program read through a mail log, buid a histogram
# to count how many messages have come from each Domain Name
# https://www.py4e.com/code3/mbox.txt
# https://www.py4e.com/code3/mbox-short.txt

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
    
domain_freq = dict()
    
for line in fhand:
    if line.startswith("From:"): continue
    elif line.startswith("From"):
        words = line.split()
        at_pos = words[1].find("@")
        domain_freq[(words[1][at_pos + 1:])] = domain_freq.get(words[1][at_pos + 1:], 0) + 1
    
for domain in domain_freq:
    print(domain, domain_freq[domain])

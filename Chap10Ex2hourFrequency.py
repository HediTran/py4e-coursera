# This program reads through a mail log and counts
# the distribution of the hour of the day for each
# messages
# https://www.py4e.com/code3/mbox.txt
# https://www.py4e.com/code3/mbox-short.txt

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
    
hour_freq = dict()
    
for line in fhand:
    if line.startswith("From:"): continue
    elif line.startswith("From"):
        words = line.split()
        colon_pos = words[5].find(":")
        hour_freq[words[5][:colon_pos]] = hour_freq.get(words[5][:colon_pos], 0) + 1
    
t = list(hour_freq.items())
t.sort()
    
for hour, freq in t:
    print(hour, freq)

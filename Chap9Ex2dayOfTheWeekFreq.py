# This program categorizes each mail message by which day
# of the week the commit was done.
# https://www.py4e.com/code3/mbox.txt
# https://www.py4e.com/code3/mbox-short.txt

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
    
day_of_the_week_freq = dict()
    
for line in fhand:
    if line.startswith("From:"): continue
    elif line.startswith("From"):
         words = line.split()
         day_of_the_week_freq[words[2]] = day_of_the_week_freq.get(words[2], 0) + 1
    
print(day_of_the_week_freq)

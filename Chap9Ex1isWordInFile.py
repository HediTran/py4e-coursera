# This programs reads a file. Then it
# checks whether a word is in that file

str = dict()
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

for line in fhand:
    words = line.split()
    for word in words:
        str[word] = 0

while True:
    word_to_look_up = input("Type 'done' to end program. Enter the word you want to check in this file: ")

    if word_to_look_up == "done": break
    elif word_to_look_up in str: print("This word IS in this file.\n")
    else: print("This word IS NOT in this file.\n")

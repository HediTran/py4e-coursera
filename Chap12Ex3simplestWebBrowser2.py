# This program combines Chap12Ex1 and Chap12Ex2
# but using urllib library instead of socket library

import urllib
from urllib.request import urlopen

url = input("Enter the URL: ")

# The number of character has been shown
count = 0

try:
    fhand = urlopen(url)
    for line in fhand:
        for char in line.decode():
            count += 1
            if count <= 3000:
                print(char, end = "")

    print("\nTotal number of characters in this document: ", count)
    

except:
    print("URL improperly formatted or non-existent: ", url)
    exit()

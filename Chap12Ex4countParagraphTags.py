# This program extract and count paragraph (p) tags from
# the retrieved HTML document
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
    
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
    
url = input("Enter the URL: ")
# Example: https://docs.python.org 

html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
    
# Retrieve all of the anchor tags and count them
tags = soup('p')
count = 0
for tag in tags:
    count += 1

print("Number of paragraph (p) tags from the retrieved HTML document: ", count)

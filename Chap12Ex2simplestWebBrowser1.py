# This program makes a connection to a web server, follows
# the rules of the HTTP protocol to request a document and
# display what the server sends back. However, this program 
# only shows up to 3000 characters.

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Enter the URL: ")

try:
    # Extract the domain name from the input
    url_component_parts = url.split("/")
    domain_name = url_component_parts[2]

    mysock.connect((domain_name, 80))
    cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()
    mysock.send(cmd)
    
    # The number of character has been shown
    count = 0

    while True:
        data = mysock.recv(500)
        if len(data) < 1:
            break
        count += len(data.decode())
        if count <= 3000:
            print(data.decode(), end = "")
    
    print("\n\nTotal number of characters in this document: ", count)
    mysock.close()
except:
    print("URL improperly formatted or non-existent: ", url)
    exit()

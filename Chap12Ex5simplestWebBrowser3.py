# This program is an upgraded version of Chap12Ex1
# It only shows data after the headers and a blank line received
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
url = input("Enter the URL: ")
# Example: http://data.pr4e.org/romeo.txt
    
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
        data = mysock.recv(512)
        if len(data) < 1:
            break
        blank_line_pos = data.decode().find('\r\n\r\n') 
        if blank_line_pos != -1: 
            # 4 because blank line has len('\r\n\r\n') = 4
            print(data.decode()[blank_line_pos + 4:], end = "")
        else:
            print(data.decode(), end = "")
        
    mysock.close()
except:
    print("URL improperly formatted or non-existent: ", url)
    exit()

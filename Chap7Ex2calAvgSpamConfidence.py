	# This program read mbox.txt file 
	# and extract floating point number on line that start with
	# X-DSPAM-Confidence: and calculate the average spam confidence
	# https://www.py4e.com/code3/mbox.txt
	
	fname = input("Enter the file name: ")
    try:
        fhand = open(fname)
    except:
        print("File cannot be opened:", fname)
        exit()
    
    count = 0;
    total = 0;
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            count += 1
            space_pos = line.find(" ")
            total += float(line[space_pos:])
    
    print("Average spam confidence:", total/count)

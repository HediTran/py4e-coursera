# This program prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”.

list_num = list()
    
while True:
    num = input("Enter a number: ")
    try:
        list_num.append(float(num))
    except:
        if num == "done":
            print("Maximum:", max(list_num))
            print("Minimum:", min(list_num))
            break
        else:
            print("Invalid input")
            continue


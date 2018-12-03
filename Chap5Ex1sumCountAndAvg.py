# This program repeatedly reads numbers until the user enters "done".
# Once "done is entered, print out the total, count, and average of
# the numbers. If the user enters anything other than a number, detect
# their mistake and skip to the next number

sum = 0
count = 0
while True:
    ans = input("Enter a number: ")
    try:
        ans = float(ans)
        sum += ans
        count += 1
    except:
        if ans == "done":
            break
        else:
            print("Invalid input")
            continue
print(sum, count, sum/count)


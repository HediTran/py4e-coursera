def initializeMaxMinNumber():
	while True:
		initial_max_and_min_number = input("Enter a number: ")
		try:
			initial_max_and_min_number = float(initial_max_and_min_number)
			break
		except:
			print("Invalid input")
	return initial_max_and_min_number
    
max_number = min_number = initializeMaxMinNumber()
    
while True:
	ans = input("Enter a number: ")
	try:
		ans = float(ans)
		if ans > max_number:
			max_number = ans
		elif ans < min_number:
			min_number = ans
	except:
		if ans == "done":
			break
		else:
			print("Invalid input")
			continue
    
print("Max Number is:", max_number, "Min Number is:", min_number)

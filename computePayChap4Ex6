# Pay computation with time-and-a-half for over-time

try:
	hours = int(input("Please enter hours: "))
	rate_per_hour = float(input("Please enter rate per hour: "))
    
	if hours > 40:
		overtime_rate_per_hour = rate_per_hour * 1.5
		print("Gross pay is: ", round(40*rate_per_hour + (hours-40)*overtime_rate_per_hour, 2))
	else:
		print("Gross pay is: ", round(hours*rate_per_hour, 2))
except:
	print("Error, please enter numeric input")


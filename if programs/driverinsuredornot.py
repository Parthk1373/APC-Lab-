m = input("Are you married?(yes/no): ")
g = input("What is your Gender (Male/Female): ")
a = int(input("Enter your age: "))

if m == "yes":
	print("Driver is insured")
elif m == "no" and g == "male" and a>30:
	print("Driver is insured")
elif m == "no" and g == "female" and a>25:
	print("Driver is insured")
else: 
	print("Driver is not insured")
#check the square root is prime or not

n=int(input("Enter the value of n: "))

r=int(n**0.5)
count=0

for i in range(1, r+1):
	if r % i==0:
		count = count + 1
		if(i%)
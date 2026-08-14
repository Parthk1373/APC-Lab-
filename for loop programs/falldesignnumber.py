#fall design of numbers

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(1 + j, end="")
    print()

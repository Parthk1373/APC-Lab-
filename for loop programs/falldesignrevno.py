#fall design of numbers 1,22,333....n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

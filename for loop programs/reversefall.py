#if user enters n value as 5 print reverse fall design of  ABCDE 

n = int(input("Enter value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

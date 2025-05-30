for j in range(1, 10):#outer loop
    for i in range(1):#inner loop
        print(j * 2, end = '')
    print()

n = int(input("Enter n:"))
for j in range(1):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

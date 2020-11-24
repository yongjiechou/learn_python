x=int(input("nxn table:"))
for i in range(1, x+1):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end="")
    print()

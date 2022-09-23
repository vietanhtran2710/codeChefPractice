t = int(input())
for i in range(t):
    x = int(input())
    print((x * 60 - 5) // 30 + 1 if (x * 60 - 5) % 30 != 0 else 0)
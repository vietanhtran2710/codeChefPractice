t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    print((z - y) // x)
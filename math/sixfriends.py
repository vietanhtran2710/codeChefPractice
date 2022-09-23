t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print(min(3 * x, 2 * y))
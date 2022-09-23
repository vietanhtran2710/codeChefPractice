t = int(input())
for i in range(t):
    x, y, m = map(int, input().split())
    print("YES" if x * m < y else "NO")
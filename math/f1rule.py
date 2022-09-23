t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print("YES" if y <= x / 100 * 107 else "NO")
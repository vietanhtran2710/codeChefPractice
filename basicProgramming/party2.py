t = int(input())
for i in range(t):
    n, x, k = map(int, input().split())
    print("YES" if k >= n * x else "NO")
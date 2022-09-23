t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    print(n // 6 * x + (x if n % 6 != 0 else 0))
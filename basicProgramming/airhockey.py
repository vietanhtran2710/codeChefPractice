t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(min(7 - a, 7 - b))
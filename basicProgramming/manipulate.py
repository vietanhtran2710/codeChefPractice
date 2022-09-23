t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    print("NO") if x < y else print("YES")
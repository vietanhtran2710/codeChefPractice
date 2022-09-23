arr = map(int, input().split())
print([i >= 10 for i in arr].count(True))
from collections import Counter
for i in range(int(input())):
    _ = input()
    arr = list(map(int, input().split()))
    dct = Counter(arr)
    _max = max(dct.values())
    print(len(arr) - _max)
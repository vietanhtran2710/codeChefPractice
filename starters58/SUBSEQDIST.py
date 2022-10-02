from collections import Counter
from math import ceil, log
for i in range(int(input())):
    _ = input()
    arr = map(int, input().split())
    dct = Counter(arr)
    max_freq = max(dct.values())
    print(ceil(log(max_freq, 2)))

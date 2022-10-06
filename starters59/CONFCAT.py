for _ in range(int(input())):
    n = input()
    c = list(map(int, input().split()))
    note = ["" for i in c]
    i = 1
    while i < len(c) and c[i] < c[0]:
        i += 1
    if i == len(c):
        print(-1)
    else:
        print(i)
        print(" ".join(map(str, c[:i])))
        print(len(c) - i)
        print(" ".join(map(str, c[i:])))
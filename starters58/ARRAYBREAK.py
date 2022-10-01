for _ in range(int(input())):
    _ = input()
    arr = list(map(int, input().split()))
    cood, ceven = 0, 0
    for item in arr:
        if item % 2 == 0:
            ceven += 1
        else:
            cood += 1
    if cood == len(arr) or ceven == len(arr):
        print(0)
    else:
        print(ceven)
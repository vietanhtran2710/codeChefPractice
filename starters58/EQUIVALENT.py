for i in range(int(input())):
    a, b = map(int, input().split())
    no = False
    while a != b:
        if a < b:
            a, b = b, a
        if a % b != 0:
            print("NO")
            no = True
            break
        else:
            a, b = a // b, b
    if not no:
        print("YES")
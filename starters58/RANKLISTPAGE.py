for _ in range(int(input())):
    x = int(input())
    print(x // 25 + (1 if x % 25 != 0 else 0))
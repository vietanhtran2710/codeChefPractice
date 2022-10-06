for _ in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    m = input()
    b = list(map(int, input().split()))
    left_sums, right_sums = [], []
    s, i = 0, 0
    while i < len(a):
        s += a[i]
        left_sums.append(s)
        i += 1
    s, i = 0, len(a) - 1
    while i >= 0:
        s += a[i]
        right_sums.append(s)
        i -= 1
    start_sum, end_sum = max(left_sums), max(right_sums)
    s, e = 0, len(a) - 1
    while s < len(a) and a[s] >= 0:
        start_sum += a[s]
        s += 1
    while e >= 0 and a[e] >= 0:
        end_sum += a[e]
        e -= 1
    s, e = 0, len(b) - 1
    while s <= e:
        if b[s] >= 0 and b[e] >= 0:
            if b[s] >= b[e]:
                if start_sum < end_sum:
                    a.append(b[s])
                else:
                    a.insert(0, b[s])
                s += 1
            else:
                if start_sum < end_sum:
                    a.append(b[e])
                else:
                    a.insert(0, b[e])
                e -= 1
        else:
            if b[s] >= 0:
                if start_sum < end_sum:
                    a.append(b[s])
                else:
                    a.insert(0, b[s])
                s += 1
            elif b[e] >= 0:
                if start_sum < end_sum:
                    a.append(b[e])
                else:
                    a.insert(0, b[e])
                e -= 1
            else:
                if b[s] < b[e]:
                    if start_sum >= end_sum:
                        a.append(b[s])
                    else:
                        a.insert(0, b[s])
                    s += 1
                else:
                    if start_sum >= end_sum:
                        a.append(b[e])
                    else:
                        a.insert(0, b[e])
                    e -= 1
    sums = []
    s, i = 0, 0
    while i < len(a):
        s += a[i]
        sums.append(s)
        i += 1
    s, i = 0, len(a) - 1
    while i >= 0:
        s += a[i]
        sums.append(s)
        i -= 1
    print(max(sums))
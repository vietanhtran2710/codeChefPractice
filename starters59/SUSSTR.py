for _ in range(int(input())):
    n = input()
    s = input()
    t = ""
    while s != "":
        if s[0] == "1":
            t = t + "1"
        else:
            t = "0" + t
        s = s[1:]
        if s == "":
            break
        if s[-1] == "1":
            t = "1" + t
        else:
            t = t + "0"
        s = s[:-1]
    print(t)
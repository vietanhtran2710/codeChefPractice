MOD = 998244353
for _ in range(int(input())):
    s = input()
    single = [0 for i in s]
    double = [0 for i in s]
    single[0], double[0] = 1, 0
    for i in range(len(s) - 1):
        single[i + 1] = (single[i] + double[i]) % MOD
        if s[i] != s[i + 1]:
            double[i + 1] = (double[i + 1] + single[i]) % MOD
    print((single[len(s) - 1] + double[len(s) - 1]) % MOD)
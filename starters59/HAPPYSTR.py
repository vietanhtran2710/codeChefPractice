vowels = "ueoai"
for _ in range(int(input())):
    s = input()
    happy = False
    for i in range(len(s) - 3):
        if s[i] in vowels and s[i + 1] in vowels and s[i + 2] in vowels:
            happy = True
            break
    print("HAPPY" if happy else "SAD")
    
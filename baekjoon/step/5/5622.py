dial = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = input()

time = 0
for i in range(len(s)):
    time += 2
    for j in range(1, len(dial)):
        if dial[j].find(s[i]) != -1:
            time += j
            break

print(time)

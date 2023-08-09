s = input()
alpha = [-1 for _ in range(26)]

for i in range(len(s)):
    loc = ord(s[i]) - 97

    if alpha[loc] == -1:
        alpha[loc] = i

for i in range(26):
    print(alpha[i], end=' ')
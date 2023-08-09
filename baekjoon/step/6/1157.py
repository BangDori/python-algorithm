word = input().upper()
alpha = [-1 for _ in range(26)]

for i in range(len(word)):
    alpha[ord(word[i]) - 65] += 1

answer = alpha.copy()
answer.sort(reverse=True)

if answer[0] == answer[1]:
    print('?')
else:
    print(chr(alpha.index(answer[0])+65))
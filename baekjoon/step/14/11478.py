# 문자열 S
S = input()
subString = {}

for i in range(len(S)):
    for j in range(len(S)):
        if not subString.get(S[j:j+i+1]):
            subString[S[j:j+i+1]] = 1

print(subString.__len__())
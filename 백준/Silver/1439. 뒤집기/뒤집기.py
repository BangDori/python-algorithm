S = list(map(int, list(input().strip())))

if len(S) == sum(S) or sum(S) == 0:
    print(0)
else:
    S.append(-1)
    group = [0, 0]

    for i in range(1, len(S)):
        if S[i-1] != S[i]:
            group[S[i-1]] += 1

    print(min(group))
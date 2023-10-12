"""
    1 sec, 256 MB

    문자열에서 특정 알파벳이 몇번 나타나는지

    특정 문자열 S, 특정 알파벳 a와 문자열 구간 [l, r]
    S의 l ~ r 사이에 a가 몇 번 나타나는지

    0부터 세고, l ~ r 번째 문자를 포함해서 생각
"""

import sys
input = sys.stdin.readline

S = input().strip()
q = int(input().strip())
dic = {}

alpha = [0] * 26
alpha[ord(S[0]) - ord('a')] += 1
dic[0] = alpha

for idx in range(1, len(S)):
    dic[idx] = dic[idx-1].copy()
    dic[idx][ord(S[idx])-ord('a')] += 1  

for _ in range(q):
    a, l, r = input().split()

    a = ord(a) - ord('a')
    l = int(l)
    r = int(r)

    if l == 0:
        print(dic[r][a])
    else:
        print(dic[r][a] - dic[l-1][a])
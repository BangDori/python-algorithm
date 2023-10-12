import sys
input = sys.stdin.readline

S = input().rstrip()
splitted_S = []

continuous_ch = ''
isStart = False
for ch in S:
    if ch == '<':
        if continuous_ch != '': splitted_S.append(continuous_ch)
        continuous_ch = '<'

        isStart = True

        continue

    if ch == ' ' and not isStart:
        splitted_S.append(continuous_ch)
        splitted_S.append(ch)
        continuous_ch = ''

        continue

    continuous_ch += ch

    if ch == '>':
        isStart = False
        splitted_S.append(continuous_ch)
        continuous_ch = ''

if continuous_ch != '':
    splitted_S.append(continuous_ch)

for s in splitted_S:
    if s.find('<') != -1 or s.find('>') != -1:
        print(s, end='')
    else:
        print(s[::-1], end='')
import sys, re
input = sys.stdin.readline

# (100+1+|01)+
REG_EXP = "(100+1+|01)+"

TC = int(input())
answer = []

for _ in range(TC):
    pattern = input().strip()
    p = re.compile(REG_EXP)
    star_vega = p.fullmatch(pattern)

    if star_vega: answer.append("YES")
    else: answer.append("NO")

for ans in answer:
    print(ans)
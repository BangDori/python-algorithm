import sys
input = sys.stdin.readline

formula = input().rstrip()

parenthis_stack = []
parenthis = []

for i in range(len(formula)):
    if formula[i] == '(':
        parenthis_stack.append((i, '('))
    
    if formula[i] == ')':
        open = parenthis_stack.pop()
        parenthis.append((open[0], i))

if len(parenthis) == 0:
    print(formula)
    sys.exit(0)

answer = []
for i in range(1, pow(2, len(parenthis))):
    order = bin(i)[2:][::-1]

    comb = []
    result = formula
    for k in range(len(order)):
        if order[k] == '0':
            continue

        comb.append((parenthis[int(k)]))

    removed = []
    for open, close in comb:
        removed.append(open)
        removed.append(close)
    
    removed.sort(reverse=True)
    for remove in removed:
        result = result[:remove] + result[remove+1:]

    if answer.count(result) == 0:
        answer.append(result)

answer.sort()
for ans in answer:
    print(ans)
import sys
input = sys.stdin.readline

def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

# 난이도 의견의 개수 (n)
n = int(input())

if n == 0:
    print(0)
else:
    scores = []
    for _ in range(n):
        scores.append(int(input()))

    scores.sort()
    exception_number = round(n * 0.15)
    scores = scores[exception_number:n-exception_number]

    result = sum(scores)

    print(round(result/len(scores)))
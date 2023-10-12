import sys
input = sys.stdin.readline

def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if n == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(n)]
    scores.sort()

    except_num = round(n * 0.15)
    size = n - 2 * except_num
    sum = sum(scores[except_num:n-except_num])

    print(round(sum / size))

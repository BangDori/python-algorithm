import sys
input = sys.stdin.readline

n = input().strip()
answer = -1

if int(n) >= 30:
    n = list(map(int, list(n)))

    if sum(n) % 3 == 0:
        n.sort(reverse=True)

        if n[-1] == 0:
            answer = "".join(list(map(str, n)))
        
print(answer)
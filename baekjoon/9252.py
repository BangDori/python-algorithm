import sys
input = sys.stdin.readline

def solution(wordA, wordB):
    x = len(wordA); y = len(wordB)
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if wordA[i-1] == wordB[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    ptrX, ptrY = x, y

    answer = []
    while ptrX != 0 and ptrY != 0:
        if wordA[ptrX-1] == wordB[ptrY-1]:
            answer.append(wordA[ptrX-1])
            ptrX -= 1
            ptrY -= 1
            continue
        if dp[ptrX][ptrY] == dp[ptrX][ptrY-1]:
            ptrY -= 1
            continue
            
        if dp[ptrX][ptrY] == dp[ptrX-1][ptrY]:
            ptrX -= 1
            continue

    answer.reverse()
    print(dp[-1][-1])
    print("".join(answer))


wordA = input().rstrip()
wordB = input().rstrip()

solution(wordA, wordB)
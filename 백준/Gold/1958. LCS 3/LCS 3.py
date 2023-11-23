import sys
input = sys.stdin.readline

wordA = input().rstrip()
wordB = input().rstrip()
wordC = input().rstrip()

def lcs(wordA, wordB, wordC):
    lenA = len(wordA)
    lenB = len(wordB)
    lenC = len(wordC)
    dp = [[[0 for _ in range(lenC+1)] for _ in range(lenB+1)] for _ in range(lenA+1)]

    # a, b에 대한 최장 부분 수열 구하기
    for a in range(1, lenA+1):
        for b in range(1, lenB+1):
            for c in range(1, lenC+1):
                if wordA[a-1] == wordB[b-1] == wordC[c-1]:
                    dp[a][b][c] = dp[a-1][b-1][c-1] + 1
                else:
                    dp[a][b][c] = max(dp[a-1][b][c], dp[a][b-1][c], dp[a][b][c-1])
    
    return dp[-1][-1][-1]

result = lcs(wordA, wordB, wordC)
print(result)
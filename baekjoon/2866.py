import sys
input = sys.stdin.readline

row, col = map(int, input().split())
table = [list(input().rstrip()) for _ in range(row)]

def isDuplication(words, mid):
    unique_words = set()

    for idx, word in enumerate(words):
        unique_words.add(word[mid:])
        
        if len(unique_words) != idx+1:
            return True

    return False

def solution(row, col, table):
    words = []  

    for y in range(col):
        query = ''
        for x in range(row):
            query += table[x][y]
        words.append(query)

    start = 0
    end = row
    answer = (start+end)//2

    while start <= end:
        mid = (start+end)//2

        isDup = isDuplication(words, mid)

        if isDup:
            end = mid-1
        else:
            answer = mid
            start = mid+1

    return answer

answer = solution(row, col, table)
print(answer)
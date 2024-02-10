import sys
input = sys.stdin.readline

word_cnt = int(input())
target = list(input().strip())
answer = 0

for _ in range(word_cnt-1):
    compare = target.copy()
    word = list(input().strip())
    cnt = 0

    for w in word:
        if w in compare: compare.remove(w)
        else: cnt += 1
    
    # 두 단어 구성이 동일하다면: cnt = 0, len(compare) = 0
    # 한 문자를 더하거나, 뺴거나, 바꾸었을때 동일한경우: cnt = 1, len(compare) = 1
    if cnt <= 1 and len(compare) <= 1: answer += 1
        
print(answer)
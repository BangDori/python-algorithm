import sys
sys.setrecursionlimit(20)
input = sys.stdin.readline

def back_tracking(index, count):
    global answer
    if count == k+1:
        read_cnt = 0
        for word in words:
            is_read_word = True

            for alpha in word:
                if not learned[ord(alpha) - ord('a')]:
                    is_read_word = False
                    break
            
            if is_read_word:
                read_cnt += 1
        
        answer = max(answer, read_cnt)
        return

    for i in range(index, 26):
        if not learned[i]:
            learned[i] = True
            back_tracking(i, count+1)
            learned[i] = False

    return

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

answer = 0

if k < 5:
    # 배울 수 있는 단어가 5개 보다 작을 경우
    answer = 0
elif k == 26:
    # 모든 단어를 배우는 경우
    answer = n
else:
    learned = [False] * 26
    essential_alpha = ['a', 'n', 't', 'i', 'c']
    
    for alpha in essential_alpha:
        learned[ord(alpha) - ord('a')] = True
    
    back_tracking(1, 6)

print(answer)
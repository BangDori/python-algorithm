import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

P = 'I' + 'OI'*N

if P not in S:
    print(0)
else:
    answer = 0
    find_start = 0

    while S.count(P, find_start) > 0:
        find_index = S.index(P, find_start)

        result = 1
        i = find_index+2*N+1
        for i in range(find_index+2*N+1, M, 2):
            if i+1 >= M:
                break
            if S[i] == 'O' and S[i+1] == 'I':
                result += 1
            else:   
                break
        
        answer += result
        find_start = i
    
    print(answer)
import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    applicant = int(input())
    ranks = [list(map(int, input().split())) for _ in range(applicant)]
    ranks.sort(key=lambda v: v[0])
    
    answer = 1
    curr = ranks.pop(0)[1]
    for scoreA, scoreB in ranks:
        if scoreB < curr:
            answer += 1
            curr = scoreB

    print(answer)
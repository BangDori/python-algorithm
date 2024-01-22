from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
people.sort()

answer = 0
for i in range(N-2):
    curr_people = people[i]
    left, right = i+1, N-1

    while left < right:
        team_result = people[left] + curr_people + people[right]

        # 0보다 크다면, 오른쪽을 이동시켜서 낮추기
        if team_result > 0:
            right -= 1

        # 0이하
        else:
            if team_result == 0:
                
                if people[left] == people[right]:
                    answer += (right - left)
                else:
                    # people[right]와 동일한 인덱스 -> 이 떄 최대 인덱스를 구함
                    pos = bisect_left(people, people[right])
                    answer += (right - pos + 1)
            
            left += 1

print(answer)
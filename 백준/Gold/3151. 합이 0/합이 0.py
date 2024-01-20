import sys
input = sys.stdin.readline
# 이분탐색

N = int(input())
people = list(map(int, input().split()))
people.sort()

answer = 0

def get_team_count(left, right, goal):
    count = 0

    max_idx = N
    while left < right:
        tmp = people[left] + people[right]

        if tmp < goal:
            left += 1

        elif tmp == goal:
            if people[left] == people[right]:
                count += (right - left)
            else:
                if max_idx > right:
                    max_idx = right
                    while max_idx >= 0 and people[max_idx - 1] == people[right]:
                        max_idx -= 1
                count += right - max_idx + 1

            left += 1

        else:
            right -= 1
    
    return count

for i in range(N - 2):
    start, end = i+1, N-1
    goal = people[i] * -1

    answer += get_team_count(start, end, goal)

print(answer)
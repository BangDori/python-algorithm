import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 수를 정렬한다.

answer = 0
for i in range(N):
    standard = numbers[i]
    temp = numbers[:i] + numbers[i+1:]

    # 0과 i-1을 투 포인터로 잡고, 각각 이동하면서 합이 되는지 확인한다.
    s = 0; e = len(temp)-1

    while s < e:
        total = temp[s] + temp[e]

        if total == standard:
            answer += 1
            break
        
        if total < standard: s += 1
        else: e -= 1

print(answer)
import sys
input = sys.stdin.readline

test_case = int(input())

array = [5]

while array[-1]*5 <= 1000000000:
    array.append(array[-1]*5)

answer = []
for _ in range(test_case):
    n = int(input())

    answer = 0
    for num in array:
        if num > n:
            break
        answer += n//num
    print(answer)
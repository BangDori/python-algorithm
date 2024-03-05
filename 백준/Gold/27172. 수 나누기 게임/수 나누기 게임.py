import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

answer = {}
numbers = []
for card in cards:
    answer[card] = 0
    numbers.append(card)

numbers.sort()
for num in numbers:
    for target in range(num * 2, numbers[-1] + 1, num):
        if target in answer:
            answer[num] += 1
            answer[target] -= 1

print(*answer.values())
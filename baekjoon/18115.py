from collections import deque
import sys
input = sys.stdin.readline

size = int(input())
ops = list(map(int, input().split()))
cards = [0 for _ in range(size)]

ptr = 0
num = size

ptrs = deque([i for i in range(size)])
while ptr < size:
    if ops[ptr] == 1:
        cards[ptrs.popleft()] = num

    if ops[ptr] == 2:
        first = ptrs.popleft()
        second = ptrs.popleft()
        cards[second] = num
        ptrs.appendleft(first)

    if ops[ptr] == 3:
        cards[ptrs.pop()] = num

    ptr += 1
    num -= 1

for card in cards:
    print(card, end=' ')
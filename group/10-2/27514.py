import sys
input = sys.stdin.readline

length = int(input())
array = list(map(int, input().split()))
bits = [0 for _ in range(63)]

for idx in range(len(array)):
    if array[idx] == 0:
        continue
    array[idx] = array[idx].bit_length()-1
    bits[array[idx]] += 1

max = 0
for idx in range(len(bits)):
    if bits[idx] == 0:
        continue

    if idx == 62:
        if bits[idx] >= 1:
            max = idx
        break

    max = idx
    if bits[idx] >= 2:
        bits[idx+1] += bits[idx]//2
        bits[idx] = bits[idx]%2
        max = idx+1

print(2 ** max)
import sys
input = sys.stdin.readline

k = int(input())

bit = 2
count = 1

while True:
    if bit-1 <= k <= bit*2-2:
        break
    count += 1
    bit *= 2

bit -= 1
binary = bin(k-bit)[2:] if len(bin(k-bit)[2:]) == count else '0' * (count-len(bin(k-bit)[2:])) + bin(k-bit)[2:]

for b in binary:
    num = 4 if b == '0' else 7
    print(num, end='')
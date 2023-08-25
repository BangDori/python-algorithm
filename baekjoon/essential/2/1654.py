def binary_search(lines, key):
    lengths = []
    start = 1
    last = lines[len(lines)-1]
    while start <= last:
        middle = int((start+last)/2)

        tot_lines = 0
        for line in lines:
            tot_lines += (line // middle)
        if tot_lines >= key:
            lengths.append(middle)
            start = middle + 1
        else:
            last = middle - 1
    
    return max(lengths)


import sys
input = sys.stdin.readline

# 기존의 랜선의 개수 (K)
# 새로운 랜선의 개수 (N)
K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]
lines.sort()

max_length = binary_search(lines, N)
print(max_length)
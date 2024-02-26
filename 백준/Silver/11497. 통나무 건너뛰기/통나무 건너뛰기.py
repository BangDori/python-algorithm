import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    count = int(input())
    heights = list(map(int, input().split()))
    heights.sort()

    answer = 0

    if count == 1: answer = 0
    elif count == 2: answer = abs(heights[0] - heights[1])
    else:
        sorted_heights = [0 for _ in range(count)]
        sorted_heights[count//2] = heights[-1]

        for i in range(count-2, -1, -2):
            idx = (count - i) // 2
            sorted_heights[count//2 - idx] = heights[i]

        for i in range(count-3, -1, -2):
            idx = ((count-1) - i) // 2
            sorted_heights[count//2 + idx] = heights[i]

        for i in range(count):
            answer = max(answer, abs(sorted_heights[i] - sorted_heights[i-1])) 

    print(answer)
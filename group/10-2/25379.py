import sys
def input():
    return sys.stdin.readline().rstrip()

length = int(input())
array = list(map(int, input().split()))

for i in range(len(array)):
    array[i] %= 2

array = [array, array.copy()]

if length == 1:
    print(0)
else:
    answer = sys.maxsize
    last = [0, 1]

    for last_num in last:
        cnt = 0
        start_pos = length
        end_pos = length

        while True:
            start = -1
            end = -1

            for i in range(start_pos-1, -1, -1):
                if start == -1 and array[last_num][i] != last_num:
                    start = i
                    break
            
            if start_pos == end_pos:
                end_pos = start

            for i in range(end_pos-1, -1, -1):            
                if start != -1 and array[last_num][start] != array[last_num][i]:
                    end = i
                    break
            
            if end == -1:
                if answer > cnt:
                    answer = cnt
                break
            
            start_pos = start
            end_pos = end

            array[last_num][start], array[last_num][end] = array[last_num][end], array[last_num][start]
            cnt += (start-end)

    print(answer)
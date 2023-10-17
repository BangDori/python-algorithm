import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    input_string = input().rstrip()
    splitted = input_string.split()
    tid, sid = int(splitted[0]), list(map(int, splitted[1:]))
    answer = 0

    for idx in range(len(sid)):
        min_sid = sid.index(min(sid[idx:]))
        if idx == min_sid:
            continue
        
        for jdx in range(min_sid, idx, -1):
            sid[jdx], sid[jdx-1] = sid[jdx-1], sid[jdx]
        answer += min_sid-idx

    print(tid, answer)
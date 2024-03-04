import sys
input = sys.stdin.readline

EIGHT = '8'

# 숫자에 8이 포함된 갯수 구하기
def comapre_numbers(l, r):
    length = len(l)
    count = 0

    for i in range(length):
        if l[i] == r[i]:
            if l[i] == EIGHT:
                count += 1
        else:
            break

    return count

l, r = input().strip().split()

answer = 0
if l.count(EIGHT) == 0 or r.count(EIGHT) == 0: answer = 0
elif len(l) == len(r):
    answer = comapre_numbers(l, r)
    
print(answer)
import sys
input = sys.stdin.readline

before = input().rstrip()
after = input().rstrip()

if sorted(before) != sorted(after):
    print(-1)
else:
    count = 0
    k = len(after)-1
    
    for i in range(len(before)-1, -1, -1):
        if after[k] != before[i]:
            count += 1
        else:
            k -= 1

    print(count)
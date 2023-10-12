import sys, itertools
input = sys.stdin.readline

n = input().rstrip()
min_odd_count = sys.maxsize
max_odd_count = 0

def dfs(num, odd_count):
    # 종료 조건 (한 자리)
    if len(num) == 1:
        global min_odd_count, max_odd_count

        odd_count += int(num) % 2

        if odd_count > max_odd_count:
            max_odd_count = odd_count
        if odd_count < min_odd_count:
            min_odd_count = odd_count
        return
    elif len(num) == 2:
        # 로직 (두 자리)
        a = int(num[-1])
        b = int(num[-2])
        
        cur_odd_count = 0
        
        if a % 2 == 1: cur_odd_count += 1
        if b % 2 == 1: cur_odd_count += 1
        
        dfs(str(a+b), odd_count + cur_odd_count)
    else:
        cur_odd_count = 0

        for n in num:
            if int(n) % 2 == 1:
                cur_odd_count += 1

        for k in itertools.combinations(range(1, len(num)), 2):
            a = int(num[0:k[0]])
            b = int(num[k[0]:k[1]])
            c = int(num[k[1]:])

            dfs(str(a+b+c), odd_count + cur_odd_count)

dfs(n, 0)
print(min_odd_count, max_odd_count)

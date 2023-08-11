n = int(input())
tot = 4

for i in range(1, n+1):
    cur = pow(2, i-1)
    add = (cur * 2 * (cur+1)) + pow(cur, 2)
    tot += add

print(tot)
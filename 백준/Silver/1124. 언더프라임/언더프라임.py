import sys, math
input = sys.stdin.readline

def get_prime_list(end):
    is_prime = [True for _ in range(end + 1)]
    is_prime[1] = False

    for i in range(2, int(end ** 0.5)+1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False
    
    return is_prime

def find(n):
    cnt = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            cnt += 1
            n //= i

    if n != 1:
        cnt+=1

    return cnt

start, end = map(int,input().split())
is_prime = get_prime_list(end)

answer = 0
for i in range(start, end+1):
    if is_prime[find(i)]: answer += 1

print(answer)
import sys
input = sys.stdin.readline

K = int(input())
wallet = []
sum = 0

for _ in range(K):
    money = int(input())

    if money == 0:
        sum -= wallet.pop()

    else:
        sum += money
        wallet.append(money)

print(sum)
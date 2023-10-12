import sys
input = sys.stdin.readline

prime = [True] * 1000000
prime[0] = prime[1] = False

size = int(len(prime) ** 0.5)
for idx in range(size):
    if prime[idx]:
        for jdx in range(idx+idx, len(prime), idx):
            prime[jdx] = False

prime_num = []
for idx in range(len(prime)):
    if prime[idx]:
        prime_num.append(idx)

while True:
    test = int(input())

    if test == 0:
        break

    if test <= 4 or test % 2 == 1:
        print("Goldbach's conjecture is wrong.")
        continue

    for num in prime_num:
        if prime[test-num]:
            print("%d = %d + %d" % (test, num, test-num))
            break
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    binA, binB = map(int, input().split())

    numA = 0
    acc = 1
    while binA > 0:
        numA += (acc * (binA % 10))
        acc *= 2
        binA //= 10
    
    numB = 0
    acc = 1
    while binB > 0:
        numB += (acc * (binB % 10))
        acc *= 2
        binB //= 10
    
    result = numA + numB
    print(bin(result)[2:])
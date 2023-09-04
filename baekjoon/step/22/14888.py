"""
    2 sec, 512 MB

    N개의 수, N-1개의 연산자 (+, -, x, /)

    주어진 수의 위치는 고정, 연산자의 위치만 변경    
    연산자 우선 순위 무시 후 진행

    음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈
    -1 // 3 => 1 // 3 => 0
    -4 // 3 => 4 // 3 => 1 => -1

    만들 수 있는 식의 결과가 최대인 것과 최소인 것
"""

import sys, itertools
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

min = sys.maxsize
max = -sys.maxsize

# 합이 N-1인 4개의 정수
ops_count = list(map(int, input().split()))
operand = ['+', '-', '*', '/']
operands = []

for idx, op in enumerate(ops_count):
    if op == 0:
        continue
    operands += (op * [operand[idx]])

ways = list(itertools.permutations(operands, N-1))

for way in ways:
    sum = A[0]
    for idx, op in enumerate(way):
        if op == '+':
            sum += A[idx+1]
        elif op == '-':
            sum -= A[idx+1]
        elif op == '*':
            sum *= A[idx+1]
        else:
            if A[idx+1] == 0:
                continue
            if sum < 0:
                sum = abs(sum) // A[idx+1]
                sum = -sum
            else:
                sum //= A[idx+1]
    if sum > max:
        max = sum
    if sum < min:
        min = sum
print(max)
print(min)
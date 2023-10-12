# 집합 A의 원소의 개수 (A), B의 원소의 개수 (B)
A, B = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(len(set_a-set_b) + len(set_b-set_a))
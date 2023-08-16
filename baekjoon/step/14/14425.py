# 집합 S에 포함되어 있는 문자열의 수 (N)
# 검새야 하는 문자열의 수 (M)
N, M = map(int, input().split())
list = [_ for _ in range(N)]

for i in range(N):
    list[i] = input()

count = 0
for i in range(M):
    check_str = input()
    if list.count(check_str):
        count += 1

print(count)
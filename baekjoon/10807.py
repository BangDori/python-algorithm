n = int(input())
array = [0 for _ in range(n)]
array = list(map(int, input().split()))
find = int(input())

print(array.count(find))
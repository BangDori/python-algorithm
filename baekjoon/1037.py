# 약수의 개수
N = int(input())
array = list(map(int, input().split()))

array.sort()
print(array[0] * array[len(array)-1])
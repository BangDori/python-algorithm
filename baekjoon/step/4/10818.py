n = int(input())
array = list(map(int, input().split()))
min, max = array[0], array[0]

for i in range(len(array)):
    if min > array[i]:
        min = array[i]
    
    if max < array[i]:
        max = array[i]

print(min, max)
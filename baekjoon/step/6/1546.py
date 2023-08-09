n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)

max = array[0]
sum = 0
for i in range(n):
    array[i] = array[i]/max * 100
    sum += array[i]

print(sum / n)
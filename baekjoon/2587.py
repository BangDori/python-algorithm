array = [0 for _ in range(5)]

sum = 0
for i in range(5):
    array[i] = int(input())
    sum += array[i]

array.sort()

print(sum // len(array))
print(array[len(array)//2])